.SILENT:

setup:
	@echo "== Setup environment =="
	poetry config virtualenvs.in-project true && poetry install

rebuild:
	@echo "== Rebuild image =="
	docker compose build --no-cache

format:
	@echo "== Format code =="
	poetry run python -m ruff format src

check:
	@echo "== Check code =="
	poetry run python -m ruff check src

start:
	@echo "== Start  =="
	docker compose up -d

stop:
	@echo "== Stop =="
	docker compose down

