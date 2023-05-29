x = int(input('边一'))
y = int(input('边二'))
z = int(input('边三'))
q = (x + y + z) / 2
s = (q * (q - x) * (q - y) * (q - z)) ** 0.5
print(s)
