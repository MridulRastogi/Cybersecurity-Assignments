def Pascal(n) : 	
    for i in range(0, n) :           #For Lines
        for k in range(n-1-i):       #For Spaces
            print(' ',end=' ')
        for j in range(0,i+1):   #For Line Elements
            print(BinomialCoeff(i,j),' ',end='') 
        print() 
	
def BinomialCoeff(n,k): 
    res = 1
    if (k>n-k) : 
        k=n-k 
    for i in range(0,k): 
        res = res*(n-i) 
        res = res//(i+1) 
    return res 

n = int(input('Enter Range : '))
Pascal(n) 


