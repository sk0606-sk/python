n=int(input('输入层数'))
print(2**n-1)
def hanruota(n,x,y,z):
    if n==1 :
        print(x,'到',z)
    else :
        hanruota(n-1,x,z,y)
        print(x,'到',z)
        hanruota(n-1,y,x,z)
hanruota(n,'a','b','c')

