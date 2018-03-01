from scipy.spatial.distance import cityblock
import sys
import re

filename = sys.argv[1]

file = open(filename, 'r')

first_line = file.readline().strip()
params = first_line.split(' ')
rows = int(params[0])
cols = int(params[1])
n_vehicles = int(params[2])
n_rides = int(params[3])
bonus = int(params[4])
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

    ride = {'start_row': a, 'start_col': b, 'finish_row': x, 'finish_col': y, 'earliest_start': s, 'latest_finish': f}

    rides.append(ride) 

s = cityblock([1,1], [1,2])
print(s)

print(rides)


