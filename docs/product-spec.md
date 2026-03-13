# Product Spec — Plataforma de Gestão de Carteira B3

## 1. Visão do Produto

Plataforma web para investidores brasileiros com análise de ativos e gestão de carteira, incluindo sincronização automatizada de movimentações, cálculo de posição consolidada e visão de desempenho por classe de ativo.

## 2. Perfis de Usuário

- **Investidor iniciante**: quer consolidar carteira e entender desempenho.
- **Investidor intermediário**: quer comparar ativos e acompanhar proventos.
- **Investidor avançado**: quer indicadores, alocação, risco e histórico detalhado.

## 3. Problemas que o produto resolve

1. Dados de investimento dispersos em corretoras e planilhas.
2. Dificuldade em acompanhar custo médio e rentabilidade real.
3. Falta de visão unificada de proventos, eventos e metas.

## 4. Escopo MVP

### 4.1 Funcionalidades obrigatórias

- Cadastro e autenticação segura
- Onboarding com criação de carteira
- Importação de movimentações (arquivo/integração)
- Dashboard com:
  - patrimônio total
  - evolução da carteira
  - alocação por classe/setor/ativo
  - rentabilidade consolidada
- Tela de ativo com:
  - preço atual e histórico
  - indicadores principais
  - posição do usuário
- Proventos:
  - histórico por ativo
  - visão mensal/anual
- Alertas e notificações básicas

### 4.2 Fora do MVP

- Recomendação de compra/venda automatizada
- Trading em tempo real
- App mobile nativo (pode vir na fase 2)

## 5. Requisitos não funcionais

- **Segurança**: criptografia em trânsito e repouso; JWT com rotação.
- **Performance**: dashboard principal em até 2s para carteira padrão.
- **Escalabilidade**: arquitetura orientada a serviços e filas para jobs.
- **Conformidade**: LGPD (consentimento, minimização de dados, exclusão).
- **Observabilidade**: logs estruturados, métricas e rastreamento.

## 6. KPIs de Sucesso

- Ativação (usuário com carteira criada e importada em D+1)
- Retenção mensal (MAU que abre dashboard >= 4x/mês)
- Erro de conciliação por evento importado < 1%
- Latência P95 da API < 400ms em endpoints críticos

## 7. Roadmap

- **Fase 1 (0-8 semanas)**: Auth, carteira, dashboard básico, importação.
- **Fase 2 (9-16 semanas)**: análise avançada, proventos completos, alertas.
- **Fase 3 (17-24 semanas)**: módulo tributário, metas e otimização de carteira.
