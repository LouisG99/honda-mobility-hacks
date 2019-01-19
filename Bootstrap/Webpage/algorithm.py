# danger lvl (1, 2, 3), dist from car (absolute), 
# speed, GPS location (calculate with that of radarCar and rel position)

import pandas as pd 
import numpy as np
import csv
import time
#import json

# other file
from radarCar import *


# dont know if all that will work with numpy, maybe cast 
# stuff to list

#csvfile = pd.read_csv('../autonomous-data/ordered-data.csv', encoding='utf-8')

csv2 = pd.read_csv('usable_data.csv', encoding='utf-8', skiprows=range(1, 2500))
df = pd.DataFrame(csv2)


#df2 = pd.DataFrame(csvfile)
#driveID = df['driveid'].values


start_time = 0.0
dt = 1 # in s
radarCar = radarCarClass(start_time, dt)

radarCar.load_car_Dist(df)
radarCar.load_car_Angle(df)

logtimes = df['logtime'].values
CAN_speed = df['CAN_VEHICLE_SPEED'].values

log0 = logtimes[0]

outputFile = open('scoredData.csv', 'w')
outputFile.close()

#outputFile = open('scoredData.csv', 'a')
#outWriter = csv.writer(outputFile, delimiter=',', 
#                       quotechar='"')
# ADD COLUMN NAMES
#fields = ['Specify fields']
# ['alert Level','object number', 'speed', 'average speed', 'stdev']
#outWriter.writerow(['John Smith', 'yeet'])


for i in range(len(logtimes)-1):
#for i in range(10):

    if (i%1==0): 
        print(i)
    log_t = logtimes[i]
    
    radarCar.index = i
    radarCar.dt = (logtimes[i+1] - log_t)*1e-3 # conversion in seconds
#    radarCar.time = (log_t - log0)*1e-3 # unused
    radarCar.speed = CAN_speed[i] / 3.6 # conversion in m/s
    
    radarCar.updateAverageSpeed()
    radarCar.updateStdevSpeed()
    radarCar.updateScores()
    
    
    # Writing into output
    open('scoredData.csv', 'w').close()
    outputFile = open('scoredData.csv', 'a')
    outWriter = csv.writer(outputFile, delimiter=',', 
                       quotechar='"')
    total_cars = 64
#    print(len(radarCar.nearCarsSpeed), len(radarCar.nearCarsSpeed))
    
    for carNbr in range(total_cars):
        score = radarCar.carsScore[carNbr]
        speed = radarCar.nearCarsSpeed[carNbr]
        avrg_speed = radarCar.meanSpeed
        if speed>0 and score!=-1:
            outWriter.writerow([ str(score), str(carNbr), str(speed*3.6), 
                                str(avrg_speed*3.6), str(radarCar.stdevSpeed)])
                                # also converts to km/h
    
    outputFile.close()

    time.sleep(0.25)

#speedCar = radarCar.nearCarsSpeed[4][:1000]

#dist = df['LRR_RANGE_4'].values
    