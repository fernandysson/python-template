.PHONY: pre-commit
pre-commit: .git/hooks/pre-commit
	@echo "Running pre-commit hooks..."
	uv run pre-commit run --all-files

.git/hooks/pre-commit:
	@echo "Installing pre-commit hooks..."
	uv run pre-commit install

test:
	@echo "Running tests..."
	uv run pytest

check:
	@echo "Running type checks..."
	uv run mypy

help:
	@echo "Available commands:"
	@echo "  make pre-commit  - Install and run pre-commit hooks"
	@echo "  make help        - Show this help message"
	@echo "  make test        - Run tests"
	@echo "  make check       - Check code with mypy and flake8"
