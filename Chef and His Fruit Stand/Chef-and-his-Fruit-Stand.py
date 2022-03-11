test_cases=int(input())
for i in range(test_cases):
    n=input()
    n_s=n.split(" ")
    X=int(n_s[0])
    Y=int(n_s[1])
    if (X/2)<Y:
        print(int(X//2))
    else:
        print(Y)
