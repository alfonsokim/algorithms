
def insertionsort(array):
    for i in range(1, len(array)):

        key = array[i]
        j = i - 1
        while (j >= 0) and (array[j] >  key):
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = key

    return array

if __name__ == '__main__':
	import random
	import time

	times = open('insertion.txt',  'a')
	for n in range(300000, 10010000, 100000):
		array = [random.randint(0, 100 * n) for _ in range(n)]
		t1 = time.clock()
		insertionsort(array)
		print >> times, 'n=%i,t=%.4f' % (n, (time.clock() - t1))
		print n
	times.close()