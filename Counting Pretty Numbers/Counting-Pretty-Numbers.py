test_cases=int(input())
for i in range(test_cases):
    count=0
    n=(input())
    n_s=n.split(' ')
    k=int(n_s[0])
    l=int(n_s[1])
    for i in range(k,l+1):
        if i%10==3 or i%10==2 or i%10==9:
            count+=1 
    print(count)
