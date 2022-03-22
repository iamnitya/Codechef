t = int(input())
for i in range(t):
    x1,x2 = map(int,input().split())
    if x1-x2>=0:
        print("YES")
    else:
        print("NO")
