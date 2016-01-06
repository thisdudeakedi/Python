

 
class Car:
    bmw_x6 = Car(model='BMW X6', max_speed=230)
    
    def __init__(self,model,max_speed):
        self.model=model
        self.max_speed=max_speed
        self.speed=0

    def accelerate(self,speed_difference):
        self.speed+=abs(speed_difference)
        self.speed=min(self.speed,self.max_speed)

    def slow_down(self,speed_difference):
        self.speed-=abs(speed_difference)
        self.speed=max(self.speed,-5)

bmw_x6.accelerate(30)
