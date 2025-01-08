def add(*args):
    soma=sum(args)
    return soma



print(add(1,2,3,4))
def calculate(n,**kargs):
    print(kargs)
    n+=kargs["add"]
    n*=kargs["multiply"]
    print(n)

calculate(2,add=3,multiply=2)

class Car:
    def __init__(self,**kw):
        self.make=kw.get("make")
        self.model=kw.get("model")


my_car=Car(make="Nissan", model="GT- R")
print(my_car.model)