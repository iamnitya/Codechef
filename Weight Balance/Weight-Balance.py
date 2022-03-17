test_cases=int(input())
for i in range(test_cases):
    k=input()
    k_s=k.split(" ")
    w1=int(k_s[0])
    w2=int(k_s[1])
    x1=int(k_s[2])
    x2=int(k_s[3])
    M=int(k_s[4])
    w_change=abs(w2-w1)
    gain_per_month=x1*M
    total_gain=x2*M
    if gain_per_month<=w_change<=total_gain:
        print(1)
    else:
        print(0)
      
