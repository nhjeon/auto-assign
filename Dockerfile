FROM python:3.10-slim


COPY . /
RUN chmod +x main.sh

ENTRYPOINT [ "main.sh" ]