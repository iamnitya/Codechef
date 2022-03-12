test_cases=int(input())
for i in range(test_cases):
    p=input()
    k=p.split(" ")
    a=int(k[0])
    b=int(k[1])
    c=int(k[2])
    d=int(k[3])
    m=c//a
    n=d//b
    print(m+n)
