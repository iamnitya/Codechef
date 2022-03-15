t = int(input())
for i in range(t):
    l = list(map(int,input().split()))
    if l[0:2] == l[2:4] or l[0:2] == l[2:4][::-1]:
        print(1)
    elif l[0:2] == l[4:7] or l[0:2] == l[4:7][::-1]:
        print(2)
    else:
        print(0)
