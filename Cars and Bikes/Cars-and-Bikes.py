test_cases=int(input())
for i in range(test_cases):
    n=int(input())
    if(n%2==0 and n%4!=0):
        print("YES")
    else:
        print("NO")
