all: SeqDiag.png ClassDiag.png
	latexmk -pdf Document.tex
	mv Document.pdf ../VideoStore-UML.pdf
SeqDiag.png: SeqDiag.wsd
	plantuml -tpng SeqDiag.wsd
ClassDiag.png: ClassDiag.wsd 
	plantuml -tpng ClassDiag.wsd
clean:
	rm -f $(wildcard *.png)
	rm -f Document.aux
	rm -f Document.fdb_latexmk
	rm -f Document.fls
	rm -f Document.log