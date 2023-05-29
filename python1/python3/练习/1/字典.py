s=dict()
s['name']=123
s.update(address='nx')
s.update(电话号码='15084852626')
s.update(学校='湖南化工职业技术学院')
print(s)
del s ['name']
print()
s.pop('address')
print(s)
print(s.items())
print(s.values())
print(s.keys())
print(s.get('sk'))
for i in s.keys():
    print(i)
