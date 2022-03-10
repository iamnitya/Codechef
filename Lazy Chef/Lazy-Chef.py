test_cases=int(input())
for i in range(test_cases):
    r=input()
    r_s=r.split(" ")
    x=int(r_s[0])
    m=int(r_s[1])
    d=int(r_s[2])
    if ((x*m)>=(x+d)):
        print(x+d)
    else:
        print(x*m)
