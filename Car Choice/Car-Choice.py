test_cases=int(input())
for i in range(test_cases):
    n=input()
    n_s=n.split(" ")
    k=int(n_s[0]) 
    l=int(n_s[1]) 
    m=int(n_s[2])
    n=int(n_s[3])
    div1=m/k 
    div2=n/l 
    if (div1<div2):
        print(-1)
    elif (div2<div1):
        print(1)
    else:
        print(0)
