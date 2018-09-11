# Django 2.0 - Aprendendo os conceitos fundamentais

### [Link do Curso - Udemy](https://www.udemy.com/django-20-aprendendo-os-conceitos-fundamentais/)

#### Criação do ambiente virtual e instalação do django
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

#### Iniciando projeto no django
    django-admin startproject controle_gastos .
    
#### Estrutura do projeto criado

    controle-gastos
    |   __init__.py
    |   settings.py
    |   urls.py
    |___wasgi.py
    manage.py

#### Criando primeira app
    python manage.py startapp contas
    
* Após criar a app, será necessario registrar a aplicação 
no settings da aplicação principal

#### Criação do banco de dados
    python manage.py migrate
    
#### Rodar a aplicação
    python manage.py runserver
    
#### Criar superusuario
    python manage.py createsuperuser
    
## URL's
    * O processo para chegar em uma view começa pela url... 
    
## Views
    *

   
    


