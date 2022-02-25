#RUNTIME ERROR SOLUTION 
import math
count=0
number_test_cases=int(input())
for i in range(number_test_cases):
    m=int(input())
    k=math.factorial(m)
    m=str(k)[::-1]
    length=len(m)
    for j in range(length):
        p=int(m[j])
        while p==0:
            count=count+1
        break
    print(count)
