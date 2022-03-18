import math
test_cases=int(input())
for i in range(test_cases):
    n=input()
    n_s=n.split(" ")
    number_of_num=int(n_s[0])
    l=[]
    for j in range(1,number_of_num+1):
        p=int(n_s[j])
        l.append(p)
    def gcd (a,b):
        if (b == 0):
            return a
        else:
            return gcd (b, a % b)

    res = l[0]
    for c in l[1::]:
        res = gcd(res , c)
    m=[]
    for j in range(1,number_of_num+1):
        q=int(n_s[j])//res
        print(q,end=" ")
    print()
