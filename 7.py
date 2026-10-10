b=int(input())
b1=b//1000
b=b%1000
b2=b//100
b=b%100
b3=b//10
b4=b%10
if b1==b4 and b2==b3:
    print('настоящее')
else:
    print('кривое')