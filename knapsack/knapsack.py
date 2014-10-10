from collections import namedtuple

""" Item es una tupla nombrada; como un objeto simple con propiedades
    name: El nombre del elemento
    weight: El peso del elemento
    value: El valor del elemento
"""
Item = namedtuple('Item', 'name, weight, value')

""" Elementos del problema visto en clase
"""
problema = [Item('a', 11, 20), Item('b', 7, 10), Item('c', 5, 11), Item('d', 4, 5), 
            Item('e', 3, 25), Item('f', 3, 50), Item('g', 3, 15), Item('h', 2, 12), 
            Item('i', 2, 6), Item('j', 2, 4), Item('k', 2, 5), Item('l', 1, 30) ]

""" Prueba simple
"""
simple = [Item('a', 5, 10), Item('b', 4, 40), Item('c', 6, 30), Item('d', 3, 50)]

# ===============================================================
def knapsack_bottom_up(items, max_weight):
    """ Implementacion del problema bottom-up
        :items Los elementos a revisar
        :max_weight El peso a maximizar
        :return La lista con los elementos mas importantes 
    """
    # Inicializacion de las variables
    value_line = [0 for _ in range(max_weight + 1)]
    values = [list(value_line) for _ in range(len(items) +  1)]

    # para cada elemento...
    for i in range(1, len(items) + 1):
        item = items[i - 1]
        # se procesa si puede estar en el maximo actual
        for current_max in range(max_weight + 1):
            if item.weight > current_max: # Se pasa, dejar los valores del elemento anterior
                values[i][current_max] = values[i - 1][current_max]
            else:   # Si no se pasa, ver si el elemento actual es un maximo
                a = values[i - 1][current_max]
                b = values[i - 1][current_max - item.weight] + item.value
                values[i][current_max] = max(a, b)

    # Formar la lista maximizada de salida
    result = []
    current_max = max_weight
    for i in range(len(items), 0, -1): # para cada elemento
        a = values[i][current_max]
        b = values[i - 1][current_max]
        if a != b: # Si es un maximo en su valor local
            result.append(items[i - 1]) # agregar a la lista de salida
            current_max -= items[i - 1].weight

    result.reverse()
    return result


# ===============================================================
def knapsack_top_down_recursivo(items, n, max_w):
    """ Funcion recursiva.
        Devuelve el maximo entre el peso del elemento n-1 y 
        el peso del elemento n-1 + el valor del elemento actual
    """
    if n == 0: return 0
    ktdr = knapsack_top_down_recursivo # Para evitar lineas largas
    item = items[n - 1]
    if item.weight > max_w: # Si el valor se pasa regresar el n-1
        return ktdr(items, n - 1, max_w)
    else:   # Si no, ver cual es el maximo
        a = ktdr(items, n - 1, max_w)
        b = ktdr(items, n - 1, max_w - item.weight) + item.value
        return max(a, b)  # y devolverlo


# ===============================================================
def knapsack_top_down(items, max_weight):
    """ Implementacion del problema top-down
        :items Los elementos a revisar
        :max_weight El peso a maximizar
        :return La lista con los elementos mas importantes 
    """
    # Inicializacion de las variables
    ktdr = knapsack_top_down_recursivo # Para evitar lineas largas
    
    # Formar la lista maximizada de salida
    result = []
    current_max = max_weight
    for i in range(len(items), 0, -1): # para cada elemento
        a = ktdr(items, i, current_max)
        b = ktdr(items, i - 1, current_max)
        if a != b:  # Si es un maximo en su valor local
            result.append(items[i - 1]) # agregar a la lista de salida
            current_max -= items[i - 1].weight
    result.reverse()
    return result


# ===============================================================
if __name__ == '__main__':
    """ Punto de entrada a la consola
    """
    result_topdown = knapsack_top_down(problema, 20)
    print '\n%s Top Down %s' % ('*'*10, '*'*10)
    print '\n'.join([str(r) for r in result_topdown])
    
    result_bottomup = knapsack_bottom_up(problema, 20)
    print '\n%s Bottom-Up %s' % ('*'*10, '*'*10)
    print '\n'.join([str(r) for r in result_bottomup])


