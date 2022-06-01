for i in range(int(input())):
    a,b = map(int,input().split())
    if b==1:
        if(a%2==1):
            print("ODD")
        else:
            print("EVEN")
    elif b==2:
        print("ODD")
    else:
        print("EVEN")
