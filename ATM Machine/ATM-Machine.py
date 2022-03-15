test_cases=int(input())
for i in range(test_cases):
    n=input()
    n_s=n.split(" ")
    number_people=int(n_s[0])
    number_units=int(n_s[1])
    k=input()
    k_s=k.split(' ')
    for i in range(number_people):
        p=int(k_s[i])
        rem=number_units-p
        if (rem>=0):
            print(1,end="")
            number_units=rem
        else:
            print(0, end="")
            number_units=number_units
    print()
