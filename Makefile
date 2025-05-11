run:
	python3 -m app.main

format:
	isort .
	ruff format .
