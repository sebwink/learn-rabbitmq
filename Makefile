COMPOSE=docker/compose

RABBITMQ_BASE=-f $(COMPOSE)/rabbitmq.base.yml
RABBITMQ_DEV=$(RABBITMQ_BASE) -f $(COMPOSE)/rabbitmq.dev.yml

PYP_BASE=-f $(COMPOSE)/pyp.base.yml 
PYP_DEV=$(PYP_BASE) -f $(COMPOSE)/pyp.dev.yml

PYC_BASE=-f $(COMPOSE)/pyc.base.yml 
PYC_DEV=$(PYC_BASE) -f $(COMPOSE)/pyc.dev.yml

SERVICES=$(RABBITMQ_DEV) $(PYP_DEV) $(PYC_DEV)

all: pyp pyc

up:
	docker-compose $(SERVICES) up

down: 
	docker-compose $(SERVICES) down 

python-producer: network
	docker-compose $(PYP_BASE) build $@

python-consumer: network
	docker-compose $(PYC_BASE) build $@

network:
	echo "Network"
