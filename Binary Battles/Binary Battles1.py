import math
for i in range(int(input())):
    a,b,c=map(int,input().split())
    k=int(math.log(a,2))
    print(k*b+(k-1)*c)
