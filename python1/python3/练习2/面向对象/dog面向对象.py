class Dog:
    def __init__(self,name,nianling,shengao):
        self.name=name
        self.nianling=nianling
        self.shengao=shengao

    def jiao(self):
        print('狗叫什么')
    def pao(self):
        print(f'{self.name}别跑')
dog=Dog('小黑','1','30')
