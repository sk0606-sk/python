sum = 0
for a in range(1, 10001):
    for x in range(1, a + 1):
        if x <= a:
            if a % x == 0:
                sum += x
                if a == x:
                    sum = sum - x
                    if sum == a:
                        print(f'{a}是完全数')
                        sum -= sum
                    else:
                        sum -= sum
