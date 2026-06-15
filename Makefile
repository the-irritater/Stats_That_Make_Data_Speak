.PHONY: setup test lint format run-dashboard clean

PYTHON = python3
VENV = .venv
BIN = $(VENV)/bin

setup:
	@echo "Creating virtual environment..."
	$(PYTHON) -m venv $(VENV)
	@echo "Installing package managers & dependencies..."
	$(BIN)/pip install --upgrade pip
	$(BIN)/pip install poetry
	$(BIN)/poetry install
	@echo "Installing dev/dashboard dependencies..."
	$(BIN)/pip install -r requirements-dev.txt -r requirements-dashboard.txt
	@echo "Setup complete. Source the environment with: source .venv/bin/activate"


test:
	$(BIN)/pytest --cov=stats_series --cov-fail-under=85 --cov-report=term-missing tests/

lint:
	$(BIN)/flake8 src/ tests/ dashboard/
	$(BIN)/black --check src/ tests/ dashboard/
	$(BIN)/isort --check-only src/ tests/ dashboard/

format:
	$(BIN)/black src/ tests/ dashboard/
	$(BIN)/isort src/ tests/ dashboard/

run-dashboard:
	$(BIN)/streamlit run dashboard/interactive_dashboard.py

generate-data:
	$(BIN)/python -m stats_series.precompute_aggregations

run-notebooks:
	$(BIN)/jupyter nbconvert --to notebook --execute applied/notebooks/*.ipynb --inplace
	$(BIN)/jupyter nbconvert --to notebook --execute applied/case-studies/**/*.ipynb --inplace
	$(BIN)/jupyter nbconvert --to notebook --execute applied/signature-project/notebooks/*.ipynb --inplace


clean:
	@echo "Cleaning temporary execution artifacts..."
	rm -rf .pytest_cache .coverage htmlcov .black-cache .isort_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
