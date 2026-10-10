n,k,m = map(int,input().split())
n=n*2
if n%k==0:
    s = n // k
else:
    s = (n // k) +1
print(s*m)
