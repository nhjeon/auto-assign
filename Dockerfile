FROM python:3.10-slim


COPY . /app
WORKDIR /app

RUN chmod +x app/main.sh

ENTRYPOINT [ "main.sh" ]