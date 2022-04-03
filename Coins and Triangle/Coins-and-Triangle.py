test_cases=int(input())
for i in range(test_cases):
    k=int(input())
    n=1
    s=n*(n+1)/2
    while int(s)<=int(k):
        n+=1
        s=n*(n+1)/2
    print(n-1)
