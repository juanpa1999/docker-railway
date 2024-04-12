#!/bin/bash

docker compose up -d
docker compose run --rm back alembic upgrade head
docker compose run --rm back alembic revision --autogenerate

# docker destop:
# --> ejecuta (docker-compose)
# enfoque: para PC con capacidad media de hardware
# explicacion: descargar docker y despues docker compose, tenemos 2 opciones con docker compose, directamente desde la imagen de desktop windows installa docker compose y puede ser ejecutado con el comando docker-compose

# docker compose plugin:
# --> ejecuta (docker compose)
# enfoque: para PC con poca capacidad de hardware
# si no tienen docker desktop instalado deberan instalar docker compose plugin desde esta documentacion:
# https://docs.docker.com/compose/install/linux/