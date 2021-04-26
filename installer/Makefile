DESTDIR = $(HOME)
SHELL = /bin/bash

.PHONY: all clean install
all: dist/pycalc

dist/pycalc: calculator.py
	pyinstaller --add-data "main.qml:." --add-data "help.qml:." --add-data "about.qml:." --name="pycalc" --onedir --windowed --onefile calculator.py 

clean:
	echo $(DESTDIR)
	rm -rf ./build
	rm -rf ./dist
	rm -f pycalc.spec
	rm -rf ./__pycache__

install: dist/pycalc
	mkdir -p $(DESTDIR)/opt
	mkdir $(DESTDIR)/opt/pycalc
	cd dist; install -D pycalc --target-directory="$(DESTDIR)/opt/pycalc"
