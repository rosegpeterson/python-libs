.PHONY: doc

doc:
	mkdir -p doc
	pydoc -w ./test_array_v1.py
	mv ./test_array_v1.html ./doc
