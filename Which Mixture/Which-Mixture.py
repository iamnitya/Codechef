n=int(input())
for i in range(n):
    p=input()
    k=p.split(' ')
    m=int(k[0])
    l=int(k[1])
    if m>0 and l>0:
        print("Solution")
    elif l==0 and m>0:
        print("Solid")
    else:
        print("Liquid")
