sg = float(input('输入身高m'))
tz = float(input('输入体重kg'))
BMI = tz / (sg ** 2)
if BMI < 18.5:
    print("过轻")
elif 18.5 <= BMI <= 23.9:
    print('正常')
elif 24 <= BMI <= 27:
    print('过重')
elif 27 < BMI < 28:
    print('比较肥胖，可以减肥')
elif 28 <= BMI <= 32:
    print('肥胖')
else:
    print('非常肥胖')
print(BMI)
