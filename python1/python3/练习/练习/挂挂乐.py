import random

# gjq=['谢谢惠顾','一等奖','谢谢惠顾','谢谢惠顾','三等奖','谢谢惠顾','三等奖','二等奖',]
# s=random.choice(gjq)
# print(s)

xz = int(input('选择1-8中的一个刮奖区 '))
if 0 < xz <= 8:
    indxe = xz - 1
    gjq = ['谢谢惠顾', '一等奖', '谢谢惠顾', '谢谢惠顾', '三等奖', '谢谢惠顾', '三等奖', '二等奖', ]
    print(gjq)
    random.shuffle(gjq)
    print('打乱后')
    print(gjq)
    s = gjq[indxe]
    print('-' * 40)
    print('抽奖结果为')
    print(s)
else:
    print('输入有误')
