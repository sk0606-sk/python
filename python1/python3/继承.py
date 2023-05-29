class Animal:
    def __init__(self,name):
        self.__name=name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name=name
    print('动物')
    def run(self):
        print('跑起来')
sk=Animal('skkk')
print(sk.name)
sk.name='llll'
print(sk.name)
class Horse(Animal):
    print('maam')
    def run(self):
        print('迈着矫健的步伐')
    def eat(self):
        print('马吃东西')
    def __init__(self,name):
        self.name=name
class SwifHorse(Horse):
    def __init__(self,name):
        super().__init__(name)
        self.name='千里马'
    print('是拥有动物和马的所以属性')
    def __repr__(self):
        return self
class Donkey(Animal):
    def run(self):
        print('跑起来')
    def eat(self):
        print('驴吃东西')
    super.__init__

class Mule(Donkey,Horse):#多继承是从左往右
    def __init__(self):
        self.name='骡子'
sk=Donkey('llslsl')
print(sk.name)
print(issubclass(Mule,object))