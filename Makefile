PYCACHES :=	$(shell find . | grep -v .venv | grep __pycache__ )

lint:
	pylint app

clean:
	rm -rf $(PYCACHES)

all: 
	make clean
	make lint

# run all tests
tests:
	pytest test

# run unit tests
test-unit:
	pytest test/unit

# run integration tests
test-int:
	pytest test/integration

# run the app locally
run run.local:
	python driver.py
