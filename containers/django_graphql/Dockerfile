FROM python:3.12-slim

RUN apt-get update

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

ADD app.tar.gz /app

EXPOSE 8000

ENV DEBUG=True
ENV SECRET_KEY=development

USER nonroot

CMD [ "python", "manage.py", "runserver"]
