hl = input('海里')
al = input('公里')
print(f'{hl}={al}*1.852')

name = 'sk'
age = 123
print(f'姓名{name},年龄{age}')
print(type(name))
print(type(age))
print('hello world')

xy = input('你的姓名')
age = input('你的年龄')
print(f'你的姓名{xy},你的年龄{age}')

hl = input('海里')
al = input('公里')
c = float(al) / 1.852
print(c)

kg = float(input('体重kg'))
sg = float(input('身高m'))
sg2 = sg * sg
BMI = kg / sg2
print(f'BMI是{BMI}')

s1 = float(input('输入第一个数'))
s2 = float(input('输入第二个数'))
h = s1 + s2
c = s1 - s2
s = s1 / s2
j = s1 * s2
print(f'和{h},差{c},积{j},商{s}')
