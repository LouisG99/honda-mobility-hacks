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
        self.nearCarsDist = [] # size 64
                # should be array of array such that 
                # index is like [obj_nbr][time_index]
        self.nearCarsAngle = [] # size 64
        self.meanSpeed = 0
        self.stdevSpeed = 0
        self.time_Index = 0
        
        
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
            dist_0 = self.nearCarsDist[i][self.time_index]
            dist_1 = self.nearCarsDist[i+1][self.time_index]
            if dist_0==0 or dist_1==0: 
                break
            else:
                angle_0 = self.nearCarsAngle[i][self.time_index]
                angle_1 = self.nearCarsAngle[i+1][self.time_index]
                
                speed = self.getSpeed(dist_0, dist_1, angle_0, angle_1)
                if speed > 8.9: # 20 mph
                    speedSum += self.getSpeed(dist_0, dist_1, angle_0, angle_1)
                    count += 1
        
        return speedSum / count
    
    def getStdevSpeed(self):
        mean = self.meanSpeed
        sumSqrd = 0
        count = 0
        
        for i in range(len(self.nearCarsAngle)-1):
            dist_0 = self.nearCarsDist[i][self.time_index]
            dist_1 = self.nearCarsDist[i+1][self.time_index]
            if dist_0==0 or dist_1==0: 
                break
            else:
                angle_0 = self.nearCarsAngle[i][self.time_index]
                angle_1 = self.nearCarsAngle[i+1][self.time_index]
                speed = self.getSpeed(dist_0, dist_1, angle_0, angle_1)
                if speed > 8.9: # 20 mph  
                    sumSqrd += (self.getSpeed(dist_0, dist_1, angle_0, angle_1))**2
                    count += 1
        
        return sumSqrd/count - mean**2
    
    def load_car_Dist(self, csv_file):
        base_flag = "LRR_RANGE_"
        for i in range(64):
            flag = base_flag + str(i)
            self.nearCarsDist[i] = df[flag].values
        return 
    
    def load_car_Angle(self, csv_file):
        base_flag = "LRR_RANGE_"
        for i in range(64):
            flag = base_flag + str(i)
            self.nearCarsAngle[i] = df[flag].values
        return        
    
    def scoreSpeed(self, speed): 
        if (speed <= self.meanSpeed + self.stdevSpeed):
            return 0
        if (speed <= self.meanSpeed + 2 * self.stdevSpeed):
            return 1
        if (speed <= self.meanSpeed + 3 *self.stdevSpeed):
            return 2
        return 3
                


def getCarNbr(col_name):
    # 2 digits vs 1 digit
    if col_name[-2].isdigit():
        return int(col_name[-2:])
    
    return int(col_name[-1])
        


def yeet():
    print("yeet")