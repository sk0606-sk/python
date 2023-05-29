#3.写一个狗类。产生10条狗（姓名，攻击力（默认5），防御力
#（默认3），血量（默认100））。然后随机从10条狗中选2条狗打架，狗的血量初始值都为100.，
# 当血量为0的时候，这条狗，死亡，清出狗的队伍。
#.直到最后一条狗，输出获胜狗的编号
import random
#写一个狗类，添加属性 姓名 攻击力 防御力 血量 并且赋予默认值
list=[]
class Gou():
    def __init__(self,name=None,shanghai=0,fangyu=0,HP=100):
        while True:
            s=random.randint(1,5)
            f=random.randint(1,3)
        self.name=name
        self.shanghia=f'{s}'
        self.fangyu=f"{f}"
        self.HP=HP

def xuangou():
    while True:
        gou1=random.choice(list1)
        gou2 = random.choice(list1)
        if  gou1==gou2:
            continue
        else:
            return gou1,gou2
def pk():
    while True:
        s = random.randint(0, 1)

#生成十条狗
list=[]
list1=[]
for t in range(0,10):
    list.append(Gou())
    list1.append(t+1)
#选狗出战，直到list1长度为1停止 十回合
for i in range(1,10):
    GO1,GO2=xuangou()
    print(f"第{i}回合:编号{list1[GO1]}VS编号{list1[GO2]}")
    death=pk(GO1+1,GO2+1)
    print(list1)
    print(f"删除狗{list1[death-1]}")
    del list1[death-1]
    del list[death-1]
print(f"狗{list1[0]}胜利,剩余血量{list[0].HP}HP")