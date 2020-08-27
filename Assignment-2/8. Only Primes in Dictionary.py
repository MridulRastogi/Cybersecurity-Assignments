def Prime(n):
    c=0
    for i in range(2,n):
        if(n%i==0):
            c=c+1
    if c==0:
        return 'Prime'
    else:
        return 'Not Prime'

n = int(input('Enter Limit : '))
d = {}
d = {i:Prime(i) for i in range(2,n+1) if Prime(i)=='Prime'}
print(d)
