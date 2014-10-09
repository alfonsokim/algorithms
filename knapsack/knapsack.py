from collections import namedtuple

Item = namedtuple('Item', 'name, weight, value')

problema1 = [Item('a', 11, 20), Item('b', 7, 10), Item('c', 5, 11), Item('d', 4, 5), 
			 Item('e', 3, 25), Item('f', 3, 50), Item('g', 3, 15), Item('h', 2, 12), 
			 Item('i', 2, 6), Item('j', 2, 4), Item('k', 2, 5), Item('l', 1, 30) ]

print problema1

MAX_W = 20

values = []

for item in problema1:
	values.append([0 for _ in range(MAX_W)])

for i in range(len(problema1) + 1):
	item = problema1[i-1]
	for j in range(MAX_W + 1):
		if item.weight < j and (item.value + values[i - 1][j - item.weight]) > values[i - 1][j]:
			print item
			values[i][j] = item.value + values[i - 1][j - item.weight]
		else:
			values[i][j] = values[i - 1][j]

print values
