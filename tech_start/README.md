# TechStart - Olist Desafio

Este é um projeto desenvolvido para possibilitar a criação, edição, listagem e deleção dos seguintes dados:
 * Vendedores
 * Produtos
 * Categorias
 * Marketplaces

# Instruções de instalação (configuração);
Para instalar o projeto e rodar localmente basta:
* Clonar o projeto:

    ```
    git clone https://github.com/Monamello/TechStart_2Ed.git
    ```
* Criar e entrar em uma env:
    ```
    python3 -m venv env
    source env/bin/activate
    ```
* Rodar o requirements.txt:
    ```
    pip install -r requirements.txt
    ```
* Rodar as migrações:
    ```
    python manage.py migrate
    ```
* Rodar o projeto:
    ```
    python manage.py runserver
    ```

# Testes
Os testes estão separados conforme seu app correspondente, para cada app existe 
um conjunto de testes para verificar se os métodos POST, PUT, GET e DELETE de cada model estão
funcionando.

* Para rodar os testes basta:
    ```
    python manage.py test
    ```


# Ambiente de trabalho
## Tecnologias
Para o desenvolvimento deste projeto foi utilizado Python com Django e Django Rest Framework,
para a parte dos filtros do model produto foi utilizada uma biblioteca django-filter;

## Ferramentas
A IDE utilizada foi o VSCode, com a SO Ubuntu 20, apesar do Django fornecer uma boa interface para testar as rotas acabei usando também o PostMan.


## Interface Django
Não foi desenvolvida nenhuma interface para se conectar a API e testar as rotas pois acredito que a interface fornecida pelo próprio DRF é o bastante já auxilia neste caso.

## Rotas
Após rodar o projeto é possivel ver as rotas e navegar entre elas, mas para facilitar e caso seja de sua preferência consultar as rotas pelo PostMan ou Insomia aqui estão as rotas:

### Marketplaces:
* GET "/marketplaces/",
* POST "/marketplaces/id do marketplace/",
* PUT "/marketplaces/id do marketplace/",
* DELETE "/marketplaces/id do marketplace/",
```
{
    "name": "",
    "description": "",
    "site": "",
    "telephone": ,
    "email": "",
    "support_contact": ""
}
```

### Products:
* GET "/products/",
* GET "/products$name=nome do produto",
* GET "/products$name=nome do produto&description=descrição do produto&price=preço do     produto&categories=[ids das categorias relacionadas]"
* POST "/products/id do product/",
* PUT "/products/id do product/",
* DELETE "/products/id do product/",
```
{
    "name": "",
    "description": "",
    "price":,
    "categories": []
}
```

### Salesperson:
* GET "/salesperson/",
* POST "/salesperson/id do product/",
* PUT "/salesperson/id do product/",
* DELETE "/salesperson/id do product/",
```
{
    "name": "",
    "company_name": "",
    "cnpj": ,
    "email": "",
    "telephone": ,
    "address": {
        "street": "",
        "number": ,
        "neighborhood": "",
        "complement_address": ""
    }
}
```

### Categories:
* GET "/categories/"
* POST "/categories/id do category/"
* PUT "/categories/id do category/"
* DELETE "/categories/id do category/"
```
{
    "name": "",
    "description": ""
}
```