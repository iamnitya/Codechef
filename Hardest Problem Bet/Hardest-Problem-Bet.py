test_cases=int(input())
for i in range(test_cases):
    n=input()
    k=[]
    n_s=n.split(' ')
    for i in range(len(n_s)):
        a=int(n_s[i])
        k.append(a)
    k.sort()
    p=k[0]
    g=n_s.index(str(p))
    if (g==0):
        print("Draw")
    elif (g==1):
        print("Bob")
    else:
        print("Alice")
