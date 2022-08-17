from loguru import logger
import time

class DroneLocator:
    def __init__(self,time_in_flight:int):
        self.time_in_flight = time_in_flight  
        
        self.r = 0
        self.upConst = 1
        self.leftIncrement = 1
        self.rightIncrement = 2
        
        self.downIncrement = 1
        self.upIncrement = 2
        
        self.leftConst = 1
        
        self.xCurrentPosition = 1
        self.yCurrentPosition = 1
        
        self.run_time = None
    
    def findDrone(self):
        self.__drone_moves()
        return f"X Metres Left:{self.xCurrentPosition} \nY Metres Left:{self.yCurrentPosition} \nelapsed time in millis:{self.run_time} "
        
    def __drone_moves(self):
        start_time = time.time()
        while(self.time_in_flight <= self.r):
            self.yCurrentPosition = self.yCurrentPosition + self.upConst
            self.r = self.r + self.upConst
                
            if self.r > self.time_in_flight:
                difference = self.r - self.time_in_flight
                self.yCurrentPosition = self.yCurrentPosition - difference
                break

            self.xCurrentPosition = self.xCurrentPosition + self.leftIncrement
            self.r = self.r + self.leftIncrement      
            self.leftIncrement = self.leftIncrement + 2
            
            if self.r > self.time_in_flight:
                difference = self.r - self.time_in_flight;
                self.xCurrentPosition = self.xCurrentPosition - difference;
                break
            
            self.yCurrentPosition = self.yCurrentPosition - self.downIncrement
            self.r = self.r + self.downIncrement;
            self.downIncrement = self.downIncrement +2
            
            if self.r > self.time_in_flight: 
                difference = self.r - self.time_in_flight
                self.yCurrentPosition = self.yCurrentPosition+ difference;
                break
            
            self.xCurrentPosition = self.xCurrentPosition + self.leftConst
            self.r = self.r + self.leftConst
            
            if self.r > self.time_in_flight:
                difference = self.r - self.time_in_flight
                self.xCurrentPosition = self.xCurrentPosition - difference
                break

            self.yCurrentPosition = self.yCurrentPosition+ self.upIncrement
            self.r = self.r + self.upIncrement
            self.upIncrement = self.upIncrement + 2
            
            if self.r > self.time_in_flight:
                difference = self.r - self.time_in_flight
                self.yCurrentPosition = self.yCurrentPosition - difference;
                break
                

            self.xCurrentPosition = self.xCurrentPosition - self.rightIncrement;
            self.r = self.r + self.rightIncrement;
            self.rightIncrement = self.rightIncrement + 2
            
            if self.r > self.time_in_flight:
                difference = self.r - self.time_in_flight
                self.xCurrentPosition = self.xCurrentPosition + difference;
                break
        stop_time = time.time()
        self.run_time = stop_time - start_time


if __name__ == '__main__':
   
    drone = DroneLocator(1)    
    print(drone.findDrone())


        
        
            

    
        