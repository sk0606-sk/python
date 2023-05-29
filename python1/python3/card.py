# 定义牌类，生成牌,生成一个对象的要写什么方法？__init__()
import random
class Card():
    # 牌面数字和花色存到2个不同的列表中
    RANKS=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    SUITS=['♥','♠','♣','♦']
    def __init__(self):
        self.cards=[]

#     生成牌的方法,普通的生成牌的方法
    def create(self):
        for suit in Card.RANKS:
            for rank in Card.SUITS:
                self.cards.append(f'{suit}{rank}')
        random.shuffle(self.cards)
#         循环上面和下面的列表，组成A♥
    def deal(self,players,percard=13):
        for rounds in range(percard):
            for play in players:
                topCrad=self.cards[0]
                play.add(topCrad)
                self.cards.remove(topCrad)

class Play():
    def __init__(self,name):
        self.name=name
        self.cards=[]

    def __str__(self):
        return f'{self.name}:{self.cards}'
    # 添加牌的功能，给玩家加牌
    def add(self,card):
        self.cards.append(card)

#     添加牌的功能
if __name__=="__main__":
    play1=[]
    for i in range(4):
        play=Play(f'玩家{i}')
        play1.append(play)
    card=Card()
    card.create()
    card.deal(play1,13)
    for play in play1:
        print(play)



# card=Card()
# card.create()
# print(card.cards)



