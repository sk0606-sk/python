class sk:
    a=[]
    def __init__(self,name,sk,age):
        self.__name=name
        self.__age=age
        self.a.append(sk)
    @property
    def name(self):
        return self.__name
    @age.setter
    def age(self,S):
        self.__age=S

a=sk(sk,18,13)
print(a.a)
print(a.name)