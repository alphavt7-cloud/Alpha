# Plataforma de Gestão de Carteira (B3)

Este repositório contém a base de produto e arquitetura para construir uma plataforma de análise e acompanhamento de ativos da bolsa brasileira, inspirada em funcionalidades de mercado como:

- Dashboard consolidado de carteira
- Sincronização com dados da B3
- Métricas fundamentalistas e comparativos
- Proventos, eventos corporativos e calendário

## Objetivo

Entregar uma plataforma web completa para investidores pessoa física, com foco em:

1. Visão patrimonial em tempo real/near-real-time
2. Análise de ativos (ações, FIIs, ETFs, BDRs e renda fixa)
3. Importação e conciliação automatizada de movimentações
4. Segurança, privacidade e conformidade (LGPD)

## Estrutura inicial

- `docs/product-spec.md`: requisitos de produto, escopo e roadmap.
- `docs/architecture.md`: arquitetura técnica proposta (frontend, backend, dados, filas).
- `docs/integration-b3.md`: estratégia de sincronização com ecossistema B3 e conciliação.
- `docs/openapi.yaml`: contrato inicial da API para autenticação, carteira e sincronização.

## Próximos passos recomendados

1. Validar escopo MVP com 5 a 10 usuários.
2. Escolher stack final e iniciar o backend (auth + carteira + importações).
3. Construir dashboard principal e fluxo de onboarding.
4. Integrar provedores de dados de mercado e pipeline de preços.
5. Evoluir para módulos de IR e relatórios avançados.
