n=int(input())
for i in range(n):
    p=input()
    k=p.split(' ')
    m=k.count('0')
    l=k.count('1')
    if m>l:
        print("NO")
    else:
        print("YES")
