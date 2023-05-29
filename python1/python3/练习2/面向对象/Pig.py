class Pig:
    def __init__(self,name,weight):
        self._name=name
        self._weight=weight
    def show(self):
        print(f'{self._name},{self._weight}')
    def run(self):
        print(f'xx:没吃过猪肉，看看猪跑')

zhu1=Pig('YYX','10')
zhu2=Pig('YY','16')
zhu3=Pig('YX','15')
zhu1.show()
zhu1.run()
