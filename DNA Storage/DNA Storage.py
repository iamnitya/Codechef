test_cases = int(input())
for j in range(test_cases):
    x = int(input())
    y = list(input())
    s = ""
    for i in range(0,x,2):
        if y[i]+y[i+1]=="00":
            s+="A"
        elif y[i]+y[i+1]=="01":
            s+="T"
        elif y[i]+y[i+1]=="10":
            s+="C"
        else:
            s+="G"
    print(s)
