
class Car:
    number_of_pepole=0
    def __init__(self,renshu2):
        self.max_people=renshu2


    def set_pepole(self,renshu):
        if self.max_people > renshu:
            self.number_of_pepole=renshu
        else:
            print(f'人数超过最大乘车人数,只能是{self.max_people}')
            self.number_of_pepole=self.max_people
    def increase_pepole(self):
        if self.number_of_pepole <self.max_people:
            self.number_of_pepole+=1
            print('车上人数',self.number_of_pepole)
        else:
            print('人数已满')
    def reduce_pepole(self):
        if self.number_of_pepole <=self.max_people:
            self.number_of_pepole-=1
            print('车上人数',self.number_of_pepole)
        else:
            print('人数已满')
che1=Car(20)
che1.set_pepole(30)
che1.increase_pepole()
che1.increase_pepole()
che1.increase_pepole()
che1.increase_pepole()
che1.reduce_pepole()


