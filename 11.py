import turtle
t=turtle.Pen()
xc=int(input())
yc=int(input())
r=int(input())
x=int(input())
y=int(input())
t.penup()
t.goto(xc,yc-r)
t.pendown()
t.circle(r)
t.penup()
t.goto(x,y)
t.pendown()
t.dot(5,'red')
d=((xc-x)**2+(yc-y)**2)**0.5
if d<r:
    print('точка внутри окружности')
elif d==r:
    print('точка на окружности')
else:
    print('точка вне окружности')
turtle.done()