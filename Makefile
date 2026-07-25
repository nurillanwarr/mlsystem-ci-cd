install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py MLProject/*.py

lint:
	pylint --disable=R,C --fail-under=5 *.py MLProject/*.py

test:
	pytest test_modelling.py -v

all: install format lint test
