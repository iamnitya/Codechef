# cook your dish here
for i in range(int(input())):
	x=int(input())
	x1=list(map(int,input().split()))
	k=set(x1)
	s=[]
	for i in k:
		c=x1.count(i)
		s.append(c)
	r=max(s)
	if r>1:
	    print(len(k))
	else:
	    print(len(s))
