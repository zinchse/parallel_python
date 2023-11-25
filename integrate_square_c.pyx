# integrate_square_c.pyx


cpdef double integrate_square(float l, float r, int n_steps):
    cdef int i
    cdef double s = 0
    cdef double h = (r - l) / n_steps
    cdef double x = 0
    cdef double f
    with nogil:
        for i from 0 <= i < n_steps:
            x = l + i * h
            f = x ** 2
            s += f * h 
    return s