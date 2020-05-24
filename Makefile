PYCACHES :=	$(shell find . | grep -v .venv | grep __pycache__ )

lint:
	pylint app

clean:
	rm -rf $(PYCACHES)

all: 
	make clean
	make lint

run run.local:
	python driver.py
