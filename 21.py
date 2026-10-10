s1,s2=map(str,input().split('-'))
x1 = "abcdefgh".index(s1[0]) + 1
x2="abcdefgh".index(s2[0]) + 1
y1=int(s1[1])
y2=int(s2[1])
dx=abs(x2-x1)
dy=abs(y2-y1)
if (dx==2 and dy==1) or (dx==1 and dy==2):
    print('верно')
else:
    print('ошибка')
