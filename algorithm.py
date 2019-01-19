<<<<<<< HEAD
# danger lvl (1, 2, 3), dist from car (absolute), 
# speed, GPS location (calculate with that of radarCar and rel position)
# 

import pandas as pd 
import numpy as np
import json

# other file
from radarCar import *


csvfile = pd.read_csv('../autonomous-data/ordered-data.csv', encoding='utf-8')

df = pd.DataFrame(csvfile)
driveID = df['driveid'].values


start_time = 0.0
dt = 1e-6 # in s

radarCar = radarCar(start_time, dt)

# load obj distances and angles into object
radarCar.load_car_Dist(df)
radarCar.load_car_Angle(df)

logtimes = df['logtime'].values

#Use dataset 1, by calculating speed of vehicles around and all of that
#Problem with dataset 2 is that vechicles might not be close by, 
#so might not face same conditions ... 
#no one might be driving dangerously

# dangerous one at 5:58 in video 

import json
import math

class closeCar:
    def __init__(self, distance, angle):
        self.distance = distance
        self.angle = angle
        

class radarCar:
    def __init__(self, speed, time):
        self.speed = speed
        self.time = time
        self.nearbyCars = []
    
    
    def getSpeed(self, dist1, dist2, angle1, angle2, dt):
        horiz_d = math.cos(angle1)*dist1 - math.cos(angle2)*dist2
        vertical_d = math.sin(angle1)*dist1 - math.sins(angle2)*dist2
        vertical_d += self.speed*dt
        
        total_d = (horiz_d**2 + vertical_d**2)**0.5
        return total_d / dt

    def getAverageSpeed(distances, angles, dt):
        speedSum = 0
        count = 0
        for car in self.nearByCars:
            if (distances[count] != 0): 
                



import pandas

csvfile = pandas.read_csv('../autonomous-data/ordered-data.csv', encoding='utf-8')
