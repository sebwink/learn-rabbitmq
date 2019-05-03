FROM debian:stretch-slim as waitforit

RUN apt-get update \
    && apt-get upgrade -y \
	&& apt-get install -y git \
	&& git clone https://github.com/sebwink/wait-for-it

FROM python:3.6-slim

COPY --from=waitforit /wait-for-it/wait-for-it.sh /usr/bin/wait-for-it.sh 

RUN apt-get update \
    && apt-get upgrade -y \	
    && python3 -m pip install pika \
	&& mkdir /app

WORKDIR /app

COPY src .

CMD ["wait-for-it.sh", "--timeout=0", "rabbitmq:5672", "--", "python3", "src/main.py"]
