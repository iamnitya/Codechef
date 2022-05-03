test_cases = int(input())
for i in range(test_cases):
    A, B = map(int,input().split())
    if A>B:
        print("A")
    else:
        print("B")
