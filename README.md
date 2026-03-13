# Plataforma de Gestão de Carteira (B3)

Este repositório agora inclui um **site web funcional** (MVP) para gestão de carteira de investimentos, inspirado no fluxo de acompanhamento de patrimônio, ativos e sincronização da carteira.

## O que já existe

- Dashboard com visão resumida de patrimônio e métricas estimadas.
- Cadastro manual de ativos com persistência local (LocalStorage).
- Simulação de sincronização de carteira.
- Tema claro/escuro.
- Estrutura de documentação de produto e arquitetura para evolução.

## Estrutura

- `web/index.html`: interface da plataforma
- `web/styles.css`: estilos visuais responsivos
- `web/app.js`: lógica do dashboard e carteira
- `docs/product-spec.md`: escopo de produto e roadmap
- `docs/architecture.md`: arquitetura proposta para escalar
- `docs/integration-b3.md`: estratégia de sincronização e conciliação
- `docs/openapi.yaml`: contrato inicial de API

## Como executar localmente

Você pode abrir de duas formas:

1. Abrir `web/index.html` diretamente no navegador, ou
2. Rodar servidor local simples:

```bash
cd web
python3 -m http.server 4173
```

Depois acesse `http://localhost:4173`.

## Como ter acesso de qualquer lugar

Para disponibilizar na internet:

1. Suba este repositório no GitHub.
2. Faça deploy estático em Vercel, Netlify, Cloudflare Pages ou GitHub Pages.
3. Aponte um domínio próprio (opcional).
4. Em próximas fases, conecte o frontend ao backend/API para autenticação e sincronização real.

## Próximos passos recomendados

1. Implementar backend (auth + portfolio + sync jobs).
2. Integrar provedor de dados de mercado e eventos corporativos.
3. Evoluir conciliação automática e trilha de auditoria.
4. Adicionar módulo tributário (IR) e relatórios avançados.
