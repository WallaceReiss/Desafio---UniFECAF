# Comandos para subir o projeto no GitHub

## 1. Inicializar repositório (se ainda não foi feito)
```bash
cd E:\walla\Documents\Desafio-uniFecaf
git init
```

## 2. Adicionar todos os arquivos
```bash
git add .
```

## 3. Fazer o primeiro commit
```bash
git commit -m "feat: Portal do Aluno UniFECAF - Desafio Fullstack Pleno

- Frontend: Next.js 16 + TypeScript + Tailwind + Framer Motion
- Backend: FastAPI + Pydantic + JWT + Rate Limiting
- Testes: Pytest com 6 testes cobrindo toda API
- Docker: docker-compose.yml funcional
- CI/CD: GitHub Actions pipeline
- Features extras: Animações, Error Boundary, Service Worker
- Tela de login moderna com gradiente
- Dashboard completo com responsividade mobile-first
"
```

## 4. Criar repositório no GitHub
Acesse: https://github.com/new

Nome sugerido: `unifecaf-portal-aluno`
Descrição: `Dashboard acadêmico e financeiro - Desafio Técnico Fullstack Pleno`

## 5. Adicionar remote e fazer push
```bash
# Substitua SEU-USUARIO pelo seu username do GitHub
git remote add origin https://github.com/SEU-USUARIO/unifecaf-portal-aluno.git
git branch -M main
git push -u origin main
```

## 6. (Opcional) Criar release/tag
```bash
git tag -a v1.0.0 -m "Release v1.0.0 - Portal do Aluno UniFECAF"
git push origin v1.0.0
```

## 7. Adicionar no README.md do GitHub
Edite diretamente no GitHub para adicionar:
- Screenshot do dashboard
- Link de demo (se fizer deploy)
- Seu nome e contato

## Comandos úteis depois do primeiro push:
```bash
# Fazer alterações
git add .
git commit -m "fix: descrição da correção"
git push

# Ver status
git status

# Ver histórico
git log --oneline
```
