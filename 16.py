p=int(input())
a=str(p)
if len(a)==4 and a.count(a[0])==1 and a.count(a[1])==1 and a.count(a[2])==1 and a.count(a[3])==1 and (p<1900 or p>2050):
    print('OK')
else:
    print('ERROR')