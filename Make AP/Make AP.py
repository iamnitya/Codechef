n = int(input())
for i in range(n):
    a,b = input().split()
    if (int(a)+int(b))%2==0:
        print((int(a)+int(b))//2)
    else:
        print("-1")
