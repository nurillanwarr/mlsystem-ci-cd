install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py MLProject/*.py

lint:
	pylint --disable=R,C *.py MLProject/*.py

test:
	pytest test_modelling.py

all: install format lint test
