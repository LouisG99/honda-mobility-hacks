#Use dataset 1, by calculating speed of vehicles around and all of that
#Problem with dataset 2 is that vechicles might not be close by, 
#so might not face same conditions ... 
#no one might be driving dangerously

# dangerous one at 5:58 in video 

import json
import math

class closeCar:
    def __init__(self, distance, angle):
        self.distance = []
        self.angle = angle
        

class radarCar:
    def __init__(self, speed, time, dt):
        self.speed = speed
        self.time = time
        self.dt = dt
        self.nearCarsDist = [] # size 63
        self.nearCarsAngle = [] # size 63
        
    def getSpeed(self, dist1, dist2, angle1, angle2):
        horiz_d = math.cos(angle1)*dist1 - math.cos(angle2)*dist2
        vertical_d = math.sin(angle1)*dist1 - math.sin(angle2)*dist2
        vertical_d += self.speed * self.dt
        
        total_d = (horiz_d**2 + vertical_d**2)**0.5
        return total_d / self.dt

    def getAverageSpeed(self):
        speedSum = 0
        count = 0
        for i in range(len(self.nearCarsAngle)-1):
            dist_0 = self.nearCarsDist[i]
            dist_1 = self.nearCarsDist[i+1]
            if dist_0==0 or dist_1==0: 
                break
            else:
                angle_0 = self.nearCarsAngle[i]
                angle_1 = self.nearCarsAngle[i+1]
                speedSum += self.getSpeed(dist_0, dist_1, angle_0, angle_1)
                count += 1
        
        return speedSum / count
    
    def getStdevSpeed(self):
        
                



import pandas

#csvfile = pandas.read_csv('../autonomous-data/ordered-data.csv', encoding='utf-8')