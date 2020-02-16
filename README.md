# Onde Doar Sangue 💉

Recolha de informação onde doar sangue e torná-la mais acessível ao público.

## O que é? 🧐

Esta é uma API feita com base no site [dador.pt](http://dador.pt/onde-dar/lista-de-recolhas).
Com a sua ajuda, podemos obter informação de todos os locais onde é possível doar sangue em Portugal, para uma causa maior.
Porque não experimentar?

## Dependências 📝

- **Instalar [o python poetry](https://python-poetry.org/)**

#### Executar o projecto localmente

1. `poetry install`
2. `poetry build`
3. `pip install dist/<latest_version_built>`
4. `poetry run waitress-server --call 'onde_dar_sangue:start_app'`

#### Docker

build: `docker build -t onde_dar_sangue .`

run: `docker run -p 8080:8080 onde_dar_sangue`

#### Endpoint (routes)

`GET /l`: Retorna JSON de todas as intervenções actuais
