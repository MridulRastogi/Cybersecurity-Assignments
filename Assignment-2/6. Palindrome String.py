def Palindrome():
    s=input()
    rev = s[::-1]
    if(s==rev):
        print('Palindrome String')
    else:
        print('Not a Palindrome String')

Palindrome()
