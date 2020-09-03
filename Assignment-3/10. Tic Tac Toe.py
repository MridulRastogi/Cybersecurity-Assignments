import winsound as ws
def out(a):
    print("_______________")
    print("|",a[0][0],"|",a[0][1],"|",a[0][2],"|")
    print("--------------")
    print("|",a[1][0],"|",a[1][1],"|",a[1][2],"|")
    print("--------------")
    print("|",a[2][0],"|",a[2][1],"|",a[2][2],"|")
    print("_______________")

def run():
    for i in range(1,2):
        ws.Beep(1600, 100)
        ws.Beep(1595, 200)
        ws.Beep(1590, 300)
        ws.Beep(1585, 400)
        ws.Beep(1400, 300)
        ws.Beep(1405, 200)
        ws.Beep(1410, 150)
        ws.Beep(1200, 250)
        ws.Beep(1100, 300)
        ws.Beep(1000, 400)

def check(a,ch):
    c=0;
    if(c!=1):
        for i in range(0,3):
            if(a[i][0]==ch and a[i][1]==ch and a[i][2]==ch):
                c=1
        if(c!=1):
            for i in range(0,3):
                if(a[0][i]==ch and a[1][i]==ch and a[2][i]==ch):
                    c=1
            if(c!=1):
                if(a[0][0]==ch and a[1][1]==ch and a[2][2]==ch):
                    c=1
                if(c!=1):
                    if(a[2][0]==ch and a[1][1]==ch and a[0][2]==ch):
                        c=1
    return c;

def check_draw(a):
    c=0
    for i in range(0,3):
        for j in range(0,3):
            if(a[i][j]=='X' or a[i][j]=='O'):
                c=c+1
    return c;

def position_filling(a,choice,ch):
    if choice==1:
        a[2][0] = ch
    elif choice==2:
        a[2][1] = ch
    elif choice==3:
        a[2][2] = ch
    elif choice==4:
        a[1][0] = ch
    elif choice==5:
        a[1][1] = ch
    elif choice==6:
        a[1][2] = ch
    elif choice==7:
        a[0][0] = ch
    elif choice==8:
        a[0][1] = ch
    elif choice==9:
        a[0][2] = ch
    else:
        print('INVALID CHOICE! Now your turn has skipped!')

print('Choose your marking block by the given reference : ')
print("7 | 8 | 9")
print("----------")
print("4 | 5 | 6")
print("----------")
print("1 | 2 | 3")
a = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']] 
p = input('Who Wants To Mark First (X or O) : ')
if p=='X':
    c = -1
else:
    c = 0
m=0
while(m!=1):
    c = c+1
    choice = 0
    if(c%2==0):
        while(choice<1 or choice>9):
            choice = int(input('\nEnter the position of X according to the reference : '))
        position_filling(a,choice,'X')
        m = check(a,'X')
        out(a)
        if(m==1):
            print('\nCongratulations...Player X Wins!!!\n')
            run() 
            exit()
        if(check_draw(a)==9 and m!=1):
            print("GAME IS DRAW")
            m = 1
    elif(c%2==1):
        choice = 0
        while(choice<1 or choice>9):
            choice = int(input('\nEnter the position of O according to the reference : '))
        position_filling(a,choice,'O')
        m = check(a,'O')
        out(a)
        if(m==1):
            print('\nCongratulations...Player O Wins!!!\n')
            run() 
            exit()
        if(check_draw(a)==9 and m!=1):
            print("GAME IS DRAW")
            m = 1
