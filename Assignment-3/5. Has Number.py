def has_number():
    n = input().split()
    flag = False
    for i in range(0,len(n)-1):
        if(int(n[i])==3 and int(n[i+1])==3):
            flag = True
    print(flag)

has_number()
