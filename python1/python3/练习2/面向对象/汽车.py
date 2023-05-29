class Car:
    def __init__(self,name,borand):
        self._name=name
        self._borand=borand


    def show(self):
        return self._name
        return self._borand

    def run(self):
        return print(f'汽车{self._name}跑起来了')
dazho=Car('大众','小轿车')
huoche=Car('大奔','SUV')
print(dazho.show())
print(dazho.show())
print(huoche.show())
print(huoche.show())
dazho1=Car('大众','小轿车1')
dazho2=Car('大众','小轿车2')
dazho3=Car('大众','小轿车3')
dazho4=Car('大众','小轿车4')
dazho5=Car('大众','小轿车5')
print(dazho1.show())
print(dazho2.show())
print(dazho3.show())
print(dazho4.show())
print(dazho5.show())
