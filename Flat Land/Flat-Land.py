t = int(input())
for i in range(t):
    n = int(input())
    count=0
    while(n>=1):
        value = int(n**0.5)
        count +=1
        n -= value**2
    print(count)
