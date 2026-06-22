
#Creational
#1.Singleton
class singleton:
    exists=None

    def __new__(cls,*args,**kwargs):
        if cls.exists is None:
            print("New instance")
            cls.exists=super().__new__(cls)
        return cls.exists

#2.Factory

class four_wheeler:
    def details(self):
        print("The vehicle has 4 wheels.")

class three_wheeler:
    def details(self):
        print("The vehicle has 3 wheels.")

def factory(Type):
    types={"Three wheeler":three_wheeler(),"Four Wheeler":four_wheeler()}
    return types.get(Type)

vehicle_1=factory("Three wheeler")
vehicle_1.details()
vehicle_2=factory("Four Wheeler")
vehicle_2.details()

a=singleton()
b=singleton()