import os
if not os.path.exists('Py'):
    os.mkdir('Py')
zhuan=os.chdir("py")
liebi=os.listdir()
for i in range(1,6):
    with open(rf'python基础班-{i}.txt','w') as sk:
            pass
for i in range(1,6):
    gaiming = os.rename(rf'python基础班-{i}.txt', rf'[黑马]python基础班-{i}.txt')

