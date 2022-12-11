k = int(input())
for i in range(k):
    D, L, R = map(int,input().split())
    if L<=D<=R:
        print("Take second dose now")
    elif L>D:
        print("Too Early")
    else:
        print("Too Late")
