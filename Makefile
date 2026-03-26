.PHONY: all lint format mypy test install format-check

lint:
	ruff check src/ tests/

format:
	ruff format src/ tests/

format-check:
	ruff format --check src/ tests/

mypy:
	mypy src/ tests/

test:
	pytest tests/

install:
	pip install -r requirements-dev.txt


all: lint format-check mypy test