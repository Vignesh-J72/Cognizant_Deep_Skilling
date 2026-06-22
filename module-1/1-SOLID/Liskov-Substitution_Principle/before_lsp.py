class Car:
    def refuel(self):
        print("The vehicle is being refuelled.")
    
    def drive(self):
        print("The vehicle is being driven.")

class EVCar(Car):
    def refuel(self):
        print("Cannot put fuel in an electrical vehicle.")

class DieselCar(Car):
    pass

if __name__=="__main__":
    car_1=EVCar()
    car_2=DieselCar()
    car_1.refuel() #Not possible
    car_2.refuel()