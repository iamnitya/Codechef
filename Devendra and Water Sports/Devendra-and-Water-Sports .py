test_cases=int(input())
for i in range(test_cases):
    p=input()
    n_s=p.split(" ")
    total_amount=int(n_s[0]) 
    amount_spent=int(n_s[1]) 
    cost1=int(n_s[2])
    cost2=int(n_s[3])
    cost3=int(n_s[4])
    amount_remaining=total_amount-amount_spent
    cost_watersports=cost1+cost2+cost3
    if amount_remaining>=cost_watersports:
        print("YES")
    else:
        print("NO")
