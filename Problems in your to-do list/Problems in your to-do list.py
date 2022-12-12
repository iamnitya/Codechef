n = int(input())
for i in range(n):
    p = int(input())
    m = list(map(int,input().split(" ")))
    count = 0
    for i in m:
        if i>=1000:
            count+=1
    print(count)
