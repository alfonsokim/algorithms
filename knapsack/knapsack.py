from collections import namedtuple

Item = namedtuple('Item', 'name, weight, value')

problema1 = [Item('a', 11, 20), Item('b', 7, 10), Item('c', 5, 11), Item('d', 4, 5), 
			 Item('e', 3, 25), Item('f', 3, 50), Item('g', 3, 15), Item('h', 2, 12), 
			 Item('i', 2, 6), Item('j', 2, 4), Item('k', 2, 5), Item('l', 1, 30) ]

simple = [Item('a', 5, 10), Item('b', 4, 40), Item('c', 6, 30), Item('d', 3, 50)]

MAX_W = 20

# ===============================================================
def knapsack_bottom_up(items, max_weight):
    """
    """
    value_line = [0 for _ in range(max_weight + 1)]
    values = [list(value_line) for _ in range(len(items) +  1)]

    for i in range(1, len(items) + 1):
        item = items[i - 1]
        for current_max in range(max_weight + 1):
            if item.weight > current_max:
                values[i][current_max] = values[i - 1][current_max]
            else:
                a = values[i - 1][current_max]
                b = values[i - 1][current_max - item.weight] + item.value
                values[i][current_max] = max(a, b)

    result = []
    current_max = max_weight
    for i in range(len(items), 0, -1):
        a = values[i][current_max]
        b = values[i - 1][current_max]
        if a != b:
            result.append(items[i - 1])
            current_max = items[i - 1].weight

    result.reverse()
    return result


# ===============================================================
def knapsack_top_down_recursivo(items, n, max_w):
    """
    """
    if n == 0:
        return 0
    ktdr = knapsack_top_down_recursivo # Para evitar lineas largas
    item = items[n - 1]
    if item.weight > max_w:
        return ktdr(items, n - 1, max_w)
    else:
        a = ktdr(items, n - 1, max_w)
        b = ktdr(items, n - 1, max_w - item.weight) + item.value
        return max(a, b)


# ===============================================================
def knapsack_top_down(items, max_weight):
    """
    """
    value_line = [0 for _ in range(max_weight + 1)]
    values = [list(value_line) for _ in range(len(items) +  1)]
    ktdr = knapsack_top_down_recursivo # Para evitar lineas largas
    result = []
    current_max = max_weight
    for i in range(len(items), 0, -1):
        a = ktdr(items, i, current_max)
        b = ktdr(items, i - 1, current_max)
        if a != b:
            result.append(items[i - 1])
            current_max -= items[i - 1].weight
    result.reverse()
    return result


# ===============================================================
if __name__ == '__main__':
    result_topdown = knapsack_top_down(problema1, 20)
    print '%s Top Down %s' % ('*'*10, '*'*10)
    print '\n'.join([str(r) for r in result_topdown])
    
    result_bottonup = knapsack_bottom_up(problema1, 20)
    print '%s Bottom-Up %s' % ('*'*10, '*'*10)
    print '\n'.join([str(r) for r in result_topdown])


