test_cases = int(input())
for i in range(test_cases):
    x = list(input())
    if x==x[::-1]:
        print("wins")
    else:
        print("loses")
