#multiple inheritance
class car_names:
    def car1(self):
        print("benz:costly car")
    def car2(self):
        print("ford:affordale car")
class bike_names:
    def bike1(self):
        print("ktm:fastest bike")
    def bike2(self):
        print("hero honda:affordable")
class vehicles(car_names,bike_names):
    def info(self):
        print("this is the vehicles information")


vehicle_info=vehicles()
vehicle_info.info()
vehicle_info.car1()
vehicle_info.car2()
vehicle_info.bike1()
vehicle_info.bike2()
