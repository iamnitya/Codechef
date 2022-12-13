n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    total1 = (500-a*2)+(1000-4*(a+b))
    total2 = (500-b*4)+(1000-2*(a+b))
    if total1>total2:
        print(total1)
    else:
        print(total2)
