test_cases = int(input())
for i in range(test_cases):
    a,b = map(int,input().split())
    if a>0 and b>0:
        print("Solution")
    elif b==0:
        print("Solid")
    else:
        print("Liquid")
