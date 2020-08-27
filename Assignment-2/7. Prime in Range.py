def Prime(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c=c+1
    if(c==2):
        return 'Prime'
    else:
        return 'Not Prime'
            
n = int(input('Enter Limit : '))
res = [(i,Prime(i)) for i in range(2,n+1)]
print(res)
