# instance Methods

# Class Methods

# Static Methods


# sample example

"""class Car:
    def sample_car_instance_method(self,a): #method define
        print(a)
carObj =Car() # object creation
carObj.sample_car_instance_method("Hello world") #Method calling

carObj1=Car()
carObj1.sample_car_instance_method(2)"""


# car problem

class car_a:
    color='red'
    max_speed=100
    #acceleration=0,
    #tyre_friction=0
    start_engine=True
    current_speed=200
    def start_Engine(self):
        self.start_engine=True
        print("The car Engine is on")

    def stop_Engine(self):
        self.start_engine=False
        print("The car Engine is off")

    """def acceleration(self,acceleration):
        self.acceleration=acceleration
        if acceleration <= self.max_speed :
            print("NORMAL SPEED")
        else:
            print(" ")"""

    def apply_Breaks(self,tyre_friction):
        self.tyre_friction= tyre_friction
        self.current_speed-=self.tyre_friction
        if self.current_speed > self.max_speed:
            self.current_spped = self.max_speed
            print("GO SLOW")
        else:
            print(self.current_speed)

    def sound_Horn(self):
        if self.start_engine == True:
            print("BEEP BEEP")
        else:
            print("Not started the car")

obj=car_a()
obj.start_Engine()
obj.stop_Engine()
#obj.acceleration(40,30)
obj.apply_Breaks(30)
obj.start_Engine()
obj.sound_Horn()



# online shopping cart












