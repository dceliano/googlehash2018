from scipy.spatial.distance import cityblock
import sys
import re

filename = sys.argv[1]

file = open(filename, 'r')

first_line = file.readline().strip()
params = first_line.split(' ')
R = int(params[0])
C = int(params[1])
F = int(params[2])
N = int(params[3])
B = int(params[4])
T = int(params[5])

rides = []
for line in file:
    line = line.strip()
    ride = {}
    params = line.split(' ')
    a = int(params[0])
    b = int(params[1])
    x = int(params[2])
    y = int(params[3])
    s = int(params[4])
    f = int(params[5])

    ride = {'a': a, 'b': b, 'x': x, 'y': y, 's': s, 'f': f}

    rides.append(ride) 

s = cityblock([1,1], [1,2])
print(s)

print(rides)
