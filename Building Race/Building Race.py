n = int(input())
for i in range(n):
    a,b,c,d = map(int,input().split())
    chef = a/b
    chefina = c/d 
    if chef>chefina:
        print("Chefina")
    elif chefina>chef:
        print("Chef")
    else:
        print("Both")
    
        
