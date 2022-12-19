test_cases = int(input())
for i in range(test_cases):
    x, y= map(int, input().split())   
    if (x-y)%2==0:
        print("Yes")
    else:
        print("No")
