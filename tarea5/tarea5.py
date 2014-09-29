
def max_subarray(A):
    max_ending_here = max_so_far = 0
    start = end = 0
    for i, x in enumerate(A):
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
        print 'eval: %i max_ending_here: %i max_so_far: %i' % (x, max_ending_here, max_so_far)
    return max_so_far


if __name__ == '__main__':
    import random
    A = [i - 10 for i in range(20)]
    random.shuffle(A)
    print A
    print '='*10
    suma = max_subarray(A)
    print suma