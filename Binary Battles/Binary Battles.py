k = int(input())
for i in range(k):
    a,b,c = map(int,input().split())
    div = a//2
    i = 1
    while div>1:
        div = a//2
        a = a//2
        i += 1
    j = i-1
    p = (b*j)+(c*(j-1))
    print(p)
