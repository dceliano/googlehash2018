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

class Ride(object):
    def __init__(self, start_row, start_column, finish_row, finish_column, earliest_start, latest_finish, ride_number):
        self.start_row = start_row
        self.start_column = start_column
        self.finish_row = finish_row
        self.finish_column = finish_column
        self.earliest_start = earliest_start
        self.latest_finish = latest_finish
        self.ride_number = ride_number
        
class Vehicle(object):
    def __init__(self, busy, vehicle_num):
        self.busy = 0
        self.vehicle_num = vehicle_num
        self.delivered_passengers = []
        self.passenger_distances = {}
    def setBusy(busy):
        self.busy = busy
    def incrementTime(busy):
        if self.busy:
            totalTime
    def deliverPassenger(passenger_num):
        self.delivered_passengers.append(passenger_num)


filename = sys.argv[1]

file = open(filename, 'r')

first_line = file.readline().strip()
params = first_line.split(' ')
rows = int(params[0])
cols = int(params[1])
n_vehicles = int(params[2])
n_rides = int(params[3])
bonus = int(params[4])
max_global_time = int(params[5])

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

    #ride = {'start_row': a, 'start_col': b, 'finish_row': x, 'finish_col': y, 'earliest_start': s, 'latest_finish': f, 'ride_number' : ride_number}
    ride = Ride(a, b, x, y, s, f, ride_number)
    rides.append(ride)
    ride_number += 1

vehicles = []
for i in range(0, n_vehicles):
    vehicles.append(Vehicle(0, i + 1))



s = cityblock([1,1], [1,2]) #example of how to calculate distance between two points
print(s)

#print(rides)
#print(vehicles)

#print(distances([0,0], rides))

# Clock is ticking. T is global time.
for T in range(0, max_global_time):
    #Do the actual algorithm
    x = 1

