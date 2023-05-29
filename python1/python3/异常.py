import time
while True:
    try:
        x = int(input('输入x的值'))
        y = int(input('输入y的值'))
    except BaseException as sk:
        print(sk)
    try:
        print(x / y)
        break
    except BaseException as s:
        print(s)
        try:
            print('你有3秒时间考虑是否手动跳出改程序，如果需要跳出请安ctrl+F2')
            time.sleep(3)
        except BaseException as a:
            print({a})
            print('已经退出程序')
            break

