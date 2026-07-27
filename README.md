# Library Manager

Library Manager é uma aplicação web desenvolvida com Flask para gerenciar uma biblioteca pessoal. O sistema permite que usuários cadastrem, editem, removam e avaliem livros, além de buscar informações automaticamente por ISBN utilizando a Open Library API.

## Funcionalidades

- Cadastro e autenticação de usuários
- Login seguro com Flask-Login e Flask-Bcrypt
- Cadastro, edição e exclusão de livros
- Busca automática de informações por ISBN
- Avaliação de livros de 1 a 5 estrelas
- Interface responsiva
- Execução com Docker

## Tecnologias

- Python
- Flask
- SQLAlchemy
- Flask-Login
- Flask-Bcrypt
- SQLite
- HTML
- CSS
- JavaScript
- Docker

## Estrutura do projeto

```text
library-manager/
├── app/
│   ├── auth/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── static/
│   └── templates/
├── config.py
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── run.py
└── README.md
```

## Como executar

Clone o repositório:

```bash
git clone https://github.com/eduardasaraujo/library-manager.git
```

Acesse a pasta do projeto:

```bash
cd library-manager
```

Crie e ative um ambiente virtual:

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
python run.py
```

A aplicação estará disponível em:

```text
http://localhost:5000
```

## Executando com Docker

Construa a imagem e inicie os containers:

```bash
docker-compose up --build
```

Depois acesse:

```text
http://localhost:5000
```
