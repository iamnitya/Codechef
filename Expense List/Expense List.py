n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    total = int(2**b)
    for j in range(a,0,-1):
        total = total-int(total//2)
    print(total)
