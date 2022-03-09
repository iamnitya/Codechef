l=input()
p=l.split(' ')
k=int(p[0]) 
n=int(p[1]) 
w=int(p[2]) 
no_of_overs=20-n
no_balls=no_of_overs*6
max_runs=no_balls*6
if w+max_runs>k:
    print("YES")
else:
    print("NO")
