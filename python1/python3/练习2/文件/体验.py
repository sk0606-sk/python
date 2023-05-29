import time
wenjianming = '身份证码值对照表.txt'
try:
    open(fr'{wenjianming}')
except Exception as sk:
    print('异常原因',sk)
else:
    with open(rf'{wenjianming}','r',encoding='utf-8') as sk:
        try:
            du = eval(sk.read())
            print(du)
            for i in du:
                print(i)
            time.sleep(15516)

        except BaseException as sk:
            print(sk)
            print(f'错误原因',{sk})
