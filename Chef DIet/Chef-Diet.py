t = int(input())
for i in range(t):
    l1=input()
    l_s1=l1.split(' ')
    No_of_Days=int(l_s1[0])
    Weight_per_day=int(l_s1[1])
    p=input()
    p_s=p.split(" ")
    rem=0
    for i in range(No_of_Days):
        b=int(p_s[i])+rem
        if (b<Weight_per_day):
            a=False
            break
        else:
            a=True
        rem=b-Weight_per_day 
    if a==True:
        print("YES")
    else:
        print("NO",i+1)
