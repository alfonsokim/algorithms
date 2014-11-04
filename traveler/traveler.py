
from collections import namedtuple
import math
import random
import itertools
import sys
import time

""" Estructura para representar una ciudad:
    name: Nombre de la ciudad
    lat: Coordenada x de la ciudad
    lon: Coordenada y de la ciudad
"""
City = namedtuple('City', 'name, lat, lon')

# ===================================================================
def distance(city1, city2):
    """ Calcula la distancia euclideanea entre 2 ciudades
        :return distancia = sqrt((city1.lat - city2.lat) + (city1.lon - city.lon))
    """
    x = city1.lat - city2.lat
    y = city1.lon - city2.lon
    return math.sqrt(x*x + y*y)


# ===================================================================
def traveled_distance(path):
    """ Calcula la distancia recorrida en todo un camino (lista de ciudades)
        :param path: El camino recorrido
        :return: La suma de las distancias entre los puntos
    """
    return sum([distance(path[i], path[i+1]) for i in range(len(path) - 1)])


# ===================================================================
def print_path(path, name='', out=sys.stdout):
    """ Imprime el camino recorrido
        :param path: El camino
        :param name: Nombre del camino, opcional
        :param out: Dispositivo de salida, salida estandar por default
    """
    str_path = '->'.join([p.name for p in path])
    print >> out, '[%s] %s : %f' % (name, str_path, traveled_distance(path))


# ===================================================================
def make_random_cities(num_cities, min_latlon=20, max_latlon=100):
    """ Crea una lista de ciudades con coordenadas aleatorias
        :param num_cities: Numero de ciudades a generar
        :param min_latlon: Latitud y longitud minima para el valor aleatorio
                           20 por defecto
        :param max_latlon: Latitud y longitud maxima para el valor aleatorio
                           100 por defecto
        :return Una lista de ciudades aleatorias
    """
    return [City(name=str(n), 
            lat=random.randint(min_latlon, max_latlon), 
            lon=random.randint(min_latlon, max_latlon))
           for n in range(num_cities)]


# ===================================================================
def nearest_city(city, cities):
    """ Dada una ciudad, encuentra la ciudad mas cercana
        :param city: La ciudad origen
        :param cities: La lista de ciudades a encontrar la mas cercana
        :return La ciudad mas cercana a city, en el conjunto cities
    """
    min_distance = float('inf')
    min_city = None
    for c in cities:
        d = distance(city, c)
        if d < min_distance:
            min_distance = d
            min_city = c
    return min_city


# ===================================================================
def all_paths(cities, start):
    """ Genera las permutaciones posibles para la lista de ciudades,
        todas las permutaciones comienzan con la ciudad start
        :param cities: La lista de ciudades a obtener sus permutaciones
        :param start: La ciudad inicial de la permutacion
        :return: Un iterador con una camino en la permutacion de ciudades
    """
    cities = list(cities)
    cities.remove(start)
    all_paths = []
    for path in itertools.permutations(cities):
        one_path = [start]
        one_path.extend(path)
        yield one_path


# ===================================================================
def evaluate_all_cities(cities, start):
    """ Evalua por fuerza bruta todos los caminos posibles en el 
        conjunto de ciudades.
        :param cities: La lista de ciudades a iterar
        :param start: La ciudad inicial
        :return Una tupla (min, max) donde min es el camino mas corto 
                y max es el camino mas largo
    """
    global_min = float('inf')
    global_max = 0
    best_path = None
    worst_path = None
    for path in all_paths(cities, start):
        d = traveled_distance(path) 
        if d < global_min:
            global_min = d
            best_path = path
        if d > global_max:
            global_max = d
            worst_path = path
    return best_path, worst_path


# ===================================================================
def nearest_neighbor(cities, start, debug=False):
    """ Algoritmo greedy para recorrer un conjunto de ciudades.
        Siempre toma la ciudad mas cercana a la ciudad actual, esperando
        encontar el minimo global del conjunto
        :param cities: La lista de ciudades a evaluar
        :param start: La ciudad inicial a navegar
        :param debug: Escribir a consola el avance del proceso
        :return El camino mas corto encotrado por el algoritmo
    """
    cities = list(cities)
    cities.remove(start)
    visited = [start]
    unvisited = cities
    current = start
    distance_so_far = 0
    while unvisited:
        nearest = nearest_city(current, unvisited)
        d = distance(current, nearest)
        if debug: print 'La ciudad mas cercana de %s es %s con %f' % (current, nearest, d)
        visited.append(nearest)
        unvisited.remove(nearest)
        current = nearest
    return visited


# ===================================================================
if __name__ == '__main__':
    """ Punto de entrada a la consola
        Evalua el algoritmo greedy para n ciudades, ademas calcula por
        fuerza bruta el mejor y el menor camino que habia en el arreglo.
        Escribe a un archivo por numero de ciudades iteradas el detalle
        de cada ciudad, el mejor camino encontrado greedy y el mejor y
        peor camino de todo el grafo
    """
    benchmark = open('traveler.txt', 'w')
    print >> benchmark, 'num_cities, greedy, best, worst, time_greedy, time_all'
    for num_cities in range(10, 12):
        sys.stdout.write('Evaluando todos los caminos para %i ciudades' % (num_cities))
        sys.stdout.flush()
        graph_file = open('ciudades_%i.txt' % num_cities, 'w')
        cities = make_random_cities(num_cities)
        for city in cities:
            print >> graph_file, '%s:%i,%i' % (city.name, city.lat, city.lon)
        start = random.choice(cities)
        t0 = time.clock()
        greedy_path = nearest_neighbor(cities, start)
        t1 = time.clock()
        print_path(greedy_path, name='greedy', out=graph_file)
        t2 = time.clock()
        best_path, worst_path = evaluate_all_cities(cities, start)
        t3 = time.clock()
        print_path(best_path, name='best', out=graph_file)
        print_path(worst_path, name='worst', out=graph_file)
        graph_file.close()
        print '... %fs' % (t3-t1)
        print >> benchmark, '%i, %f, %f, %f, %f, %f' % (num_cities, traveled_distance(greedy_path), 
                                                        traveled_distance(best_path),
                                                        traveled_distance(worst_path),
                                                        t1-t0, t3-t2)
    benchmark.close()

