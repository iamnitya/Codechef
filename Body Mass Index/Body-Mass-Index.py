n=int(input())
for i in range(n):
    p=input()
    k=p.split(" ")
    a=int(k[0])
    b=int(k[1])
    c=a//(b**2)
    if c<=18:
        print(1)
    elif 19<=c<=24:
        print(2)
    elif 25<=c<=29:
        print(3)
    else:
        print(4)
