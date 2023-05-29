import random

print('字符串')
a = list(input())
print(a, '打乱前')
b = random.shuffle(a)
print(a, '打乱后')
print('=' * 20)
print('验证码为')
for i in range(4):
    c = random.choice(a)
    print(f'{c}', end='')
