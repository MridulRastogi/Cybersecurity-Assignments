def Unique():
    s = input().split()
    a = [] 
    for x in s: 
        if x not in a: 
            a.append(x) 
    for x in a: 
        print (x,end=' ')
Unique() 
