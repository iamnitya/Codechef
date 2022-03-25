T = int(input())
while T!=0:
    count =0
    n,a,b,c = map(int,input().split())
    for i in range(0,100):
        if b>=a and a!=0:
          b= b-1
          a= a -1
          count = count +1                                        
        elif c>=b and b!=0:
          c= c-1
          b=b-1
          count  = count +1
        elif b>=c and c!=0:
          b = b-1
          c= c-1
          count = count +1
        elif a>=b and b!=0:
          a= a-1
          b = b-1
          count = count +1
    if count >= n:
        print("YES")
    else:
        print("NO")
    T = T-1
