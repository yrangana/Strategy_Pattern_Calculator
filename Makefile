install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv

format:
	black src/*.py

lint:
	pylint --disable=R,C src/*.py

all: install lint test format