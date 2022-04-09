
run-dev:
	uvicorn app.main:app --reload

env:
	python3 -m venv venv2 --prompt comclass; \
	. venv/bin/activate.fish

install:
	pip install --upgrade pip
	pip install -r app/requirements.txt

install-dev:
	pip install --upgrade pip
	pip install -r requirements-dev.txt

check-fmt:
	python -m black app/ client/ --diff --color

fix-fmt:
	python -m black app/ client/

mypy:
	python -m mypy --explicit-package-bases --namespace-packages app/ client/

mypy-strict:
	python -m mypy --strict app/ client/

