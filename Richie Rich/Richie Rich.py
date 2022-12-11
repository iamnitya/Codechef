k = int(input())
for i in range(k):
    A, B, X = map(int,input().split())
    time = (B-A)//X 
    print(time)
