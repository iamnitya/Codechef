t = int(input())
for i in range(t):
    l = input()
    l_s=l.split(' ')
    k=int(l_s[0])
    m=int(l_s[1])
    if (k*m)%2==0:
        print("YES")
    else:
        print("NO")
    
