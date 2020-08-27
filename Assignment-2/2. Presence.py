def Presence():
    high = int(input('Enter the Upper Range : '))
    low = int(input('Enter the Lower Range : '))
    num = int(input('Enter the number to be searched for : '))
    if(num<=high & num>=low):
        print('In Range')
    else:
        print('Not in Range')
Presence()
