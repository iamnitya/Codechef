test_cases = int(input())
for i in range(test_cases):
    m = int(input())
    p = list(map(int, input().split()))
    sum = 0
    for j in range(m):
        sum+=int(p[j])
    if sum%2 == 0:
        print("NO")
    else:
        n=sum//2
        if n+n+1 == sum:
            print("YES")
        else:
            print("NO")
        
