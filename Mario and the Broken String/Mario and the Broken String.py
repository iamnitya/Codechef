test_cases = int(input())
for j in range(test_cases):
    x = int(input())
    y = list(input())
    if y[0:x//2] == y[x//2:x]:
        print("YES")
    else:
        print("NO")
