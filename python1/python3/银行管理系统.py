a = []
xinxi={}
import random
class xy:
    def __init__(self):
        print('请输入名字')
        name = input()
        self.name = name
        print('请输入身份证号')
        sf = (input())
        for i in sf:
            if 0 < i < 10:
                print('kaihushivai')
                break
            else:
                self.sfzh = sf
        print('请输入密码')
        mm = input()
        cd = len(mm)
        if 6 < cd or cd > 6:
            print('kiahuishibai')
        else:
            self.mima = mm

        preMoney = int(input("请输入您的预存款金额："))
        if preMoney < 0:
            print("预存款输入有误，开户失败......")
        else:
            self.ye = preMoney
        IDCARD = "".join(map(str, random.sample(range(0, 9), 8)))
        user = (IDCARD, self.mima, self.sfzh, self.ye)
        xinxi[f"{self.name}"]=f"{user}"
    def chaxun(self):
        print('请输入密码')
        mima=input()
        print('请输入卡号')
        kh=input()
        for i in range(3):
            b=(self.__mima,self.__kahao)
            if mima==self.__mima and kh==self.__kahao :
                print(self.__ye)
sk=xy()