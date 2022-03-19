s = input()
for i in range(int(input())):
    t = input()
    for i in t:
        if i not in s:
            print('No')
            break 
    else:
        print('Yes')
