
import math

FUNCTIONS = [
	('lg* log(n)', lambda n: (iterated_log(math.log(n, 2)))),
	('log(lg* n)', lambda n: (math.log(iterated_log(n), 2))),
	('3/2 n', lambda n: (3 / 2 * n)),
	('n^3', lambda n: (n ** 3)),
	('(log n)^log n', lambda n: (math.log(n, 2) ** math.log(n, 2))),
	('3^log(n)', lambda n: (3 ** math.log(n, 2))),
	('2^sqrt(2 log(n))', lambda n: 2 ** math.sqrt(2 * math.log(n))),
	('log(log(n))', lambda n: math.log(math.log(n, 2), 2)),
	('n^3', lambda n: n ** 3),
	('n 2^n', lambda n: n * (2 ** n)),
	('2 log(n)', lambda n: 2 * math.log(n, 2)),
	('log(n)', lambda n: math.log(n)),
	('e^n', lambda n: math.exp(n)),
	('n', lambda n: n),
	('n^2', lambda n: n ** 2),
	('2^n', lambda n: 2 ** n),
	('log(n!)', lambda n: math.log(math.factorial(n), 2)),
	('n^(lg* log(n))', lambda n: n ** (iterated_log(math.log(n, 2)))),
	('4^log(n)', lambda n: 4 ** math.log(n, 2)),
	('n!', lambda n: math.factorial(n)),
	('2^2^n', lambda n: 2 ** (2 ** n)),
	('(log n)!', lambda n: math.log(math.factorial(n), 2)),
	('n^(1/log(n))', lambda n: n ** (1 / math.log(n))),
	('1', lambda n: 1),
	('sqrt(log(n))', lambda n: math.sqrt(math.log(n, 2))),
	('2^2^n+1', lambda n: 2 ** (2 ** (n+1)))
]

def iterated_log(n):
	if n <= 1: return 0
	else: return 1 + iterated_log(math.log(n, 2))


if __name__ == '__main__':
	import operator
	values = dict([(name, function(10)) for name, function in FUNCTIONS])
	sorted_values = sorted(values.iteritems(), key=operator.itemgetter(1))
	for name, value in sorted_values:
		try:
			print '%s: %f' % (name, value)
		except:
			print name + ': ' + str(value)