test_cases=int(input())
for i in range(test_cases):
    p=input()
    p_split=p.split(" ")
    n=p_split[0]
    o=int(n)
    m=p_split[1]
    s=int(m)
    t=o+s
    if(21-t>10):
        print("-1")
    else:
        print(21-t)
