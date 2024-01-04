install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv

format:
	black  *.py spcalc/*.py tests/*.py

lint:
	pylint --disable=R,C *.py spcalc/*.py tests/*.py

all: install lint format test