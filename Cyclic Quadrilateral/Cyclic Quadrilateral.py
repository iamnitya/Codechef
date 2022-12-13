n = int(input())
for i in range(n):
    a,b,c,d = map(int,input().split())
    A = a+c
    B = b+d 
    # C = a+b
    # D = c+d 
    # E = a+d 
    # F = b+c 
    if A==180 and B==180:
        print("YES")
    # elif C ==180 and D==180:
    #     print("YES")
    # elif E==180 and F==180:
    #     print("YES")
    else:
        print("NO")
        
