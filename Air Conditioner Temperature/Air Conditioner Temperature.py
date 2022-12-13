n = int(input())
for i in range(n):
    a,b,c = map(int,input().split())
    if a>b or c>b:
        print("No")
    else:
        print("Yes")
