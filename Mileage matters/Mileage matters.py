test_cases = int(input())
for j in range(test_cases):
    n,x,y,a,b = map(int,input().split())
    #cost of petrol
    p = n/a*x
    #cost of diesel
    d = n/b*y
    if p>d:
        print("DIESEL")
    elif d>p:
        print("PETROL")
    else:
        print("ANY")
