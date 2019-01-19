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

csv2 = pd.read_csv('usable_data.csv', encoding='utf-8', nrows=10000)
df = pd.DataFrame(csv2)


df2 = pd.DataFrame(csvfile)
driveID = df['driveid'].values


start_time = 0.0
dt = 1 # in s
radarCar = radarCarClass(start_time, dt)

radarCar.load_car_Dist(df)
radarCar.load_car_Angle(df)
print()

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
# ['logtime', 'object number', 'speed', 'alert Level', 'average speed']
#outWriter.writerow(['John Smith', 'yeet'])


#for i in range(len(logtimes)-1):
for i in range(100):

    if (i%1000==0): 
        print(i)
    log_t = logtimes[i]
    
    radarCar.index = i
    radarCar.dt = (logtimes[i+1] - log_t)*1e-6
    radarCar.time = (log_t - log0)*1e-6
    radarCar.speed = CAN_speed[i] / 3.6
    
    radarCar.updateAverageSpeed()
    radarCar.updateStdevSpeed()
    radarCar.updateScores()
    
    
    # Writing into output
    outputFile = open('scoredData.csv', 'a')
    outWriter = csv.writer(outputFile, delimiter=',', 
                       quotechar='"')
    total_cars = 64
    print(len(radarCar.nearCarsSpeed[1]), len(radarCar.nearCarsSpeed[18]))
    
    for carNbr in range(total_cars):
        score = radarCar.carsScore[carNbr][-1]
        speed = radarCar.nearCarsSpeed[carNbr][-1]
        avrg_speed = radarCar.meanSpeed
        if speed>0:
            outWriter.writerow([str(log_t), str(carNbr), str(speed*3.6), str(score), 
                                str(avrg_speed*3.6)])
    
    outputFile.close()
#    time.sleep(1.5)

speedCar = radarCar.nearCarsSpeed[4][:1000]

dist = df['LRR_RANGE_4'].values
    