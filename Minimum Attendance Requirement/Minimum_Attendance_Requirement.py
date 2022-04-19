test_cases = int(input())
for i in range(test_cases):
    m = int(input())
    k=input()
    l=k.count("1")
    remaining_days = 120-m
    max_possible_attendance = (l+remaining_days)
    frac = max_possible_attendance/120 
    percentage = frac*100
    if percentage>=75:
        print("YES")
    else:
        print("NO")
