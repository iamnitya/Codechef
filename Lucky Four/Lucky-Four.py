t = int(input())
for i in range(t):
    count = 0
    num = int(input())
    while(num):
        if(num%10 == 4):
            count +=1
        num = int(num/10)
    print(count)
