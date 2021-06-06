# MRBIT - API
EXCHANGE DE CRIPTOMOEDAS

## Features

- Gerenciamente de criptomoedas

- Cotação das criptomoedas em tempo real

- Operação de compra e venda de criptomoedas

## Caracteristicas

1. Banco de dados [Postgresql](https://www.postgresql.org/)

2. Consome informações da API da [CryptoCompare](https://min-api.cryptocompare.com/documentation) utilizando a lib [request](https://pypi.org/project/requests/)

3. A documentação da API foi feita com [Swagger](https://swagger.io/) utilizando a lib [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/)

4. Deploy foi feito no Heroku -> [acesse](mrbit.herokuapp.com)

## Ambiente

1. Instalar [**Docker**](https://docs.docker.com/engine/install/ubuntu/) e [**Docker Compose**](https://docs.docker.com/compose/install/)

2. Instalar **Python 3.7** na sua maquina local

3. Instalar o [**pipenv**](https://pypi.org/project/pipenv/) no Python global:

    `sudo install pipenv`

4. Na pasta raiz do projeto, rodar o comando:

    `pipenv sync`

    Ele irá criar automaticamente o *virtualenv* e instalar as dependencias do projeto.

5. Rodar o **docker-compose** com as dependências básicas

    `docker-compose up -d`

6. Ative o **virtualenv**

    `pipenv shell`

7. Para rodar, acesse a pasta `src` e execute o comando:

    `python src/manage.py runserver`

8. Acesse **localhost:8000** para visualizar a documentação da API no Swagger
