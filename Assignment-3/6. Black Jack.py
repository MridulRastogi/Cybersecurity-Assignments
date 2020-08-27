def blackjack(a,b,c):
    s=a+b+c
    if((a==11 or b==11 or c==11) and (s>21)) :
        s=s-10
        print(s)
    elif(s>21):
        print('BUST')
    elif(s<=21):
        print(s)
    
a = int(input('First : '))
b = int(input('Second : '))
c = int(input('Third : '))
blackjack(a,b,c)
