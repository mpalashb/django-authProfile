FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /app_auth

COPY ./g_auth /app_auth/

COPY requirements.txt /app_auth/

RUN pip3 install -r requirements.txt

EXPOSE 8080