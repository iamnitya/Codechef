test_cases=int(input())
for i in range(test_cases):
    no_of_women=int(input())
    p=input()
    p_split=p.split(" ")
    count=0
    for i in range(no_of_women):
        a=p_split[i]
        a_int=int(a)
        if 10<=a_int<=60:
            count+=1
    print(count)
