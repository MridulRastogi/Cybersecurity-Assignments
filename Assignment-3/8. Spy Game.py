def Spy_Game():
    s = input().split()
    flag = False
    for i in range(0,len(s)-2):
        if(s[i]=='0'):
            for j in range(i+1,len(s)-1):
                if(s[j]=='0'):
                    for k in range(i+1,len(s)):
                        if(s[k]=='7'):
                            flag = True
    if(flag==True):
        print('True')
    else:
        print('False')

Spy_Game()
