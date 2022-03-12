n=int(input())
for i in range(n):
    p=input()
    k=p.split(" ")
    a=int(k[0])
    b=int(k[1])
    c=a+b
    if c<3:
        print(1)
    elif 3<=c<=10:
        print(2)
    elif 11<=c<=60:
        print(3)
    else:
        print(4)
