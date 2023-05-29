# *       j  1   i 0
# **      j  2   i 1
# ***     j  3   i 2
# ****    j  4   i 3
# *****   j  5   i 4
i = 0
while i < 5:
    j = 0
    while j < i + 1:
        print('*', end='')
        j += 1
    i += 1
    print()
