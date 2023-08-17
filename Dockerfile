FROM python:3.10-slim


COPY . /

ENTRYPOINT [ "main.sh" ]