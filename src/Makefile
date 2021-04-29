PYTHON=python3
TMPPACK=../../xkozak18_xkovac61_xhezel00

.PHONY: all pack clean test doc run profile profiling-remove-inputs remove-pycache remove-tmp-pack make-installer clean-installer setup

all:
	@echo "Python project doesn't need to be compiled."

pack: clean setup doc make-installer
	@mkdir -p $(TMPPACK)
	@mkdir -p $(TMPPACK)/repo
	@mkdir -p $(TMPPACK)/install
	@mkdir -p $(TMPPACK)/doc
	@cp ../installer/pycalc_1.0_amd64.deb $(TMPPACK)/install
	make clean-installer
	@cp -r .. $(TMPPACK)/repo
	@rm -f $(TMPPACK)/repo/src/pycalc_1.0_amd64.deb
	@cp -r html $(TMPPACK)/doc
	@rm -rf $(TMPPACK)/repo/src/html
	@cd ../../ && zip -r xkozak18_xkovac61_xhezel00.zip xkozak18_xkovac61_xhezel00
	make clean

clean: profiling-remove-inputs remove-pycache remove-tmp-pack clean-installer
	rm -rf html

test:
	@$(PYTHON) test_mathlib.py

doc:
	doxygen

run:
	@$(PYTHON) calculator.py

profile:
	@cd ../profiling && $(PYTHON) generate_inputs.py
	@$(PYTHON) profiling.py < ../profiling/input/inputs1000.txt

profiling-remove-inputs:
	@if [ -d ../profiling/input ]; then cd ../profiling/ && rm -rf input; fi

remove-pycache:
	@if [ -d __pycache__ ]; then rm -rf __pycache__; fi

remove-tmp-pack:
	@if [ -d $(TMPPACK) ]; then rm -rf $(TMPPACK); fi

make-installer: clean
	mkdir -p ../installer/pycalc-1.0
	cp calculator.py ../installer/pycalc-1.0
	cp main.qml ../installer/pycalc-1.0
	cp help.qml ../installer/pycalc-1.0
	cp about.qml ../installer/pycalc-1.0
	cp mathlib.py ../installer/pycalc-1.0
	cp ../installer/Makefile ../installer/pycalc-1.0
	cp -r ../installer/install ../installer/pycalc-1.0
	cd ../installer/pycalc-1.0 && zip -r pycalc-1.0.tar.gz *
	cp ../installer/pycalc-1.0/pycalc-1.0.tar.gz ../installer
	rm -f ../installer/pycalc-1.0/pycalc-1.0.tar.gz
	cd ../installer/pycalc-1.0 && dh_make -e "xhezel00@stud.fit.vutbr.cz" -c gpl -n -s -y -f ../pycalc-1.0.tar.gz
	rm -f ../installer/pycalc-1.0/debian/control
	cp ../installer/sources/* ../installer/pycalc-1.0/debian
	cd ../installer/pycalc-1.0 && dpkg-buildpackage -rfakeroot -uc -b

clean-installer:
	rm -rf ../installer/pycalc-1.0*
	rm -rf ../installer/pycalc_1.0*

setup:
	sudo apt-get install python3-pip
	pip3 install -r requirements.txt
	sudo apt-get install dh-make
