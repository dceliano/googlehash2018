from scipy.spatial.distance import cityblock
import sys
import re

# start point [x,y]
# rides array of dicts
def distances(start_point, rides):
    dist_map = {}
    a = start_point
    for ride in rides:
        b = [ ride['start_row'], ride['start_col'] ]
        ride_number = ride['ride_number']
        dist = cityblock(a, b)
        dist_map[ride_number] = dist
    return dist_map

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
ride_number = 0
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

    ride = {'start_row': a, 'start_col': b, 'finish_row': x, 'finish_col': y, 'earliest_start': s, 'latest_finish': f, 'ride_number' : ride_number}

    rides.append(ride) 
    ride_number = ride_number + 1

s = cityblock([1,1], [1,2])
print(s)

print(rides)

print(distances([0,0], rides))
