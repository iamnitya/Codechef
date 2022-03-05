test_cases=int(input())
for i in range(test_cases):
    p=int(input())
    if p%10==0:
        print(int(p/10))
    else:
        print((p//10)+1)
