test_cases=int(input())
for i in range(test_cases):
    p=input()
    n_s=p.split(" ")
    k=int(n_s[0]) 
    l=int(n_s[1]) 
    m=int(n_s[2])
    n=int(n_s[3])
    o=int(n_s[4])
    q=int(n_s[5])
    if l>=k and n>=m and q<=o:
        print("YES")
    else:
        print("NO")
