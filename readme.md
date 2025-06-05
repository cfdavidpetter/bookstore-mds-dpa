# Projet Bookstore - Murabei - David Petter

## Estrutura do Projeto

```
bookstore-mds-dpa/
├── backend/
│   ├── src/                # Código fonte
│   │   ├── domain/         # Entidades e regras de negócio
│   │   ├── endpoints/      # Rotas da API
│   │   ├── services/       # Lógica de negócio
│   │   ├── datalayer/      # Acesso a dados
│   │   │   ├── interfaces/          # Contratos dos repositórios
│   │   │   ├── repositories/        # Os repositórios podem ser escalados para outros 
│   │   │   │   │                      tipos de armazenamento com PostgreSQL e MySQL ou NoSQL 
│   │   │   │   │                      porque o domínio é completamente independente do repositório 
│   │   │   │   ├── sqlite/          # Implementação SQLite
│   │   │   └── base.py              # Classes base para repositórios
│   │   ├── factories/      # Construção e ligação de dependências
│   │   └── utils/          # Funções utilitárias
│   ├── tests/              # Testes unitários
│   ├── app.py              # Ponto de entrada da aplicação
│
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   │   ├── books/      # Páginas relacionadas a livros
│   │   │   ├── authors/    # Páginas relacionadas a autores
│   │   │   └── layout.tsx  # Layout principal
│   │   ├── core/
│   │   │   ├── services/   # Serviços de comunicação com a API
│   │   │   ├── models/     # Definições de entidades
│   │   ├── hooks/          # Custom React hooks
│   │   └── shared/         # Componentes e utilitários compartilhados
│   │       ├── components/
│   │       │   ├── ui/              # Componentes de interface básicos (shadcn/ui)
│   │       │   ├── navigation/      # Componentes de navegação
│   │       │   ├── sidebar/         # Barra lateral
│   │       │   ├── table-view/      # Visualização em tabela
│   │       │   ├── pagination-view/ # Componentes de paginação
│   │       │   └── filter-view/     # Componentes de filtro
│   │       └── lib/                 # Utilitários e helpers
│   ├── cypress/            # Config. para os testes end-to-end (componentes)
│
└── _docker-compose/        # Configuração do ambiente Docker
```

## Instruções para Desenvolvimento

### Pré-requisitos
- Docker e Docker Compose instalados

### Configuração do Ambiente de Desenvolvimento

1. Clone o repositório:
```bash
git clone https://github.com/cfdavidpetter/bookstore-mds-dpa
cd bookstore-mds-dpa
```

2. Inicie os containers Docker:
```bash
cd _docker-compose
./docker-up.bash
```

### Acessando a Aplicação
- Frontend: http://localhost:7720
- Backend: http://localhost:7721


### Observações
- Certifique-se de que as portas 7720 e 7721 estejam disponíveis
- Em caso de problemas com permissões, pode ser necessário usar `sudo` nos comandos Docker
