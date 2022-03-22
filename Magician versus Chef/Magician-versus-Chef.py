t = int(input())
for i in range(t):
    n,x,s = map(int,input().split())
    p = x
    for j in range(s):
        a,b = map(int,input().split())
        if p==a:
            p = b
        elif p==b:
            p =a
    print(p)
