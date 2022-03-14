test_cases=int(input())
for i in range(test_cases):
    n=input()
    n_s=n.split(" ")
    k=int(n_s[0]) 
    l=int(n_s[1]) 
    m=int(n_s[2])
    if k+l<m:
        print("PLANEBUS")
    elif k+l>m:
        print("TRAIN")
    else:
        print("EQUAL")
