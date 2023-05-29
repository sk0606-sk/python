# n=1 #定义初始值
# while n<=5 :   #循环条件
#     print(n) #循环体
#     n+=1
# #自增量 确保不是死循环
# else:
#     print(132,end='')
# if zbz is True :
#     lieb=os.listdir()
#     print(lieb)
#     for i in lieb:
#         x = i.rfind('.')
#         hocuim = i[x + 1:]
#         print('''
#         请做出选择
#         1.docx文件
#         2.xlsx
#         3.其他文件
#         ''')
#         xz=input()
#         if xz=='1':
#             if hocuim == 'docx':
#                 shutil.move(f'{i}', f'{shuru}')
#         elif xz=='2':
#             if hocuim == 'xlsx':
#                 shutil.move(f'{i}', f'{shuru}')
#         elif xz == '3':
#             if hocuim!='docx' or hocuim!='xlsx':
#                 shutil.move(f'{i}', f'{shuru}')
#         else:
#             print('选择有误')
#
# else:
#     lieb = os.listdir()
#     print(lieb)
#     for i in lieb :
#         x = i.rfind('.')
#         hocuim = i[x + 1:]
#         print('''
#                    请做出选择
#                    1.docx文件
#                    2.xlsx
#                    3.其他文件
#                    ''')
#         xz = input()
#
#         if xz == '1':
#             if hocuim == 'docx':
#                 print('创建文件夹')
#                 shuru = input()
#                 cj = os.mkdir(shuru)
#                 shutil.move(f'{i}', f'{shuru}')
#                 break
#         elif xz == '3':
#             if hocuim == 'xlsx':
#                 print('创建文件夹')
#                 shuru = input()
#                 cj = os.mkdir(shuru)
#                 shutil.move(f'{i}', f'{shuru}')
#                 break
#         elif xz == '4':
#             if hocuim != 'docx' or hocuim != 'xlsx':
#                 print('创建文件夹')
#                 shuru = input()
#                 shutil.move(f'{i}', f'{shuru}')
#                 break
#         else:
#             print('选择有误')
#
#
#
#
#
