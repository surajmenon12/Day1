.PHONY: run test lint clean

run:
	python src/app.py

test:
	python -m pytest tests/ -v

lint:
	black --check src/ tests/

format:
	black src/ tests/

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
