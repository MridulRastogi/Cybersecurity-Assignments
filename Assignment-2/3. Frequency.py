def Frequency():
    u=0
    l=0
    s = str(input('Enter a String : '))
    for i in range(len(s)):
        if(s[i].isupper()==True):
            u=u+1
        elif(s[i].islower()==True):
            l=l+1
    print('Frequency of UpperCase Letters : ',u)
    print('Frequency of LowerCase Letters : ',l)
Frequency()
