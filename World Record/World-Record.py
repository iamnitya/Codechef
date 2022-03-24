t = int(input())
for i in range(t):
    k1, k2, k3, v = map(float,input().split())
    p=k1*k2*k3*v
    j=round(100/p,2)
    if j<9.58:
        print("YES")
    else:
        print("NO")
