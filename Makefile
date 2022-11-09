install:
	poetry install

check:
	poetry run pytest

build: 
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest -vv --cov

test-coverage:
	poetry run pytest --cov-report=xml --cov=tests/
