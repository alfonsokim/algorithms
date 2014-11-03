
# http://nbviewer.ipython.org/url/norvig.com/ipython/TSPv3.ipynb

from collections import namedtuple
import math
import random
import itertools
import sys
import time

City = namedtuple('City', 'name, lat, lon')

# ===================================================================
def distance(city1, city2):
    """
    """
    x = city1.lat - city2.lat
    y = city1.lon - city2.lon
    return math.sqrt(x*x + y*y)


# ===================================================================
def traveled_distance(path):
    """
    """
    return sum([distance(path[i], path[i+1]) for i in range(len(path) - 1)])


# ===================================================================
def print_path(path, name='', out=sys.stdout):
    """
    """
    str_path = '->'.join([p.name for p in path])
    print >> out, '[%s] %s : %f' % (name, str_path, traveled_distance(path))


# ===================================================================
def make_random_cities(num_cities, min_latlon=20, max_latlon=100):
    """
    """
    return [City(name=str(n), 
            lat=random.randint(min_latlon, max_latlon), 
            lon=random.randint(min_latlon, max_latlon))
           for n in range(num_cities)]


# ===================================================================
def nearest_city(city, cities):
    min_distance = float('inf')
    min_city = None
    for c in cities:
        d = distance(city, c)
        if d < min_distance:
            min_distance = d
            min_city = c
    return min_city


# ===================================================================
def all_cities(cities, start):
    """
    """
    cities = list(cities)
    cities.remove(start)
    all_paths = []
    for path in itertools.permutations(cities):
        one_path = [start]
        one_path.extend(path)
        yield one_path
        #all_paths.append(one_path)


# ===================================================================
def evaluate_all_cities(cities, start):
    #all_paths = all_cities(cities, start)
    global_min = float('inf')
    global_max = 0
    best_path = None
    worst_path = None
    for path in all_cities(cities, start):
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
    """
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
    """
    """
    #random.seed(1)
    benchmark = open('traveler.txt', 'w')
    print >> benchmark, 'num_cities, greedy, best, worst, time_greedy, time_all'
    for num_cities in range(10, 101):
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
        #print >> benchmark, 'num_cities, greedy, best, worst, time_greedy, time_all'
        print >> benchmark, '%i, %f, %f, %f, %f, %f' % (num_cities, traveled_distance(greedy_path), 
                                                        traveled_distance(best_path),
                                                        traveled_distance(worst_path),
                                                        t1-t0, t3-t2)
    benchmark.close()

