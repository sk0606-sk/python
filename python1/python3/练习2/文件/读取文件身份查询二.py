wenjianming = '身份证码值对照表.txt'
class yichang :
    pass
try:
    open(rf'{wenjianming}')
except Exception as sk:
    print('异常原因',sk)
else:
    with open(wenjianming, 'r', encoding='utf-8') as file:
        du = eval(file.read())
        print(du)
        print('输入前6位数字')
        a = input()

        if a in du:
            print(du[a])

