print('验票')
print('买了票是1，没有买是0')
p = int(input('1或0 '))
if p == 1:
    print('进行安检')
    print('安检正常为1，不正常为0')
    a = int(input('1或0 '))
    if a == 1:
        print('没有携带危险品上车')
    else:
        print('携带危险品，不允许上车')
else:
    print('没有买票不允许进站')
