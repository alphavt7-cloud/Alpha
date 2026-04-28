#!/usr/bin/env python3
"""Ferramenta CLI para buscar passagens baratas baseada em resultados do Google Flights.

Modo 1 (recomendado): consulta preços via SerpApi (engine=google_flights)
- Requer variável de ambiente SERPAPI_API_KEY.

Modo 2 (fallback): gera links diretos do Google Flights para comparação manual.
- Não requer chave, mas não retorna preços automaticamente.
"""

from __future__ import annotations

import argparse
import datetime as dt
import itertools
import json
import os
import sys
import urllib.parse
import urllib.request
from dataclasses import dataclass
from typing import Any

SERPAPI_URL = "https://serpapi.com/search.json"
GOOGLE_FLIGHTS_BASE = "https://www.google.com/travel/flights"


@dataclass
class SearchQuery:
    origem: str
    destino: str
    ida: dt.date
    volta: dt.date | None


def parse_airports(value: str) -> list[str]:
    airports = [v.strip().upper() for v in value.split(",") if v.strip()]
    if not airports:
        raise argparse.ArgumentTypeError("Informe ao menos um aeroporto (ex: GRU,GIG,JFK)")
    return airports


def parse_date(value: str) -> dt.date:
    try:
        return dt.datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError as err:
        raise argparse.ArgumentTypeError(
            f"Data inválida '{value}'. Use o formato YYYY-MM-DD"
        ) from err


def build_queries(
    origens: list[str],
    destinos: list[str],
    ida_inicio: dt.date,
    ida_fim: dt.date,
    flex_dias: int,
    dias_viagem: int | None,
) -> list[SearchQuery]:
    queries: list[SearchQuery] = []
    current = ida_inicio

    while current <= ida_fim:
        for offset in range(-flex_dias, flex_dias + 1):
            ida = current + dt.timedelta(days=offset)
            if ida < ida_inicio or ida > ida_fim:
                continue
            for origem, destino in itertools.product(origens, destinos):
                if origem == destino:
                    continue
                volta = ida + dt.timedelta(days=dias_viagem) if dias_viagem else None
                queries.append(SearchQuery(origem=origem, destino=destino, ida=ida, volta=volta))
        current += dt.timedelta(days=1)

    unique: dict[tuple[str, str, dt.date, dt.date | None], SearchQuery] = {}
    for q in queries:
        unique[(q.origem, q.destino, q.ida, q.volta)] = q
    return list(unique.values())


def google_flights_link(q: SearchQuery, adults: int, currency: str, lang: str) -> str:
    params = {
        "hl": lang,
        "curr": currency,
        "adults": adults,
    }

    route = f"{q.origem}.{q.destino}.{q.ida.isoformat()}"
    if q.volta:
        route = f"{route}*{q.destino}.{q.origem}.{q.volta.isoformat()}"

    encoded = urllib.parse.urlencode(params)
    return f"{GOOGLE_FLIGHTS_BASE}?{encoded}#flt={route};c:BRL;e:1;sd:1;t:f"


def serpapi_search(q: SearchQuery, api_key: str, adults: int, currency: str, lang: str, country: str) -> dict[str, Any]:
    params = {
        "engine": "google_flights",
        "departure_id": q.origem,
        "arrival_id": q.destino,
        "outbound_date": q.ida.isoformat(),
        "adults": str(adults),
        "currency": currency,
        "hl": lang,
        "gl": country,
        "api_key": api_key,
        "type": "2" if q.volta else "1",
    }
    if q.volta:
        params["return_date"] = q.volta.isoformat()

    url = f"{SERPAPI_URL}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

    with urllib.request.urlopen(req, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def extract_cheapest(data: dict[str, Any]) -> tuple[int | None, str | None]:
    prices: list[tuple[int, str]] = []

    for bucket in ("best_flights", "other_flights"):
        for item in data.get(bucket, []) or []:
            price = item.get("price")
            flights = item.get("flights") or []
            if isinstance(price, int) and flights:
                airline = flights[0].get("airline") or "Companhia desconhecida"
                prices.append((price, airline))

    if not prices:
        return None, None

    return min(prices, key=lambda x: x[0])


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Busca passagens baratas (nacionais/internacionais) com base no Google Flights."
    )
    parser.add_argument("--origens", required=True, type=parse_airports, help="Aeroportos de origem separados por vírgula")
    parser.add_argument("--destinos", required=True, type=parse_airports, help="Aeroportos de destino separados por vírgula")
    parser.add_argument("--ida-inicio", required=True, type=parse_date, help="Data inicial da ida (YYYY-MM-DD)")
    parser.add_argument("--ida-fim", required=True, type=parse_date, help="Data final da ida (YYYY-MM-DD)")
    parser.add_argument("--dias-viagem", type=int, default=None, help="Qtd. de dias da viagem (se informado, busca ida+volta)")
    parser.add_argument("--flex-dias", type=int, default=0, help="Flexibilidade de datas em dias (+/-)")
    parser.add_argument("--adults", type=int, default=1, help="Quantidade de adultos")
    parser.add_argument("--currency", default="BRL", help="Moeda (ex: BRL, USD, EUR)")
    parser.add_argument("--lang", default="pt-BR", help="Idioma da busca")
    parser.add_argument("--country", default="br", help="País para contextualização da busca")
    parser.add_argument("--max-resultados", type=int, default=10, help="Máximo de resultados exibidos")

    args = parser.parse_args()

    if args.ida_fim < args.ida_inicio:
        print("Erro: --ida-fim deve ser maior ou igual a --ida-inicio", file=sys.stderr)
        return 2

    if args.dias_viagem is not None and args.dias_viagem < 1:
        print("Erro: --dias-viagem deve ser >= 1", file=sys.stderr)
        return 2

    queries = build_queries(
        origens=args.origens,
        destinos=args.destinos,
        ida_inicio=args.ida_inicio,
        ida_fim=args.ida_fim,
        flex_dias=args.flex_dias,
        dias_viagem=args.dias_viagem,
    )

    api_key = os.getenv("SERPAPI_API_KEY")
    rows: list[dict[str, Any]] = []

    for q in queries:
        row = {
            "origem": q.origem,
            "destino": q.destino,
            "ida": q.ida.isoformat(),
            "volta": q.volta.isoformat() if q.volta else "-",
            "link_google_flights": google_flights_link(q, args.adults, args.currency, args.lang),
            "preco": None,
            "companhia": None,
        }

        if api_key:
            try:
                data = serpapi_search(q, api_key, args.adults, args.currency, args.lang, args.country)
                cheapest, airline = extract_cheapest(data)
                row["preco"] = cheapest
                row["companhia"] = airline
            except Exception as err:  # pragma: no cover - falha de rede/limite
                row["erro"] = str(err)

        rows.append(row)

    rows.sort(key=lambda r: (r["preco"] is None, r["preco"] or 10**12, r["ida"], r["origem"], r["destino"]))

    print("\n=== MELHORES OPORTUNIDADES ===")
    for r in rows[: args.max_resultados]:
        price_display = f"{args.currency} {r['preco']}" if r["preco"] is not None else "(preço indisponível sem SERPAPI_API_KEY)"
        airline_display = r["companhia"] or "-"
        print(f"- {r['origem']} -> {r['destino']} | ida: {r['ida']} | volta: {r['volta']} | preço: {price_display} | cia: {airline_display}")
        print(f"  {r['link_google_flights']}")

    print("\nDica: defina SERPAPI_API_KEY para retornar preços automaticamente via Google Flights (SerpApi).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
