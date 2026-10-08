# Agenda de Contatos

Aplicação web desenvolvida em Django para gerenciamento de contatos.

O sistema permite pesquisar contatos cadastrados, visualizar seus detalhes e cadastrar novos registros através de uma interface web simples e intuitiva.

<img width="1395" height="839" alt="image" src="https://github.com/user-attachments/assets/83c2a80b-7397-4f56-aef0-437adb86182c" />
<br>
<br>
<img width="1421" height="792" alt="image" src="https://github.com/user-attachments/assets/f83c7b67-1a98-4e2d-9ac5-78c47c0e7595" />
<br>
<br>
<img width="1352" height="770" alt="image" src="https://github.com/user-attachments/assets/53e99a81-03aa-4d9a-b72f-be1e589ed56a" />



## Funcionalidades

- Pesquisa de contatos por nome
- Listagem de resultados encontrados
- Visualização detalhada de um contato
- Cadastro de novos contatos
- Administração dos registros pelo Django Admin

## Tecnologias Utilizadas

- Python 3.13.7
- Django
- SQLite (padrão do Django)
- HTML
- CSS

## Estrutura de Rotas

| Endpoint | Descrição |
|-----------|-----------|
| `/search/` | Pesquisa de contatos |
| `/contact/create/` | Cadastro de novo contato |
| `/admin/` | Painel administrativo do Django |

## Instalação

### 1. Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_PROJETO>
```

### 2. Criar ambiente virtual

#### Linux / Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instalar dependências

Atualize o pip:

```bash
python -m pip install --upgrade pip
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

### 4. Aplicar migrações

```bash
python manage.py migrate
```

### 5. Criar usuário administrador

```bash
python manage.py createsuperuser
```

Informe:

- Usuário
- E-mail
- Senha

### 6. Executar o servidor

```bash
python manage.py runserver
```

Acesse:

```text
http://127.0.0.1:8000/
```

## Utilização

### Buscar contatos

Acesse:

```text
http://127.0.0.1:8000/search/
```

Digite parte do nome de um contato para visualizar os resultados encontrados.

### Cadastrar contato

Acesse:

```text
http://127.0.0.1:8000/contact/create/
```

Preencha os campos obrigatórios e envie o formulário.

### Painel Administrativo

Acesse:

```text
http://127.0.0.1:8000/admin/
```

Entre com o usuário criado através do comando:

```bash
python manage.py createsuperuser
```

## Modelo de Contato

Os contatos podem possuir informações como:

- Nome
- Sobrenome
- Telefone
- E-mail
- Data de criação
- Categoria
- Descrição

## Licença

Projeto desenvolvido para fins de estudo e prática com Django.
