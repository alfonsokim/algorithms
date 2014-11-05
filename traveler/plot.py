from collections import namedtuple

import matplotlib
import matplotlib.pyplot as plt
import sys

def plot_path(cities, city, path, name):
    route = list(cities)
    x_lines, y_lines = [], []
    #print path
    for node in path:
        c = [c for c in cities if c.name == node][0]
        x_lines.append(c.lat)
        y_lines.append(c.lon)
    x_lines.append(city.lat)
    y_lines.append(city.lon)
    #print x_lines
    plt.plot(x_lines, y_lines, '-')


def plot(cities, city):
    print cities
    print city
    #all_cities = list(cities)
    #cities.remove(city)
    x = [int(c.lat) for c in cities]
    y = [int(c.lon) for c in cities]
    #color = ['b' if c.name != city.name else 'r' for c in cities]
    fig, ax = plt.subplots()
    for i, c in enumerate(cities):
        ax.annotate(c.name, (int(c.lat)+0.5, int(c.lon)+0.5))
    ax.annotate(city.name, (int(city.lat)+0.5, int(city.lon)+0.5))
    plt.plot(x, y, 'bo')
    plt.plot([city.lat], [city.lon], 'ro', markersize=8)

    """
    route = list(all_cities)
    x_lines, y_lines = [], []
    print path
    for node in path:
        c = [c for c in all_cities if c.name == node][0]
        x_lines.append(c.lat)
        y_lines.append(c.lon)
    x_lines.append(city.lat)
    y_lines.append(city.lon)
    print x_lines
    plt.plot(x_lines, y_lines, '-')
    """
    

City = namedtuple('City', 'name, lat, lon')

def parse(str_path):
    return str_path[str_path.find(']')+2 : str_path.find(' : ')].split('->')

def find_start_city(cities, path):
    for city in cities:
        if city.name == path[0]:
            return cities, city

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

    file_name = sys.argv[1].split('.')[0]

    cities, city = find_start_city(cities, greedy)
    plot(cities, city)
    plot_path(cities, city, greedy, 'greedy')
    figure = plt.gcf() # get current figure
    figure.set_size_inches(5, 5)
    plt.savefig('%s_greedy.png' % file_name)
    plt.close()

    cities, city = find_start_city(cities, best)
    plot(cities, city)
    plot_path(cities, city, best, 'best')
    figure = plt.gcf() # get current figure
    figure.set_size_inches(5, 5)
    plt.savefig('%s_best.png' % file_name)
    plt.close()

    cities, city = find_start_city(cities, worst)
    plot(cities, city)
    plot_path(cities, city, worst, 'worst')
    figure = plt.gcf() # get current figure
    figure.set_size_inches(5, 5)
    plt.savefig('%s_worst.png' % file_name)
    plt.close()
    