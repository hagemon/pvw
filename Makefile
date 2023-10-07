BINDIR := /usr/bin

all:
	pyinstaller --onefile main.py --distpath . --clean -n pvw_py

install:
	mkdir -p ${DESTDIR}${BINDIR}
	cp pvw.sh pvw
	cp pvw pvw_py ${DESTDIR}${BINDIR}/
	rm pvw
