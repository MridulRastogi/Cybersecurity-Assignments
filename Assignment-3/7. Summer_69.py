def summer_69():
    s = input().split()
    sum=0
    while '6' in s:
        del s[s.index('6'):s.index('9')+1]
    for i in s:
        sum = sum + int(i)
    print(sum)
    
summer_69()
