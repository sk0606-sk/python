zh = input('输入账号')
mima = input('密码')
i = 3
while i > 0:
    i -= 1
    if zh == 'sk' and mima == '123456':
        print('登录成功')
        break
    else:
        print(f'用户密码错误，您还有{i}次')
        if i == 0:
            print('输入次数过多稍后执行')
            break
        zh = input('输入账号')
        mima = input('密码')
