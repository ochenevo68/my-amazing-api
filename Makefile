.SILENT:

setup:
	@echo "== Setup environment =="
	poetry config virtualenvs.in-project true && poetry install
	poetry run pre-commit install

start:
	@echo "== Start DB and API =="
	docker compose up -d db api

stop:
	@echo "== Stop API and DB =="
	docker compose down api db

test:
	@echo "== Run tests =="
	docker compose up -d db-test
	docker compose up test
	docker compose down db-test

doc:
	@echo "== Generate doc =="
	ln -sf '../README.md' docs/usage.md
	poetry run python -m mkdocs build
	rm docs/usage.md

rebuild:
	@echo "== Rebuild image =="
	docker compose build --no-cache

format:
	@echo "== Format code =="
	poetry run python -m ruff format src tests

check:
	@echo "== Check code =="
	poetry run python -m ruff check src tests

check-fix:
	@echo "== Check code and fix =="
	poetry run python -m ruff check --select I --fix src tests

dbclient:
	docker compose exec db bash -c "psql -U docker pj_mdpi"
