print('假设汽车有i辆，那么模特有48-i辆')
print('汽车轮子有4i，摩托就有（48-i）*3')
for i in range(1,49):
    if i*4+(48-i)*3==172:
        print(f'汽车有{i}辆，摩托有{48-i}辆')

print('商康')