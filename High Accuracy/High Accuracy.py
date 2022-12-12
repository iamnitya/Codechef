n = int(input())
for i in range(n):
    p = int(input())
    if p%3==0:
        print(0)
    else:
        print(3-(p%3))
