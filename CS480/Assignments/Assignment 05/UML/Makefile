all: UML
	latexmk -pdf Document.tex
	mv Document.pdf ../VideoStore-UML.pdf
UML: ClassDiag.wsd SeqDiag.wsd
	plantuml -tpng ClassDiag.wsd
	plantuml -tpng SeqDiag.wsd
clean:
	rm -f $(wildcard *.png)
	rm -f Document.aux
	rm -f Document.fdb_latexmk
	rm -f Document.fls
	rm -f Document.log