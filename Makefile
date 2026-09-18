PYTHON ?= python

install:
	$(PYTHON) -m pip install -e '.[dev]'

test:
	pytest -q

run:
	$(PYTHON) -m synergy_ai_committee.api

