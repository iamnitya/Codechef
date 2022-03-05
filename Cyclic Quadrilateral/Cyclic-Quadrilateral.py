test_cases=int(input())
for i in range(test_cases):
    p=input()
    p_split=p.split(" ")
    p1=p_split[0]
    p1_int=int(p1)
    p2=p_split[1]
    p2_int=int(p2)
    p3=p_split[2]
    p3_int=int(p3)
    p4=p_split[3]
    p4_int=int(p4)
    if(p1_int+p3_int==180 and p2_int+p4_int==180):
        print("YES")
    else:
        print("NO")
