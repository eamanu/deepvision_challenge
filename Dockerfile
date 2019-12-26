FROM tiangolo/uwsgi-nginx-flask:python3.7

ENV LISTEN_PORT 8080

EXPOSE 8080

COPY .  /app

WORKDIR /app/

RUN pip --no-cache-dir install -r requirements.txt
