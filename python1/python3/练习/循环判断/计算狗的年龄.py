dog = float(input('狗狗的年龄'))
# if dog<0 :
# print('输入不合法')
# elif dog<=2:
# dog =10.5*dog
# else :
# dog=21+((dog-2)*4)
# if dog>0 :
# print(f'狗儿的年龄相当于人的{dog}岁')
if dog > 0:
    if dog <= 2:
        dog = 10.5 * dog
    else:
        dog = 21 + ((dog - 2) * 4)
    print(f'狗儿的年龄相当于人的{dog}岁')
else:
    print('请输入一个合法的年龄!')
