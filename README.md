# 🎓 Portal do Aluno - UniFECAF

> Dashboard acadêmico e financeiro completo desenvolvido como solução para o desafio técnico de **Desenvolvedor Fullstack Pleno**.

[![TypeScript](https://img.shields.io/badge/TypeScript-5.0-blue)](https://www.typescriptlang.org/)
[![Next.js](https://img.shields.io/badge/Next.js-16-black)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.128-green)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue)](https://www.docker.com/)

---

## 🚀 Tecnologias

### Frontend
- **Next.js 16** com TypeScript
- **React 19** (Server/Client Components)
- **Tailwind CSS 4** (Mobile-First)
- **Framer Motion** para animações
- **Service Worker** para cache offline
- **Error Boundary** para tratamento de erros
- Tipagem completa com interfaces TypeScript

### Backend
- **FastAPI** (Python 3.12+)
- **Pydantic** para validação de schemas
- **JWT** para autenticação
- **SlowAPI** para rate limiting
- **CORS** configurado
- **Pytest** para testes unitários

### Infraestrutura
- **Docker** e **Docker Compose**
- **GitHub Actions** para CI/CD
- Hot-reload em desenvolvimento

---

## 📦 Como Rodar

### Pré-requisitos

- [Docker](https://www.docker.com/get-started) e Docker Compose **OU**
- [Node.js 20+](https://nodejs.org/) + [Python 3.12+](https://www.python.org/)

### Opção 1: Docker (Recomendado) 🐳

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/unifecaf-portal-aluno.git
cd unifecaf-portal-aluno

# Suba os containers
docker-compose up --build

# Acesse http://localhost:3000
```

**Pronto!** Backend rodando em `http://localhost:8000` e Frontend em `http://localhost:3000`

### Opção 2: Manual (Desenvolvimento) 💻

#### 1. Backend (Terminal 1)
```bash
cd backend
pip install -r requirements.txt    # ou: py -m pip install -r requirements.txt
uvicorn app.main:app --reload      # ou: py -m uvicorn app.main:app --reload
```

Backend disponível em: **http://localhost:8000**

#### 2. Frontend (Terminal 2)
```bash
cd frontend
npm install
npm run dev
```

Frontend disponível em: **http://localhost:3000**

### 🎯 Fluxo de Uso

1. Acesse `http://localhost:3000` → Redirecionado para `/login`
2. Credenciais já preenchidas (demo) → Clique em **"Entrar"**
3. Dashboard completo com todos os dados mockados

---

## 🧪 Testes

### Backend (Pytest)
```bash
cd backend
pip install -r requirements.txt    # ou: py -m pip install -r requirements.txt
pytest -v                          # ou: py -m pytest -v

# Cobertura:
# ✓ Health check endpoint
# ✓ Login com JWT
# ✓ Dashboard sem token (403)
# ✓ Dashboard com token válido
# ✓ Validação completa da estrutura de dados
```

**Resultado esperado:** 6 testes passando ✅

### Frontend (TypeScript + Build)
```bash
cd frontend
npm install
npm run build  # Valida tipagem e build de produção
```

**Resultado esperado:** Build sem erros ✅

---

## 📂 Estrutura do Projeto

```
Desafio-uniFecaf/
│
├── backend/                        # FastAPI Backend
│   ├── app/
│   │   ├── core/                   # JWT, Segurança
│   │   ├── routes/                 # auth.py, dashboard.py
│   │   ├── schemas/                # Pydantic models
│   │   ├── services/               # Lógica de negócio
│   │   └── mock/                   # Dados mockados
│   ├── tests/                      # Testes Pytest
│   ├── requirements.txt
│   ├── pytest.ini
│   └── Dockerfile
│
├── frontend/                       # Next.js Frontend
│   ├── src/
│   │   ├── app/
│   │   │   ├── page.tsx            # Redirect para /login
│   │   │   ├── login/              # Tela de login
│   │   │   └── dashboard/          # Dashboard principal
│   │   ├── components/
│   │   │   ├── dashboard/          # StudentHeader, Cards, etc
│   │   │   ├── ui/                 # Card, Badge, ProgressBar
│   │   │   └── ErrorBoundary.tsx
│   │   ├── types/                  # Interfaces TypeScript
│   │   └── services/               # API client
│   ├── public/
│   │   ├── sw.js                   # Service Worker
│   │   └── register-sw.js
│   ├── package.json
│   └── Dockerfile
│
├── .github/workflows/
│   └── ci-cd.yml                   # GitHub Actions
│
├── docker-compose.yml
├── .gitignore
├── .env.example
└── README.md
```

---

## ✨ Funcionalidades Implementadas

### Dashboard Acadêmico & Financeiro
- ✅ **Header do Aluno**: Nome, RA, Curso e Barra de Progresso animada
- ✅ **Resumo de Notas**: Cards com média e % de faltas
- ✅ **Alerta de Faltas >20%**: Borda vermelha + badge visual
- ✅ **Widget Financeiro**: Valor, data de vencimento e status
- ✅ **Agenda do Dia**: Próxima aula com horário e sala
- ✅ **Central de Notificações**: Sininho com contador de não lidas
- ✅ **Ações Rápidas**: Declaração, Carteirinha, Histórico

### Aspectos Técnicos
- ✅ **Autenticação JWT**: Rota `/dashboard` protegida
- ✅ **Rate Limiting**: Login 5/min, Dashboard 10/min
- ✅ **Tipagem Completa**: Zero uso de `any`
- ✅ **Responsividade**: Mobile-First com Tailwind CSS
- ✅ **Componentização**: Reutilizável e isolada
- ✅ **Error Boundary**: Captura erros globalmente
- ✅ **Animações**: Transições suaves (Framer Motion)
- ✅ **Service Worker**: Cache offline básico
- ✅ **Testes**: 6 testes Pytest cobrindo API
- ✅ **CI/CD**: GitHub Actions pipeline

### Extras (Diferencial)
- ✅ Tela de login moderna com gradiente
- ✅ Loading states em todas as ações
- ✅ Health check endpoint `/health`
- ✅ OpenAPI Docs automático em `/docs`
- ✅ `.env.example` para configuração
- ✅ Documentação completa

---

## 📊 Resumo de Atendimento aos Requisitos

| Requisito | Status | Implementação |
|-----------|--------|---------------|
| **Stack Obrigatória** | ✅ | Next.js + TypeScript + FastAPI + Pydantic + Docker |
| **Header do Aluno** | ✅ | Nome, RA, Curso, Barra de Progresso |
| **Resumo de Notas** | ✅ | Cards com média e % faltas |
| **Alerta Faltas >20%** | ✅ | Borda vermelha + badge |
| **Widget Financeiro** | ✅ | Valor, data, status |
| **Agenda do Dia** | ✅ | Horário, matéria, sala |
| **Notificações** | ✅ | Sininho com contador |
| **Ações Rápidas** | ✅ | 3 botões funcionais |
| **JWT Protegido** | ✅ | Bearer token |
| **Docker Compose** | ✅ | One-command setup |
| **Mobile-First** | ✅ | Tailwind CSS responsivo |
| **README Completo** | ✅ | Este arquivo |

---

## 📡 Endpoints da API

- **GET** `/health` - Health check
- **POST** `/auth/login` - Autenticação (rate limit: 5/min)
- **GET** `/dashboard/` - Dados do dashboard (protegido, rate limit: 10/min)
- **GET** `/docs` - Swagger UI (documentação interativa)

---

## 🎨 Design Patterns

### Frontend
- **Separation of Concerns**: Componentes por responsabilidade
- **Atomic Design**: UI components reutilizáveis
- **TypeScript Strict**: Interfaces para tudo
- **Error Boundaries**: Captura de erros React

### Backend
- **MVC Pattern**: Routes → Services → Mock Data
- **Dependency Injection**: FastAPI dependencies
- **Schema Validation**: Pydantic models
- **Middleware**: CORS, Rate Limiting

---

## 🔐 Segurança

- JWT tokens com Bearer authentication
- CORS restrito a `localhost:3000`
- Rate limiting (SlowAPI)
- Validação de schemas (Pydantic)
- Error boundary para dados sensíveis

---

## 📱 Responsividade

- **Mobile First**: Design otimizado para mobile
- **Breakpoints**: sm (640px), md (768px), lg (1024px)
- **Grid Adaptável**: Layout reorganizado em telas menores
- **Touch-friendly**: Botões e áreas clicáveis adequados

---

## 🎯 Decisões Técnicas

### Por que Next.js?
- SSR/SSG out of the box
- App Router com React Server Components
- Otimização automática de imagens e fontes
- TypeScript integrado

### Por que Tailwind CSS?
- Desenvolvimento rápido
- Purge CSS automático (bundle menor)
- Utility-first (fácil manutenção)
- Responsividade intuitiva

### Por que FastAPI?
- Performance superior (Starlette + Uvicorn)
- Validação automática com Pydantic
- Documentação OpenAPI automática
- Type hints nativos (Python 3.12+)

### Por que componentização granular?
- Facilita testes unitários
- Reusabilidade em outras páginas
- Manutenção isolada
- Code splitting automático

---

## 📊 Regras de Negócio

- **Alerta de Faltas**: Disciplina com >20% de faltas recebe indicador visual vermelho
- **Status Financeiro**: Boletos pendentes têm destaque amarelo
- **Notificações**: Contador exibe apenas não lidas
- **Barra de Progresso**: Visual do percentual de conclusão do curso

---

## 🚀 Deploy

### Vercel (Frontend)
```bash
cd frontend
vercel --prod
```

### Railway/Render (Backend)
```bash
railway up
# ou
render deploy
```

### Docker Hub
```bash
docker-compose build
docker tag unifecaf_backend seu-usuario/unifecaf-backend
docker tag unifecaf_frontend seu-usuario/unifecaf-frontend
docker push seu-usuario/unifecaf-backend
docker push seu-usuario/unifecaf-frontend
```

---

## 🔮 Melhorias Futuras

- [ ] Testes E2E (Playwright)
- [ ] Banco de dados (PostgreSQL)
- [ ] Refresh tokens
- [ ] Dark mode
- [ ] Internacionalização (i18n)
- [ ] PWA completo (manifest.json)
- [ ] Upload de arquivos (declarações, comprovantes)
- [ ] WebSockets para notificações em tempo real
- [ ] Integração com sistemas acadêmicos reais

---

## 👨‍💻 Autor

Desenvolvido para o case técnico da **UniFECAF** - Vaga de Desenvolvedor Fullstack Pleno.

**Stack:** Next.js 16 + TypeScript + Tailwind CSS + FastAPI + Docker

**Diferenciais:** Animações, Error Boundary, Service Worker, Rate Limiting, Testes, CI/CD

---

## 📝 Licença

MIT License - Livre para uso e referência.

## 🤝 Contribuições

Pull requests são bem-vindos! Abra uma issue para mudanças maiores.

---

**Desenvolvido com ❤️ para UniFECAF** | 2026
