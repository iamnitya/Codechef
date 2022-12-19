test_cases = int(input())
for j in range(test_cases):
    d,x,y,z = map(int,input().split())
    m1 = 7*x 
    m2 = d*y+((7-d)*z)
    if m1>m2:
        print(m1)
    else:
        print(m2)
