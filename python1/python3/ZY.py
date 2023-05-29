import random
class Dog:
    list=[]
    def __init__(self,name):
        self.name=name
        self.gongji=5
        self.fangyu=3
        self.xue=100
        self.list.append(self)
    def __repr__(self):
        return f'{self.name}'


    def dajia(self,dog2):
            suiji=random.randint(0,1)
            if suiji==0:
                dog2.xue-=2
                print(f'我的名字是{dog2.name}血量是{dog2.xue}')

                if dog2.xue <= 0:
                    Dog.list.remove(dog2)

            else:
                self.xue-=2
                print(f'我的名字是{self.name}血量是{self.xue}')
                if self.xue <= 0:
                    Dog.list.remove(self)

for i in range(10):
   Dog(i)
while True:
    a=random.choice(Dog.list)
    b= random.choice(Dog.list)
    a.dajia(b) #一开始我写的是Dog（）啥啥 原本a，b来源就是对象 如果加一个Dog（）那就是重新创建了一个实例 每次都重新创建一个实例 所有就是为什么血量一直是98
    if len(Dog.list)==1:
        print(Dog.list)
        break

