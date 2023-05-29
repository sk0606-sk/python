class  People:
    def __init__(self,age):
        self.__age=age
    @property
    def age(self):
        return self.__age
    @age.setter
    def ag(self,ag):
        if  age >100 or age<0 :
            print('年龄修改有误')
        else:
            self.__age=age
            print(self.__age)
r=People(18)

print(r.age)
print(r.ag)