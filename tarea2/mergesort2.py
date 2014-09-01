
def mergesort(array):
    if len(array) == 1:
        return array
    else:
        #recursion: break arrayuence down into chunks of 1
        mid = len(array)/2
        left = mergesort(array[:mid])
        right = mergesort(array[mid:])

        i, j, k = 0, 0, 0 #i= left counter, j= right counter, k= master counter

        #run until left or right is out
        while i < len(left) and j < len(right):
            #if current left val is < current right val; assign to master list
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1; k += 1
            #else assign right to master
            else:
                array[k] = right[j]
                j += 1; k += 1

        #handle remaining items in remaining list
        remaining = left if i < j else right
        r = i if remaining == left else j

        while r < len(remaining):
            array[k] = remaining[r]
            r += 1; k += 1

        return array

if __name__ == '__main__':
	import random
	import time

	times = open('merge2.txt',  'a')
	for n in range(2000000, 10010000, 10000):
	#for n in range(1000, 10000, 10000):
		array = [random.randint(0, 100 * n) for _ in range(n)]
		t1 = time.clock()
		mergesort(array)
		print >> times, 'n=%i,t=%.4f' % (n, (time.clock() - t1))
		print n
	times.close()