t=int(input())
for i in range(t):
    count=0
    m=input()
    
    for i in range(len(m)-1):
        if(m[i]=='<' and m[i+1]=='>'):
            count=count+1
    print(count)
