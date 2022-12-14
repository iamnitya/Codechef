n = int(input())
for i in range(n):
    a = list(map(int,input().split()))
    if len(set(a))==4:
        print(2)
    elif len(set(a))==3:
        print(1)
    else:
        print(0)
    
        
