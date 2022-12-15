t = int(input())
for i in range(t):
    x,y,z= map(int,input().split())
    if y%z==0:
        k = y//z
        print(x*k)
    else:
        k = y//z+1
        print(x*k)
