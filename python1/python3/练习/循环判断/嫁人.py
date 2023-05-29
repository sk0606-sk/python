sg = int(input('身高'))
cf = int(input('财产'))
sq = int(input('帅气值'))
if sg > 180 and cf > 1000 and sq > 500:
    print('我一定嫁给他')
elif sg > 180 or cf > 1000 or sq > 500:
    print('嫁吧，比上不足，比下有余')
else:
    print('不嫁')
