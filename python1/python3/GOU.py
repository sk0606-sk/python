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
            gj=self.gongji-dog2.fangyu
            if (dog2.xue-gj)>0:
                dog2.xue=dog2.xue-gj
                print(f"{dog2.name}受到攻击，血量{dog2.xue}")
            else:
                dog2.xue=0
                print(f'{dog2.name}血量为0')
                Dog.list.remove(dog2)
for i in range(10):
   Dog(i)
while True:
    a=random.choice(Dog.list)
    b= random.choice(Dog.list)

    a.dajia(b)
    if len(Dog.list)==1:
    
        print(Dog.list[0],'获胜')
        break
