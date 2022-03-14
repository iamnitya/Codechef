test_cases=int(input())
for i in range(test_cases):
    n=int(input())
    if 1<=n<100:
        print("Easy")
    elif 100<=n<200:
        print("Medium")
    else:
        print("Hard")
