
from collections import namedtuple
import math
import random
import itertools

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
def print_path(path):
    """
    """
    str_path = '->'.join([p.name for p in path])
    print '%s : %f' % (str_path, traveled_distance(path))


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
        all_paths.append(one_path)
    return all_paths


# ===================================================================
def evaluate_all_cities(cities, start):
    all_paths = all_cities(cities, start)
    global_min = float('inf')
    global_max = 0
    best_path = None
    worst_path = None
    for path in all_paths:
        d = traveled_distance(path) 
        if d < global_min:
            global_min = d
            best_path = path
        if d > worst_path:
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
    cities = make_random_cities(10)
    start = random.choice(cities)
    path = nearest_neighbor(cities, start)
    print_path(path)
    print '%s Evaluando todos los caminos %s' % ('*'*10, '*'*10)
    best_path, worst_path = evaluate_all_cities(cities, start)
    print_path(best_path)
    print_path(worst_path)
