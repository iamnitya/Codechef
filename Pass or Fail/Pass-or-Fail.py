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
    p4=p1_int-p2_int
    marks=(p2_int*3)-p4
    if (marks>=p3_int):
        print("PASS")
    else:
        print("FAIL")
    

#p1=number of students(str)
#p2=questions correct(str)
#p3=pass marks(str)
#p4=incorrectquestions(int)
