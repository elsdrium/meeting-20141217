cython --cplus -o wahaaa.cpp wahaaa.py
clang++ -shared -fPIC -I/usr/local/Cellar/python3/3.4.2_1/Frameworks/Python.framework/Versions/3.4/include/python3.4m/ -L/usr/local/Cellar/python3/3.4.2_1/Frameworks/Python.framework/Versions/3.4/lib/ -lpython3.4m -o wahaaa.so wahaaa.cpp
