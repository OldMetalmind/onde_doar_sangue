# Onde Dar Sangue

Recolha de informação onde doar sangue e torna-la de forma mais acessível

Fonte: [http://dador.pt/onde-dar/lista-de-recolhas](http://dador.pt/onde-dar/lista-de-recolhas)

## Executar o projecto localmente

1. `poetry build`
2. `pip install dist/<latest_version_built>`
3. `waitress-server --call 'onde_dar_sangue:start_app'`

## Docker

build: `docker build -t onde_dar_sangue --build-arg YOUR_ENV=production`
run: `docker run -p 8080:8080 onde_dar_sangue`

## Endpoint

`/l`:
Retorna JSON de todas as intervenções actuais
