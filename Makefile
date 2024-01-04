install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv

format:
	black  *.py src/*.py

lint:
	pylint --disable=R,C *.py src/*.py

all: install lint test format