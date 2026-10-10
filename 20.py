a=input()
if a[0] in 'aceg' and int(a[1])%2==1:
    print('черный')
elif a[0] in 'aceg' and int(a[1])%2==0:
    print('белый')
elif a[0] in'bdfh' and int(a[1])%2==0:
    print('черный')
else:
    print('белый')