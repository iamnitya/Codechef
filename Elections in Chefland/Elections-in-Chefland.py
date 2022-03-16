t=int(input())
if t >=1 and t <= 1000:
    for tc in range(t):
        a,b,c=map(int,input().split()) 
        if a>50 and b<=50 and c<=50:
            print("A")
        elif a<=50 and b>50 and c<=50:
            print("B")
        elif a<=50 and b<=50 and c>50:
            print("C")
        elif a<=50 and b<=50 and c<=50:
            print("NOTA")
