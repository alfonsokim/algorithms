from collections import namedtuple

import matplotlib
import matplotlib.pyplot as plt
import sys

def plot(cities):
    x = [int(city.lat) for city in cities]
    y = [int(city.lon) for city in cities]
    fig, ax = plt.subplots()
    for i, c in enumerate(cities):
        ax.annotate(c.name, (int(c.lat)+0.5, int(c.lon)+0.5))

    plt.plot(x, y, 'bo')
    plt.show()

City = namedtuple('City', 'name, lat, lon')

def parse(str_path):
    return None

if __name__ == '__main__':
    inf = open(sys.argv[1], 'r')
    cities = []
    greedy, best, worst = None, None, None
    for line in inf:
        line = line.strip()
        if line[0] != '[':
            city = City(*line.replace(',', ':').split(':'))
            cities.append(city)
        else:
            if line.startswith('[greedy]'): greedy = parse(line)
            if line.startswith('[best]'): best = parse(line)
            if line.startswith('[worst]'): worst = parse(line)
    plot(cities)
