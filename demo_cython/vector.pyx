cdef extern from "<vector>" namespace "std":
    cdef cppclass vector[T]:
        cppclass iterator:
            T operator*()
            iterator operator++()
            bint operator==(iterator)
            bint operator!=(iterator)
        vector()
        void push_back(T&)
        T& operator[](int)
        T& at(int)
        iterator begin()
        iterator end()
        size_t size()


def demo():
    cdef vector[int] v
    v.push_back( 1 )
    v.push_back( 5566 )
    print( v.size() )
    cdef vector[int].iterator iter  #iter is declared as being of type vector<int>::iterator
