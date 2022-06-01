for i in range(int(input())):
    a,b = map(int,input().split())
    diff = (b-a)
    if diff == 1:
        print(1)
    elif diff == 0:
        print(0)
    elif diff>1:
        print(diff)
    elif diff<0 and diff%2==1:
        print(abs(diff)//2+2)
    elif diff<0 and diff%2==0:
        print(abs(diff//2))
