import math
for i in range(int(input())):
	m,n=(map(int,input().split()))
	count = 0
	while math.floor(m/n)>0:
	    count+=1
	    m = math.floor(m/n)
	print(count+1)
