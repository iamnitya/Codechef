t = int(input())
for i in range(t):
    x = list(map(int,input().split()))
    x.sort()
    p = x[1]+x[2]
    print(p)
    
