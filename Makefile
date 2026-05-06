COMPOSE=docker-compose -f docker-compose.yml

up-localstack:
	$(COMPOSE) up -d

down-localstack:
	$(COMPOSE) down

tf-init:
	terraform -chdir=terraform init

tf-apply:
	terraform -chdir=terraform apply -auto-approve

tf-destroy:
	terraform -chdir=terraform destroy -auto-approve

run-app:
	pip install -r app/requirements.txt && python app/app.py

test:
	python tests/smoke_test.py

.PHONY: up-localstack down-localstack tf-init tf-apply tf-destroy run-app test
