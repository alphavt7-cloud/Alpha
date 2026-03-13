# Arquitetura Técnica Proposta

## 1. Visão geral

Arquitetura em camadas com separação entre experiência do usuário, APIs de domínio e processamento assíncrono de sincronização.

- **Frontend (Web SPA/SSR)**: dashboard, análise de ativos e configurações.
- **API Gateway/BFF**: autenticação, agregação de dados para telas.
- **Serviços de domínio**:
  - `portfolio-service`
  - `market-data-service`
  - `corporate-events-service`
  - `notification-service`
- **Workers/Jobs**: ingestão de extratos, conciliação de carteira, atualização de preços.

## 2. Stack sugerida (referência)

- **Frontend**: Next.js + TypeScript + Tailwind
- **Backend**: Node.js (NestJS/Fastify) ou Python (FastAPI)
- **Banco relacional**: PostgreSQL
- **Cache**: Redis
- **Fila**: RabbitMQ ou SQS
- **Observabilidade**: OpenTelemetry + Prometheus + Grafana

## 3. Modelo de dados (alto nível)

Entidades principais:

- `users`
- `portfolios`
- `assets`
- `positions`
- `transactions`
- `dividends`
- `price_history`
- `sync_jobs`

## 4. Fluxo de sincronização

1. Usuário concede consentimento para sincronização.
2. Sistema cria `sync_job`.
3. Worker coleta dados no provedor integrado.
4. Parser normaliza eventos para o modelo interno.
5. Motor de conciliação recalcula posições e custo médio.
6. Dashboard é invalidado em cache e atualizado.

## 5. Segurança

- OAuth2/OIDC para login social opcional.
- MFA opcional para conta.
- Segredos em cofre (Vault/Secrets Manager).
- Criptografia de dados sensíveis (KMS).
- Trilha de auditoria para ações críticas.

## 6. Estratégia de deploy

- Ambiente: `dev`, `staging`, `prod`
- CI/CD com testes automatizados e migrações versionadas
- Deploy canário para reduzir risco de regressão
