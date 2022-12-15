n=int(input())
for i in range(n):
    p=int(input())
    if p%5==0:
        print((p//5)*4)
    else:
        print(((p//5)*4)+p%5)
