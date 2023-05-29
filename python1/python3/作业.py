#3.写一个狗类。产生10条狗（姓名，攻击力（默认5），防御力
#（默认3），血量（默认100））。然后随机从10条狗中选2条狗打架，狗的血量初始值都为100.，
# 当血量为0的时候，这条狗，死亡，清出狗的队伍。
#.直到最后一条狗，输出获胜狗的编号
import random
#写一个狗类，添加属性 姓名 攻击力 防御力 血量 并且赋予默认值
class Gou():
    def __init__(self,name=None,shanghai=0,fangyu=0,HP=100):
        self.name=name
        self.shanghia=shanghai
        self.fangyu=fangyu
        self.HP=HP
def xuangou():
    while True:
        GO1=random.randint(0,len(list1)-1)
        GO2=random.randint(0,len(list1)-1)
        if GO1==GO2:
            continue
        else:
            return GO1,GO2
def pk(a,b):
    while True:
        xuel=
        s=random.randint(0,1)
        shanghai=random.randint(1,5)
        fangyu=random.randint(1,3)
        zhenshishanghai=shanghai-fangyu
        if list[a-1].HP==0:
            print(f"结果：狗{list1[a-1]}死亡")
            return a
        elif list[b-1].HP==0:
            print(f"结果：狗{list1[b-1]}死亡")
            return b
        else:
            if s==0:
                if zhenshishanghai <=0 :
                    print(f"狗{list1[a - 1]}对狗{list1[b - 1]}造成了0点伤害")
                    list[b - 1].HP -= int(zhenshishanghai)
                    print(f"狗{list1[a - 1]}：{list[a - 1].HP}HP,狗{list1[b - 1]}：{list[b - 1].HP}HP")
                elif zhenshishanghai>0:
                    print(f"狗{list1[a - 1]}对狗{list1[b - 1]}造成了{shanghai}点伤害")
                    list[b - 1].HP -= int(zhenshishanghai)
                    print(f"狗{list1[a - 1]}：{list[a - 1].HP}HP,狗{list1[b - 1]}：{list[b - 1].HP}HP")
            else:
                if zhenshishanghai<=0:
                    print(f"狗{list1[b - 1]}对狗{list1[a - 1]}造成了0点伤害")
                    list[a - 1].HP -= 0
                    print(f"狗{list1[a - 1]}：{list[a - 1].HP}HP,狗{list1[b - 1]}：{list[b - 1].HP}HP")
                elif zhenshishanghai>0:
                    print(f"狗{list1[b-1]}对狗{list1[a-1]}造成了{shanghai}点伤害")
                    list[a-1].HP-= int(zhenshishanghai)
                    print(f"狗{list1[a-1]}：{list[a-1].HP}HP,狗{list1[b-1]}：{list[b-1].HP}HP")

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






#随机生成验证码

def cID(sj):
    while True:
        for o in range(0, 6):
            k = random.randint(0, 2)
            if k == 0:
                sj += str(random.randint(0, 9))  # 数字
            elif k == 1:
                sj += chr(random.randint(65, 90))  # 大写字母
            elif k == 2:
                sj += chr(random.randint(97, 122))  # 小写字母   48-57 65-90 97-122
        b,l,n=0,0,0  #b大写字母数目 l小写字母数目 n数字数目
        for i in sj:
            if i.islower():
                l+=1
            elif i.isupper():
                b+=1
            elif i.isdigit():
                n+=1
        if b==0 or l==0 or n==0:
            continue
        else:
            return sj
sj=""
print(cID(sj))
