t = int(input())
for i in range(t):
    n,k,x,y= map(int,input().split())
    total1 = (k*x)+(n-k)*y  
    total2 = n*x
    if total1>total2:
        print(total2)
    else:
        print(total1)
