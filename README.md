# Projeto Contas a pagar e receber

Bem-vindo ao Projeto Contas a pagar e receber! Este é um projeto simples com uso do Fastapi.

## Descrição

O Projeto tem a finalidade de demostrar como utilizar o Fastapi para construção de Apis Rest rapidamente.

## Banco de Dados Postgres com Docker

## CRIAR CONTAINER DB
docker run --name db_fastapi -p 5432:5432 -d -e POSTGRES_DB=my_postgres -e POSTGRES_USER=falcao -e POSTGRES_PASSWORD=f1616 postgres

## CRIAR CONTAINER PGADMIN
docker run -p 8080:80 -e 'PGADMIN_DEFAULT_EMAIL=tiagofalcaoshow12@gmail.com' -e 'PGADMIN_DEFAULT_PASSWORD=falcao' -d dpage/pgadmin4
