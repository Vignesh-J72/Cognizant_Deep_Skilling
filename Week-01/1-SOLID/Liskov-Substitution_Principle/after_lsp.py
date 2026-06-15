class DriveCar:
    def drive(self):
        print("The car is being driven.")

class FuelCar(DriveCar):
    def refuel(self):
        print("The vehicle is being refuelled.")
class EVCar(DriveCar):
    def charge(self):
        print("Charging the batteries.")

class DieselCar(FuelCar):
    pass

class ElectricCar(EVCar):
    pass

if __name__=="__main__":
    car_1=ElectricCar()
    car_2=DieselCar()
    car_1.charge() #Not possible
    car_2.refuel()