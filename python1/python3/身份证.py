import re
print('输入身份证号')
sfz=input()
if re.match(r'[1-9]\d{5}(18|19|20){1}\d{2}([0-1]{1}[1-12]{1})([0-9]|X){1}$',sfz):
    print('符号',sfz)
else:
    print('不符合')

