w = '618e25a2590f76045.jpg'
with open(w, 'rb') as sk:
    duqu = sk.read()
    cd = int(len(duqu) // 2)
    yiban = duqu[0:cd]
    print(yiban)
    with open('618e25a2590f76045.jpg备份.jpg', 'wb') as skk:
        skk.write(yiban)
