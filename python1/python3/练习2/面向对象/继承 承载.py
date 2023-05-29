#父类
class father:
    name='sjk'
    def speak(self):
        print('i can spenk')
class mather:
    def write(self):
        print('i can write')
class son(father,mather):
    def speak(self):
        print('ssss')     #重载父类的内容   找属性找方法 都是从自己开始找
s=son
s.name='dadadadadad'
s.speak(s)
s.write(s)
print(s.name)

