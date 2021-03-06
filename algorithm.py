# danger lvl (1, 2, 3), dist from car (absolute), 
# speed, GPS location (calculate with that of radarCar and rel position)

import pandas as pd 
import numpy as np
import csv
import time

#Use dataset 1, by calculating speed of vehicles around and all of that
#Problem with dataset 2 is that vechicles might not be close by, 
#so might not face same conditions ... 
#no one might be driving dangerously

# dangerous one at 5:58 in video 

import math

class closeCar:
    def __init__(self, distance, angle):
        self.distance = []
        self.angle = angle
        

class radarCar:
    def __init__(self, time, dt):
        self.speed = 0
        self.time = time
        self.dt = dt
        self.nearCarsDist = [None] * 64 # size 64
                # should be array of array such that 
                # index is like [obj_nbr][time_index]
        self.nearCarsAngle = [None] * 64  # size 64
        self.nearCarsSpeed = [ [None] ] * 64  # size 64, each inner array size-1 of dist
        self.carsScore = [ [None] ] * 64  # size 64
        self.meanSpeed = 0
        self.stdevSpeed = 0
        self.time_Index = 0
        
        
    def getSpeed(self, dist1, dist2, angle1, angle2):
        horiz_d = math.cos(angle1)*dist1 - math.cos(angle2)*dist2
        vertical_d = math.sin(angle1)*dist1 - math.sin(angle2)*dist2
        vertical_d += self.speed * self.dt
        
        total_d = (horiz_d**2 + vertical_d**2)**0.5
        return total_d / self.dt
    

    def updateAverageSpeed(self):
        speedSum = 0
        count = 0
        for i in range(len(self.nearCarsAngle)-1):
            dist_0 = self.nearCarsDist[i][self.time_index]
            dist_1 = self.nearCarsDist[i][self.time_index+1]
            if dist_0==0 or dist_1==0: 
                speed = "NO"
            else:
                angle_0 = self.nearCarsAngle[i][self.time_index]
                angle_1 = self.nearCarsAngle[i][self.time_index+1]
                
                speed = self.getSpeed(dist_0, dist_1, angle_0, angle_1)
                if speed > 8.9: # 20 mph
                    speedSum += speed
                    count += 1
                    
            self.nearCarsSpeed[i].append(speed)
        
        self.meanSpeed = speedSum / count
        
    
    def updateStdevSpeed(self):
        mean = self.meanSpeed
        sumSqrd = 0
        count = 0
        
        for i in range(len(self.nearCarsAngle)-1):
            speed = self.nearCarsSpeed[i][-1]
            
            if type(speed) == int:
                if speed > 8.9: # 20 mph 
                    sumSqrd += speed**2
                    count += 1
                    
        self.stdevSpeed = sumSqrd/count - mean**2
        
    def updateScores(self):
        for carNbr in range(len(self.carsScore)):
            speed = self.nearCarsSpeed[carNbr][-1]
            score = self.scoreSpeed(speed)
            
            self.carsScore[carNbr].append(score)
            
                 
    def scoreSpeed(self, speed): 
        if (speed == "NO"):
            return "NO"
        if (speed <= self.meanSpeed + self.stdevSpeed):
            return 0
        if (speed <= self.meanSpeed + 2 * self.stdevSpeed):
            return 1
        if (speed <= self.meanSpeed + 3 *self.stdevSpeed):
            return 2
        return 3
    
    
    def load_car_Dist(self, data_frame):
        base_flag = "LRR_RANGE_"
        for i in range(64):
            flag = base_flag + str(i)
            self.nearCarsDist[i] = data_frame[flag].values
        return 
    
    
    def load_car_Angle(self, data_frame):
        base_flag = "LRR_RANGE_"
        for i in range(64):
            flag = base_flag + str(i)
            self.nearCarsAngle[i] = data_frame[flag].values
        return        
    
    
                

def getCarNbr(col_name):
    # 2 digits vs 1 digit
    if col_name[-2].isdigit():
        return int(col_name[-2:])
    
    return int(col_name[-1])
        


def yeet():
    print("yeet")
#import json

# other file
# from radarCar import *


# dont know if all that will work with numpy, maybe cast 
# stuff to list

# csvfile = pd.read_csv('../autonomous-data/ordered-data.csv', encoding='utf-8')

csv2 = pd.read_csv('usable_data.csv', encoding='utf-8')
df = pd.DataFrame(csv2)


# df = pd.DataFrame(csvfile)
# driveID = df['driveid'].values

start_time = 0.0
dt = 1e-6 # in s
radarCar = radarCar(start_time, dt)

radarCar.load_car_Dist(df)
radarCar.load_car_Angle(df)

logtimes = df['logtime'].values
CAN_speed = df['CAN_VEHICLE_SPEED'].values

log0 = logtimes[0]


#outputFile = open('scoredData.csv', 'a')
#outWriter = csv.writer(outputFile, delimiter=',', 
#                       quotechar='"')
# ADD COLUMN NAMES
#fields = ['Specify fields']
# ['logtime', 'object number', 'speed', 'alert Level', 'average speed']
#outWriter.writerow(['John Smith', 'yeet'])


for i in range(len(logtimes)-1):
    log_t = logtimes[i]
    
    radarCar.index = i
    radarCar.dt = log_t - logtimes[i+1]
    radarCar.time = log_t - log0
    radarCar.speed = CAN_speed[i]
    
    radarCar.updateAverageSpeed()
    radarCar.updateStdevSpeed()
    
    
    # Writing into output
    outputFile = open('scoredData.csv', 'a')
    outWriter = csv.writer(outputFile, delimiter=',', 
                       quotechar='"')
    total_cars = 64
    for carNbr in range(len(total_cars)):
        score = radarCar.carsScore[carNbr][-1]
        speed = radarCar.nearCarsSpeed[carNbr][-1]
        avrg_speed = radarCar.meanSpeed
        outWriter.writerow([str(log_t), str(carNbr), str(speed), str(score), 
                            str(avrg_speed)])
    outputFile.close()
#    time.sleep(1.5)
    
    
    