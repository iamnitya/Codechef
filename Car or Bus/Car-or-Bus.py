test_cases=int(input())
for i in range(test_cases):
    p=input()
    p_split=p.split(" ")
    n=p_split[0]
    o=int(n)
    m=p_split[1]
    s=int(m)
    if o>s:
        print("CAR")
    elif(s>o):
        print("BIKE")
    else:
        print("SAME")
