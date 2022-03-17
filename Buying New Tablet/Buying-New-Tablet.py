test_cases=int(input())
for i in range(test_cases):
    k=input()
    k_s=k.split(" ")
    number=int(k_s[0])
    max_aff=int(k_s[1])
    m=[]
    for j in range(number):
        l=input()
        l_s=l.split(" ")
        length=int(l_s[0])
        width=int(l_s[1])
        cost=int(l_s[2])
        count=0
        if cost<=max_aff:
            area=length*width
            m.append(area)
        else:
            m.append(0)
    m.sort()
    j=m[-1]
    if j>0:
        print(j)
    else:
        print("no tablet")
        
