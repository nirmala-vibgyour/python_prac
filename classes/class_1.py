# The name of the class should be in CamelCaps.
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # Adding one more attribute but not assigning it from the instance.
        self.color = " "
    
    def get_descriptive_name(self):
        long_name = str(self.year)+ " "+self.make+" "+self.model
        return(long_name.title())
    
    def update_mileage(self, mileage):
        self.odometer_reading = mileage

    def increment_mileage(self, miles):
        self.odometer_reading += miles
    
    def read_odometer(self):
        print("The car has "+str(self.odometer_reading)+" miles on it.")
    
    def got_color(self):
        print("The car got the color "+self.color.title())

my_car = Car('scorpio', 's23', 2024)
print("The car is "+my_car.get_descriptive_name())
my_car.get_descriptive_name()
my_car.read_odometer()
# Changing the value of the attribute using the method.
my_car.update_mileage(34)
my_car.read_odometer()
my_car.increment_mileage(45)
my_car.read_odometer()
# Changing th value of the attribute using the instance.
my_car.color = 'Red'
my_car.got_color()
