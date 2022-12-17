test_cases = int(input())
for i in range(test_cases):
    a,b,c = list(map(int,input().split()))
    if a+(c*2)>=b:
        print("YES")
    else:
        print("NO")
