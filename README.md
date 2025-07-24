# Professor Hub

**Professor Hub** é uma plataforma web desenvolvida com Django que visa auxiliar professores no planejamento e organização de suas atividades acadêmicas.

A aplicação oferece uma interface intuitiva com navegação lateral, permitindo o gerenciamento fácil de disciplinas, tarefas, avaliações, planos de aula e calendários escolares.

## Tecnologias Utilizadas
- Django
- Bootstrap 5

## Funcionalidades
- Cadastro e login de usuários
- Registro de avaliações e tarefas
- Sidebar com navegação dinâmica
- Gerar aulas automaticamente
- Calendários por disciplina

## Instalação
- Clone o repositório:
    ```
    git clone https://github.com/hick-hpe/frontend-professorhub/
    ```

- Criar e ativar ambiente virtual:
    - Windows:
        ```
        python -m venv venv
        venv\Scripts\activate
        ```
    - Linux/MacOS:
        ```
        python3 -m venv venv
        source venv/bin/activate
        ```

- Instalar dependências:
    ```
    pip install -r requirements.txt
    ```

- Acessar diretório de trabalho:
    ```
    cd professorhub
    ```
    
- Criar e aplicar as migrações:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

- Rodar servidor:
    ```
    python manage.py runserver
    ```

## Servidor
- O servidor Django estará disponível em [http://localhost:8000/](http://localhost:8000/)
