# Go to following webpage for more details.
# http://docs.cython.org/src/userguide/wrapping_CPlusPlus.html

cython --cplus -o vector.cpp vector.pyx
clang++ -shared -fPIC -I/usr/local/Cellar/python3/3.4.2_1/Frameworks/Python.framework/Versions/3.4/include/python3.4m/ -L/usr/local/Cellar/python3/3.4.2_1/Frameworks/Python.framework/Versions/3.4/lib/ -lpython3.4m -o vector.so vector.cpp
