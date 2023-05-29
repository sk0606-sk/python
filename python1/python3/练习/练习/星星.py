def xx():
    print('*'*10)
def hs(i):
    for x in range(1,i+1):
        xx()
    return hs
hs(10)