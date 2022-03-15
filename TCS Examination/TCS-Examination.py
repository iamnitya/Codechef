t = int(input())
for i in range(t):
    l1=input()
    l_s1=l1.split(' ')
    DSA1=int(l_s1[0])
    TOC1=int(l_s1[1])
    DM1=int(l_s1[2])
    l2=input()
    l_s2=l2.split(' ')
    DSA2=int(l_s2[0])
    TOC2=int(l_s2[1])
    DM2=int(l_s2[2])
    if (DSA1+TOC1+DM1)>(DSA2+TOC2+DM2):
        print("DRAGON")
    elif (DSA1+TOC1+DM1)==(DSA2+TOC2+DM2) and DSA1>DSA2:
        print("DRAGON")
    elif (DSA1+TOC1+DM1)==(DSA2+TOC2+DM2) and DSA1==DSA2 and TOC1>TOC2:
        print("DRAGON")
    elif (DSA1+TOC1+DM1)==(DSA2+TOC2+DM2) and DSA1==DSA2 and TOC1==TOC2:
        print("TIE")
    else:
        print("SLOTH")
