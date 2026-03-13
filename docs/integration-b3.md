# Estratégia de Integração e Sincronização de Carteira (B3)

## 1. Objetivo

Permitir atualização automatizada e confiável da carteira do usuário com base em movimentações de mercado brasileiro, com reconciliação e rastreabilidade.

## 2. Princípios

- Consentimento explícito do usuário
- Menor privilégio e minimização de dados
- Reprocessamento idempotente
- Auditoria completa de importações

## 3. Fontes de dados possíveis

- Integrações oficiais/parceiros autorizados
- Upload de extrato em formatos suportados
- Integração com APIs de cotações e fundamentalistas

## 4. Pipeline de importação

1. **Coleta**: captura dados brutos por fonte.
2. **Validação**: schema, assinatura/campos obrigatórios, duplicidade.
3. **Normalização**: compra, venda, bonificação, desdobramento, grupamento, dividendos, JCP.
4. **Conciliação**: cálculo de posição por ativo e custo médio.
5. **Persistência**: gravação transacional e versionamento de eventos.
6. **Notificação**: feedback de sucesso/erro para o usuário.

## 5. Tratamento de inconsistências

- Regras de detecção de transações conflitantes.
- Fila de pendências para revisão manual.
- Histórico de correções com motivo e timestamp.

## 6. UX de sincronização

- Tela de status da sincronização (última execução, duração, erros).
- Botão de reprocessar período.
- Resumo do que mudou após cada sincronização.

## 7. Compliance

- Política clara de retenção de dados.
- Mecanismo de revogação de consentimento.
- Exclusão de dados sob solicitação (LGPD).
