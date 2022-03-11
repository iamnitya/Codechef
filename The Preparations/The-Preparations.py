test_cases=int(input())
for i in range(test_cases):
    n=input()
    n_s=n.split(" ")
    X=int(n_s[0])
    Y=int(n_s[1])
    Z=int(n_s[2])
    if X>(Y*Z):
        print("YES")
    else:
        print("NO")
