test_cases = int(input())
for j in range(test_cases):
    x,y = map(int,input().split())
    total = (x-(x//3))*y
    print(total)
