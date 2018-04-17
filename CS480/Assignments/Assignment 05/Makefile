.PHONY: run

all: deliverable
code: Code/*
	cd Code && $(MAKE) all
codetest: code
	cd Code && $(MAKE) clean
run:
	cd Code && $(MAKE) run
uml: UML/*
	cd UML && $(MAKE) all
	cd UML && $(MAKE) clean
deliverable: uml codetest
	zip -r VideoStore-imp Code VideoStore-UML.pdf
clean:
	cd Code && $(MAKE) clean
	cd UML && $(MAKE) clean
	rm -f VideoStore-UML.pdf
	rm -f VideoStore-imp.zip
