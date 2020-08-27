def Result():
    a = int(input("First : "))
    b = int(input("Second : "))
    if(a%2==0 and b%2==0):
        print(min(a,b))
    else:
        print(max(a,b))

Result()

