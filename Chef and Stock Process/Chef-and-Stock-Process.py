for i in range(int(input())):
    m,n,o,p=map(int,input().split())
    t=m+(m*p/100)
    if n<=t<=o:
        print("Yes")
    else:
        print("No")
