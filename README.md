 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/README.md b/README.md
new file mode 100644
index 0000000000000000000000000000000000000000..ec5244c02fcc9a9b101402b130c3e412db6b3e7d
--- /dev/null
+++ b/README.md
@@ -0,0 +1,80 @@
+# Plataforma de Gestão de Carteira (B3)
+
+Este repositório agora inclui um **site web funcional** (MVP) para gestão de carteira de investimentos, inspirado no fluxo de acompanhamento de patrimônio, ativos e sincronização da carteira.
+
+## O que já existe
+
+- Dashboard com visão resumida de patrimônio e métricas estimadas.
+- Cadastro manual de ativos com persistência local (LocalStorage).
+- Simulação de sincronização de carteira.
+- Tema claro/escuro.
+- Estrutura de documentação de produto e arquitetura para evolução.
+
+## Estrutura
+
+- `web/index.html`: interface da plataforma
+- `web/styles.css`: estilos visuais responsivos
+- `web/app.js`: lógica do dashboard e carteira
+- `docs/product-spec.md`: escopo de produto e roadmap
+- `docs/architecture.md`: arquitetura proposta para escalar
+- `docs/integration-b3.md`: estratégia de sincronização e conciliação
+- `docs/openapi.yaml`: contrato inicial de API
+
+
+## Acesso (login obrigatório)
+
+O dashboard só é exibido após autenticação com login e senha.
+
+Credencial padrão do MVP:
+
+- **Email**: `investidor@alpha.com`
+- **Senha**: `Alpha@123`
+
+> Observação: neste MVP estático, a autenticação é simulada no navegador (LocalStorage/SessionStorage). Em produção, o login deve ser validado por backend com hash de senha, sessão segura/JWT e controles de segurança adicionais.
+
+## Como executar localmente
+
+Você pode abrir de duas formas:
+
+1. Abrir `web/index.html` diretamente no navegador, ou
+2. Rodar servidor local simples:
+
+```bash
+cd web
+python3 -m http.server 4173
+```
+
+Depois acesse `http://localhost:4173`.
+
+## Como ter acesso de qualquer lugar
+
+### Opção implementada neste repositório: GitHub Pages (deploy automático)
+
+Este projeto já inclui workflow em `.github/workflows/deploy-pages.yml` para publicar automaticamente a pasta `web/` no GitHub Pages.
+
+Passo a passo:
+
+1. Suba o projeto para um repositório no GitHub.
+2. Garanta que a branch padrão seja `main`.
+3. Vá em **Settings → Pages** e em **Build and deployment** selecione **GitHub Actions**.
+4. Faça push na branch `main`.
+5. Aguarde o workflow **Deploy static site to GitHub Pages** finalizar em **Actions**.
+6. Acesse sua URL pública:
+   - `https://SEU_USUARIO.github.io/NOME_DO_REPOSITORIO/`
+
+> Se quiser usar domínio próprio, configure em **Settings → Pages → Custom domain**.
+
+### Outras opções
+
+Você também pode publicar em Vercel, Netlify ou Cloudflare Pages apontando a pasta `web/` como diretório estático.
+
+### Observação importante de segurança
+
+No MVP atual, o login/senha é client-side (simulado no navegador). Para produção real, implemente autenticação server-side com hash de senha, sessão/JWT e controles robustos de segurança.
+
+## Próximos passos recomendados
+
+1. Implementar backend (auth + portfolio + sync jobs).
+2. Integrar provedor de dados de mercado e eventos corporativos.
+3. Evoluir conciliação automática e trilha de auditoria.
+4. Adicionar módulo tributário (IR) e relatórios avançados.
 
EOF
)
