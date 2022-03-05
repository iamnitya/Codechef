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
    diff1=abs(p1_int-p3_int)
    diff2=abs(p2_int-p4_int)
    print(max(diff1,diff2))
