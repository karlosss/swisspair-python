install:
	rm -rf build
	mkdir build
	git clone https://github.com/karlosss/Minimum-Cost-Perfect-Matching.git build/Minimum-Cost-Perfect-Matching
	git clone https://github.com/karlosss/gmpwrap.git build/gmpwrap
	git clone https://github.com/karlosss/swisspair.git build/swisspair
	git clone https://github.com/karlosss/swisspair-python-bindings.git build/bindings
	cd build/gmpwrap && cmake . && make
	cd build/Minimum-Cost-Perfect-Matching && cmake . && make
	cd build/swisspair && cmake . && make
	cd build/bindings && make
	cp build/bindings/swisspair*.so ../src