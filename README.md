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
   * O processo para chegar em uma view começa pela url. As url's são definidas no 
   arquivo <em>urls.py</em> do projeto principal
    
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


## Operações no Banco de Dados [Documentação](https://docs.djangoproject.com/en/2.1/topics/db/queries/)
Uma vez criados os modelos de dados, o Django automaticamente fornece uma API de abstração 
de banco de dados que permite criar, recuperar, atualizar e excluir objetos.
A Manager é a interface através da qual as operações de consulta do banco de dados são fornecidas 
aos modelos do Django. Pelo menos um Managerexiste para cada modelo em um aplicativo Django.

#### ModelForm

 * Criar arquivo chamado <em>form.py</em>.
 
A classe criada para o formulario herdara de ModelForm, que terá a classe Meta que recebe
um model(Do qual será criado o formulario). A Form classe gerada terá um campo de formulário 
para cada campo de modelo especificado, na ordem especificada no atributo field.


    
    


   
  


