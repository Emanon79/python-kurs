def f(double x):
    return x*x

def integrate(f, double a, double b, double N):
    cdef double distance, interval

    distance = b - a
    interval = distance/N

    cdef int i
    cdef double sum
    cdef double x2

    sum = 0
    i = 0
    while i < N+1:
        x2 = a + i*interval
        sum += interval * x2*x2
        i += 1

    return sum
