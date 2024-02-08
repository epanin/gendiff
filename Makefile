test-json:
	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json
test-yaml:
	poetry run gendiff tests/fixtures/yaml1.yml tests/fixtures/yaml2.yml
check:
	poetry run pytest
install:
	poetry install
lint:
	poetry run flake8 gendiff
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
