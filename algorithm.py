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

