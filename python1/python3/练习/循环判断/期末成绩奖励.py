cj = int(input('输入期末成绩'))
if 0 <= cj <= 100:
    if cj == 100:
        print('奖励BWM')
    elif 80 <= cj <= 99:
        print('奖励台iphone')
    elif 60 <= cj <= 79:
        print('奖励参考书')
    else:
        print('什么奖励都没有')
else:
    print('请输入正确的内容')
