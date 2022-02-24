#accepting input
i=input()
l=i.split(' ')
A=int(l[0])
B=int(l[1])
L=A-B
if L%10==9:
    print(L-1)
else:
    print(L+1)
