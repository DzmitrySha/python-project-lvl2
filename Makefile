install: 
	poetry install

run-gendiff:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-uninstall:
	python3 -m pip uninstall --yes dist/*.whl

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest
