test_with_doctest:
	python3 -m pytest --doctest-modules --ignore=setup.py -v ./
	python2 -m pytest --doctest-modules --ignore=setup.py -v ./

test_no_doctest:
	python3 -m pytest  -v --ignore=setup.py ./
	python2 -m pytest  -v --ignore=setup.py ./

clean:
	find . -type d -name '__pycache__' | xargs -r rm -r
	find . -type d -name '.cache' | xargs -r rm -r

.PHONY : test_no_doctest test_with_doctest clean

