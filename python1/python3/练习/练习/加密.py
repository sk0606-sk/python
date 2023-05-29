#先打开一个文件
a=list()
sk='words_file.txt'
dakai=open(sk,'a')
du=open(sk,'r')
du1=du.read()
for s in du1 :
    a.append(s)
cd=len(a)
print(a)
for i in range(cd):
    if 'a'<=a[i]<='z':
        if a[i]=='z':
            a[i]='a'
        else:
            a[i] = chr(ord(a[i])+1)
    elif 'A'<=a[i]<='Z':
        if a[i] == 'Z':
            a[i] == 'A'
        else:
            a[i] = chr(ord(a[i])+1)
print(a)
new_file= '../循环判断/new_file.txt'
new_file1=open(new_file,'w')
for i in a:
    new_file1.write(i)
du.close()
new_file1.close()


