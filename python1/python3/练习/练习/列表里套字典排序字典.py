
d = {'张三':23,'李四':18,'王五':20,'刘六':25}
r=sorted(d.items(),key=lambda items:items[1])
print(r)