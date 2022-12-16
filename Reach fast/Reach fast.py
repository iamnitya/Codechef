t = int(input())
for i in range(t):
    x,y,z = map(int,input().split())
    k = abs(x-y)
    if k%z==0:
        print(k//z)
    else:
        print(k//z+1)
