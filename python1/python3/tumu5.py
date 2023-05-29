class Animal:
    print('动物')
    def run(self):
        print('1跑起来')
class Cat(Animal):
    def __init__(self):
        self.__name='珀斯猫'
    def run(self):
        print('2跑起来')
    def eat(self):
        print('吃起来')
class Dog(Animal):
    def __init__(self):
        self.__name='京巴狗'
    def run(self):
        print('3跑起来')
A=Animal()
def letRun(A):
    A.run()
letRun(A)