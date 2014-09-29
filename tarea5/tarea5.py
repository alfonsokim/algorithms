
# -------------------------------------------------------------
def max_subarray(A):
    """ Devuelve la suma maxima del arreglo
    """
    max_ending_here = max_so_far = 0
    for x in A:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

# -------------------------------------------------------------
def max_subarray_bounds(A):
    """ Devuelve los limites del arreglo donde se encuentra la suma maxima
    """
    max_ending_here = max_so_far = 0
    start = end = temp = 0
    for i, x in enumerate(A):
        if max_ending_here < 0:
            max_ending_here = x
            temp = i;
        else:
            max_ending_here += x
        if max_ending_here >= max_so_far:
            max_so_far = max_ending_here
            start = temp
            end = i
    return start, end

# -------------------------------------------------------------
if __name__ == '__main__':
    import random, sys, math

    arr_size = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    offset = int(math.ceil(arr_size / 2))
    print 'Probando con arreglo de longitud %i y desplazamiento de -%i' % (arr_size, offset)

    A = [i - offset for i in range(arr_size)]
    random.shuffle(A)
    start, end = max_subarray_bounds(A)
    max_sum = sum(A[start:end+1])

    print 'Arreglo original:\n%s' % A
    print '=' * 20
    print 'Subarr maximo: A[%i:%i] =\n%s' % (start, end, A[start:end])
    print 'Suma = %i' % max_sum
