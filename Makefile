.SILENT:

setup:
	@echo "== Setup environment =="
	poetry config virtualenvs.in-project true && poetry install

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

start:
	@echo "== Start DB and API =="
	docker compose up -d db api

stop:
	@echo "== Stop all =="
	docker compose down

test:
	@echo "== Run tests =="
	docker compose up -d db-test
	docker compose up test

dbclient:
	docker compose exec db bash -c "psql -U docker pj_mdpi"
