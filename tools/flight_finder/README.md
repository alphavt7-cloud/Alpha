# Flight Finder (Google Flights)

Ferramenta de linha de comando para buscar passagens aéreas mais baratas **nacionais e internacionais**, baseada no Google Flights.

## Como funciona

- **Com chave `SERPAPI_API_KEY`**: consulta resultados do Google Flights via SerpApi (`engine=google_flights`) e ordena pelo menor preço.
- **Sem chave**: gera links prontos do Google Flights para comparação manual.

## Requisitos

- Python 3.10+
- (Opcional) Chave SerpApi: <https://serpapi.com/google-flights-api>

## Exemplos

### 1) Viagem nacional (ida e volta)

```bash
python3 tools/flight_finder/google_flights_finder.py \
  --origens GRU,VCP \
  --destinos GIG,SSA \
  --ida-inicio 2026-06-10 \
  --ida-fim 2026-06-20 \
  --dias-viagem 5 \
  --flex-dias 2 \
  --currency BRL \
  --lang pt-BR \
  --country br
```

### 2) Viagem internacional (somente ida)

```bash
python3 tools/flight_finder/google_flights_finder.py \
  --origens GRU \
  --destinos LIS,MAD,FCO \
  --ida-inicio 2026-09-01 \
  --ida-fim 2026-09-15 \
  --flex-dias 3 \
  --currency EUR \
  --lang pt-BR \
  --country pt
```

## Ativando retorno de preços automático

```bash
export SERPAPI_API_KEY="sua-chave"
```

Depois rode os mesmos comandos acima.
