a,b,c = map(int,input().split())
runs = (20-b)*6*6
if c+runs>a:
    print("YES")
else:
    print("NO")
