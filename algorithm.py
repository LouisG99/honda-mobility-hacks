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

csv2 = pd.read_csv('usable_data.csv', encoding='utf-8')
df2 = pd.DataFrame(csv2)


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
    
    
    