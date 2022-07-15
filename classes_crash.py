class Car:




    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    

    def description(self):
        long_name=f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.") 
    
    def update_odometer(self, mileage):#updating method
        if mileage >= self.odometer_reading:            
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


my_new_car=Car('audi','a4','2019')
print(my_new_car.description())
my_new_car.update_odometer(23)
#my_new_car.odometer_reading = 24 #to change attribute directly 
my_new_car.read_odometer()


#for used car
my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.description())


my_used_car.update_odometer(23_500)
my_used_car.read_odometer()


my_used_car.increment_odometer(100)
my_used_car.read_odometer()



#battery class
class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self,battery_size=75):#defult value
        self.battery_size=battery_size
    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
    

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")     

class ElectricCar(Car):#child class from the parent class

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        """Then initialize attributes specific to an electric car."""
        super().__init__(make, model, year)
        #self.battery_size=75
        self.battery=Battery()
    #def describe_battery(self):
    #    print(f'this car has a {self.battery_size}-kwh battery')
         
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.description())
#my_tesla.describe_battery()
#to ovride methods from the parent class just name the function the same
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()