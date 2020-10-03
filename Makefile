VERSION?=minor

install:
	poetry install

format:
	isort --recursive --quiet bin src tests migrations
	black bin src tests migrations

lint:
	isort --recursive --quiet --check --diff bin src tests migrations || exit 1
	flake8 bin src tests || exit 1
	pydocstyle bin src tests || exit 1
	mypy src || exit 1
	bandit -r src || exit 1
	black --check --diff bin src tests migrations || exit 1

bump:
	poetry version $(VERSION)