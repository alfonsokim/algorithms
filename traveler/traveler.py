
from collections import namedtuple
import math
import random

City = namedtuple('City', 'name, lat, lon')


# ===================================================================
def distance(city1, city2):
    """
    """
    x = city1.lat - city2.lat
    y = city1.lon - city2.lon
    return math.sqrt(x*x + y*y)


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
def nearest_neighbor(cities, start):
    """
    """
    cities.remove(start)
    visited = [start]
    unvisited = cities
    current = start
    distance_so_far = 0
    while unvisited:
        nearest = nearest_city(current, unvisited)
        d = distance(current, nearest)
        distance_so_far += d
        print 'La ciudad mas cercana de %s es %s con %f' % (current, nearest, d)
        visited.append(nearest)
        unvisited.remove(nearest)
        current = nearest
    return visited, distance_so_far


# ===================================================================
if __name__ == '__main__':
    """
    """
    cities = make_random_cities(10)
    start = random.choice(cities)
    path, distance = nearest_neighbor(cities, start)
    print path, distance
