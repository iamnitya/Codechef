t = int(input())
for i in range(t):
    l1=input()
    l_s1=l1.split(' ')
    No_of_People=int(l_s1[0])
    Position_of_Chef=int(l_s1[1])
    Time_Vaccinate_Child=int(l_s1[2])
    Time_Vaccinate_Adult=int(l_s1[3])
    
    p=input()
    p_s=p.split(" ")
    time=0
    for i in range(Position_of_Chef):
        k=int(p_s[i])
        if k==0:
            time+=Time_Vaccinate_Child
        else:
            time+=Time_Vaccinate_Adult

    print(time)
        
