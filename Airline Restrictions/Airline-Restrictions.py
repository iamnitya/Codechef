test_cases=int(input())
for i in range(test_cases):
    k=input()
    k_s=k.split(" ")
    bag1=int(k_s[0])
    bag2=int(k_s[1])
    bag3=int(k_s[2])
    max_combined=int(k_s[3])
    max_individual=int(k_s[4])
    if ((bag1+bag2<=max_combined and bag3<=max_individual) 
    or (bag1+bag3<=max_combined and bag2<=max_individual)
    or (bag3+bag2<=max_combined and bag1<=max_individual)):
        print("YES")
    else:
        print("NO")
