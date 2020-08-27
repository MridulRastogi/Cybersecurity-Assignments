def Pangrams(s):
    a = [chr(x) for x in range(97,123)]
    c=0
    for i in a:
        if i not in s:
            c=c+1
    if(c==0):
        print('Pangram')
    else:
        print('Not a Pangram')
    
s = input().lower()
Pangrams(s)


