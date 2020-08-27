def Number_Of_Primes():
    n = int(input("Enter the Limit : "))
    d=0
    for i in range(2,n+1):
        c=0
        for j in range(2,i):
            if(i%j==0):
                c=c+1
        if(c==0):
            d=d+1
    print(d)

Number_Of_Primes()
            
