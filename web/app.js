const formatBRL = (value) =>
  new Intl.NumberFormat("pt-BR", {
    style: "currency",
    currency: "BRL"
  }).format(value);

const storageKey = "alpha-carteira-assets";
const assets = JSON.parse(localStorage.getItem(storageKey) || "[]");

const cards = document.getElementById("dashboard");
const rows = document.getElementById("assetRows");
const form = document.getElementById("assetForm");
const tickerInput = document.getElementById("ticker");
const quantityInput = document.getElementById("quantity");
const avgPriceInput = document.getElementById("avgPrice");

const syncNow = document.getElementById("syncNow");
const syncStatus = document.getElementById("syncStatus");
const syncTime = document.getElementById("syncTime");
const themeToggle = document.getElementById("themeToggle");

function persist() {
  localStorage.setItem(storageKey, JSON.stringify(assets));
}

function totals() {
  const invested = assets.reduce((acc, item) => acc + item.quantity * item.avgPrice, 0);
  const monthlyIncome = invested * 0.006;
  const estimatedReturn = invested * 0.11;

  return {
    invested,
    monthlyIncome,
    estimatedReturn,
    assetsCount: assets.length
  };
}

function renderCards() {
  const { invested, monthlyIncome, estimatedReturn, assetsCount } = totals();
  cards.innerHTML = [
    { title: "Patrimônio investido", value: formatBRL(invested) },
    { title: "Renda passiva estimada/mês", value: formatBRL(monthlyIncome), positive: true },
    { title: "Retorno estimado 12m", value: formatBRL(estimatedReturn), positive: true },
    { title: "Ativos na carteira", value: String(assetsCount) }
  ]
    .map(
      (metric) => `
      <article class="card">
        <p>${metric.title}</p>
        <div class="metric ${metric.positive ? "positive" : ""}">${metric.value}</div>
      </article>`
    )
    .join("");
}

function renderRows() {
  rows.innerHTML = assets
    .map(
      (item, index) => `
      <tr>
        <td>${item.ticker}</td>
        <td>${item.quantity}</td>
        <td>${item.avgPrice.toFixed(2)}</td>
        <td>${(item.quantity * item.avgPrice).toFixed(2)}</td>
        <td><button data-index="${index}" class="remove">Remover</button></td>
      </tr>`
    )
    .join("");

  rows.querySelectorAll(".remove").forEach((btn) => {
    btn.addEventListener("click", () => {
      assets.splice(Number(btn.dataset.index), 1);
      persist();
      render();
    });
  });
}

form.addEventListener("submit", (event) => {
  event.preventDefault();

  const newAsset = {
    ticker: tickerInput.value.trim().toUpperCase(),
    quantity: Number(quantityInput.value),
    avgPrice: Number(avgPriceInput.value)
  };

  if (!newAsset.ticker || newAsset.quantity <= 0 || newAsset.avgPrice < 0) {
    return;
  }

  assets.push(newAsset);
  persist();
  form.reset();
  render();
});

syncNow.addEventListener("click", () => {
  syncStatus.textContent = "Sincronizando...";
  syncStatus.style.background = "#dbeafe";
  syncStatus.style.color = "#1e3a8a";

  setTimeout(() => {
    syncStatus.textContent = "Sincronizado com sucesso";
    syncStatus.style.background = "#dcfce7";
    syncStatus.style.color = "#14532d";
    syncTime.textContent = `Última sincronização: ${new Date().toLocaleString("pt-BR")}`;
  }, 1200);
});

themeToggle.addEventListener("click", () => {
  document.documentElement.classList.toggle("dark");
  themeToggle.textContent = document.documentElement.classList.contains("dark") ? "☀️" : "🌙";
});

function render() {
  renderCards();
  renderRows();
}

render();
