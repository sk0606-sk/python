b1 = float(input('边1'))
b2 = float(input('边2'))
b3 = float(input('边3'))
if b1 + b2 > b3 and b1 + b3 > b2 and b2 + b3 > b1:
    print(f'是三角形')
else:
    print(f'不是三角形')
