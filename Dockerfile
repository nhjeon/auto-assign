FROM python:3.10-slim


COPY . .

CMD [ "python", "./main.py" ]