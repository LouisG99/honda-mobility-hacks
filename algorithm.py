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

csvfile = pd.read_csv('../autonomous-data/ordered-data.csv', encoding='utf-8')

<<<<<<< HEAD
csv2 = pd.read_csv('usable_data.csv', encoding='utf-8')
df2 = pd.DataFrame(csv2)
||||||| merged common ancestors
csv2 = pd.read_csv('usable_data.csv', encoding='utf-8', nrows=5000)
df = pd.DataFrame(csv2)
=======
csv2 = pd.read_csv('usable_data.csv', encoding='utf-8')
df = pd.DataFrame(csv2)
>>>>>>> 3143053e56485d23340170ceda0e454051dbb54b


df = pd.DataFrame(csvfile)
driveID = df['driveid'].values

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
<<<<<<< HEAD
# ['logtime', 'object number', 'speed', 'alert Level', 'average speed']
||||||| merged common ancestors
# ['logtime', 'object number', 'speed', 'alert Level', 'average speed', 'stdev']
=======
# ['alert Level','object number', 'speed', 'average speed', 'stdev']
>>>>>>> 3143053e56485d23340170ceda0e454051dbb54b
#outWriter.writerow(['John Smith', 'yeet'])


for i in range(len(logtimes)-1):
    log_t = logtimes[i]
    
    radarCar.index = i
<<<<<<< HEAD
    radarCar.dt = log_t - logtimes[i+1]
    radarCar.time = log_t - log0
    radarCar.speed = CAN_speed[i]
||||||| merged common ancestors
    radarCar.dt = (logtimes[i+1] - log_t)*1e-3
    radarCar.time = (log_t - log0)*1e-6
    radarCar.speed = CAN_speed[i] / 3.6
=======
    radarCar.dt = (logtimes[i+1] - log_t)*1e-3 # conversion in seconds
#    radarCar.time = (log_t - log0)*1e-3 # unused
    radarCar.speed = CAN_speed[i] / 3.6 # conversion in m/s
>>>>>>> 3143053e56485d23340170ceda0e454051dbb54b
    
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
<<<<<<< HEAD
        outWriter.writerow([str(log_t), str(carNbr), str(speed), str(score), 
                            str(avrg_speed)])
||||||| merged common ancestors
        if speed>0:
            outWriter.writerow([str(log_t), str(carNbr), str(speed*3.6), str(score), 
                                str(avrg_speed*3.6), str(radarCar.stdevSpeed)])
    
=======
        if speed>0:
            outWriter.writerow([ str(score), str(carNbr), str(speed*3.6), 
                                str(avrg_speed*3.6), str(radarCar.stdevSpeed)])
                                # also converts to km/h
    
>>>>>>> 3143053e56485d23340170ceda0e454051dbb54b
    outputFile.close()
#    time.sleep(1.5)
    
    
    