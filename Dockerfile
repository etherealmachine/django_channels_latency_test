FROM python:3.4

# Force stdio/out/err to be unbuffered - we want to see errors pronto.
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY . .

RUN pip install django
RUN pip install channels
RUN pip install psycopg2
RUN pip install asgi_redis
RUN pip install Twisted[tls,http2]
RUN pip install txredisapi