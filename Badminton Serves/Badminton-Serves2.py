#time limit exceeded error
test_cases=int(input())
for i in range(test_cases):
    count=0
    n=int(input())
    for i in range(n+1):
        if i%2==0:
            count+=1 
    print(count)
        
