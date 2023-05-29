wenjianming = '身份证码值对照表.txt'
with open(wenjianming, 'r', encoding='utf-8') as file:
    du = eval(file.read())
    print(du)
    print('输入前6位数字')
    a = input()
    cd = len(a)
    if cd == 6:
        for i in du:
            print(i)
            if a in i:
                print(du[a])

                break
        else:
            print(f'{a}输入有误')

    else:
        print('输入的长度有误')
