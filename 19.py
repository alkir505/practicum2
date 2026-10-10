n,m = map(int, input().split('x'))
k=int(input())
r=0
for a in range(1,n):
    if a*m==k or (n-a)*m==k:
        r=r+1
for b in range(1,m):
    if b*n==k or (m-b)*n==k:
        r=r+1
if r!=0:
    print('успешно')
else:
    print('неосуществимо')


