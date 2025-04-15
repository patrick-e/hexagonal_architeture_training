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
│─/app
├── core
│   ├── entities       # Entidades do domínio (Developer, Company, Job)
│   ├── services       # Casos de uso e regras de negócio
│   ├── repository     # Interfaces (ex.: IDeveloperRepository)
│   └── exceptions     # Exceções específicas do domínio
├── adapters
│   ├── repositories   # Implementações concretas (ex.: SQLAlchemyRepository)
│   ├── aws            # Integrações com AWS (ex.: S3, SNS)
│   └── notifications  # Implementações de notificações (ex.: Celery)
├── api
│   ├── routes         # Endpoints FastAPI
│   ├── schemas        # Schemas Pydantic para entrada/saída
│   └── dependencies   # Dependências injetadas (ex.: repositórios)
├── infra
│   ├── database.py    # Configuração do banco de dados
│   ├── celery.py      # Configuração do Celery
│   └── settings.py    # Configurações gerais (ex.: leitura do .env)
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

## LocalStack - Simulação de AWS Localmente

O LocalStack é usado para simular serviços da AWS localmente, como S3, SNS, Lambda, entre outros. Ele é configurado no `docker-compose.yml` e pode ser acessado no endpoint `http://127.0.0.1:4566`.

### 1. Instalar o AWS CLI
Caso ainda não tenha o AWS CLI instalado, use o seguinte comando:
```bash
sudo snap install aws-cli --classic
```

## configuração do aws-cli para o projeto
```bash
aws configure
```

- **Access Key ID**: `test` (padrão do LocalStack)
- **Secret Access Key**: `test` (padrão do LocalStack)
- **Default region**: `us-east-1` (ou a região que você configurou no `docker-compose.yml`)
- **Output format**: `json`

---

### **4. Teste a Conexão com o LocalStack**
O LocalStack usa o endpoint `http://127.0.0.1:4566` para todos os serviços simulados. Sempre que usar o AWS CLI, adicione o parâmetro `--endpoint-url` para apontar para o LocalStack.

#### **Exemplo: Criar um bucket no S3**
```bash
aws --endpoint-url=http://127.0.0.1:4566 s3 mb s3://meu-bucket
```
## Exemplo de uso no terminal
Para utilizar o codigo via terminal:
```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"name": "joseph", "skills": ["python"]}' \
http://localhost:8000/api/v1/developers```
## Licença  
Este projeto está sob a licença MIT.  