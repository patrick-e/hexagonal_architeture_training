Aqui está o **README.md** sem emojis e com um tom mais sério:  

```markdown
# DevMatch - Plataforma de Conexão entre Empresas e Desenvolvedores  

DevMatch é uma plataforma que conecta empresas e desenvolvedores com base em suas habilidades e experiência. O projeto segue a Arquitetura Hexagonal para garantir desacoplamento e flexibilidade.  

## Tecnologias Utilizadas  
- FastAPI (Framework web assíncrono)  
- Pydantic (Validação de dados)  
- SQLAlchemy + Alembic (Banco de dados PostgreSQL)  
- Passlib + bcrypt (Autenticação segura)  
- Python-dotenv (Gerenciamento de variáveis de ambiente)  
- HTTPX (Testes e chamadas HTTP assíncronas)  
- Celery + Redis (Fila de tarefas para notificações)  
- LocalStack (Simulação de AWS localmente)  

## Estrutura do Projeto  
```bash
/meu_projeto
│── /app
│   ├── /core          # Domínio e casos de uso
│   │   ├── entities   # Entidades (Developer, Company, Job)
│   │   ├── services   # Regras de negócio (Match de devs e vagas)
│   │   ├── repository # Interface de acesso a dados (ABC)
│   ├── /adapters      # Implementações concretas (SQLAlchemy, AWS)
│   ├── /api           # FastAPI Endpoints
│   ├── /infra         # Configuração (Banco, Celery, Redis)
│── .env               # Variáveis sensíveis (.gitignore recomendado)
│── docker-compose.yml # Configuração para rodar localmente
│── requirements.txt   # Dependências do projeto
```

## Como Rodar o Projeto  

### 1. Configurar o ambiente  
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

### 2. Configurar variáveis de ambiente  
Crie um arquivo `.env` na raiz do projeto com as configurações necessárias:  
```ini
DATABASE_URL=postgresql://usuario:senha@localhost:5432/devmatch
SECRET_KEY=sua_chave_secreta
REDIS_URL=redis://localhost:6379/0
```

### 3. Rodar o banco de dados e serviços auxiliares  
```bash
docker-compose up -d
```

### 4. Aplicar migrações do banco de dados  
```bash
alembic upgrade head
```

### 5. Iniciar a API  
```bash
uvicorn app.api.main:app --host 0.0.0.0 --port 8000 --reload
```

A API estará disponível em `http://localhost:8000`.

## Testes  
Para rodar os testes automatizados:  
```bash
pytest
```

## Licença  
Este projeto está sob a licença MIT.  
```

Agora o README está direto ao ponto, bem estruturado e sem emojis. Alguma outra coisa que gostaria de ajustar?