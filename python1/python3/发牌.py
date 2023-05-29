# import random
#
#
# class Fapai:
#
#     def zuopai(self):
#         p = []
#         zp = []
#         for i in 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K':
#             p.append(f'♦{i}')
#             p.append(f"♣{i}")
#             p.append(f"♠{i}")
#             p.append(f"♥{i}")
#         random.shuffle(p)
#         p1 = p[0:13]
#         p2 = p[13:26]
#         p3 = p[26:39]
#         p4 = p[39:]
#         zp1 = zp.append(p1)
#         zp2 = zp.append(p2)
#         zp3 = zp.append(p3)
#         zp4 = zp.append(p4)
#         xuhao = [0, 1, 2, 3]
#         x = random.choice
#         pai=zp[x]
#         del zp[x]
# class kei(Fapai):
#     def __init__(self,name):
#         self.name=name
# k=kei('sk')
# print(k.zuopai())
import random

class kehu():
    def __init__(self,name):
        self.name=name
        self.cards=[]
    def __str__(self):
        return f'{self.name}:{self.cards}'
    def add(self, card):
        self.cards.append(card)


class p:
    pai = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    hua = ['♦', '♣', '♠', '♥']
    def __init__(self):
        self.cards=[]
    def creat(self):
        for i in p.hua:
            for x in p.pai :
                self.cards.append(f'{x}{i}')
        random.shuffle(self.cards)
    def napai(self,yonghu):
        for i in range(0,13):
            topCrad = self.cards[0]
            yonghu.add(topCrad)
            self.cards.remove(topCrad)

ke=kehu('sk')
k=kehu('skk')
l=kehu('skkk')
ll=kehu('skkkk')
p1=p()
p1.creat()
p1.napai(ke)
p1.napai(k)
p1.napai(l)
p1.napai(ll)
print(p1.cards)
print(ke.__str__())
print(k.__str__())
print(l.__str__())
print(ll.__str__())








