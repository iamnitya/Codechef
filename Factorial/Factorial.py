def z(m):
    zero=0
    i=1
    while m//5**i>0:
        zero=zero+m//5**i
        i=i+1
    return zero
t=int(input())
while t>0:
    m=int(input())
    print(z(m))
    t=t-1
