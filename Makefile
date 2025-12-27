PYTHON := python

run:
	$(PYTHON) -c "from app.main import create_app; app = create_app(); app.run(debug=True)"

test:
	$(PYTHON) -m pytest -v
