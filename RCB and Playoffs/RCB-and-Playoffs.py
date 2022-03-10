test_cases=int(input())
for i in range(test_cases):
    r=input()
    r_s=r.split(" ")
    x=int(r_s[0])
    y=int(r_s[1])
    z=int(r_s[2])
    if ((x+(2*z))>=y):
        print('YES')
    else:
        print('NO')
