n = int(input())
for i in range(n):
    a,b,c = map(int,input().split())
    total = (b*3)-(a-b)
    if total>=c:
        print("PASS")
    else:
        print("FAIL")
        
