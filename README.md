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

## Templates
    * Deve ser criada uma pasta template dentro do projeto (app), que terá
    um pasta com o mesmo nome do projeto(assim evitará ambiguidade com os demais app's), onde dentro estará os templates utilizados
    pelo aplicativo.
   
## Models 
   * Irão representar as tabelas criadas no banco de dados, após implementados
   os models, será preciso rodar o comando <em>makemigrations</em> que irá verificar
   as modificações feitas nos models e criará um arquivo dentro da pasta migrations,
   com os comandos para o django criar as tabelas do BD, depois será preciso rodar o comando <em>migrate</em> 
   que criará as tabelas no banco de dados
    
    python manage.py mikemigrations
    
    python manage.py migrate
#### Documentação
[Dango Models](https://docs.djangoproject.com/en/2.0/topics/db/models/)

[Dango Model Fileds](https://www.udemy.com/django-20-aprendendo-os-conceitos-fundamentais/)

#### Registrando o modelo criado no Django Admin
   * Após a criação da tabela, será preciso registra-la para que possa ser usada pelo Django Admin
     no arquivo <em>admin.py</em> do app

    from .models import Categoria # Importando o model
    
    ...
    
    admin.site.register(Categoria) # Registrando





   
  


