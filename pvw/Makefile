BINDIR := /usr/bin

.PHONY: all

all:
	pip install pyinstaller termcolor
	$${HOME}/.local/bin/pyinstaller --onefile main.py --distpath . --clean -n pvw_py

install:
	mkdir -p ${DESTDIR}${BINDIR}
	cp pvw.sh pvw
	cp pvw pvw_py ${DESTDIR}${BINDIR}/
	rm pvw pvw_py pvw_py.spec
