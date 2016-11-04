all: reference.py reference.java

reference.py:
	find . -name "*.py" | grep -v reference.py | xargs tail -n +1 > reference.py

reference.java:
	find . -name "*.java" | grep -v reference.java | xargs tail -n +1 > reference.java

clean:
	rm -rf reference.py reference.java
