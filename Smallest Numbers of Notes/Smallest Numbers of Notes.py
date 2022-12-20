for t in range(int(input())):
    n = int(input())
    rs = [100, 50, 10, 5, 2, 1]
    c = 0
    for i in range(0, 6):
        c += n // rs[i]
        n = n % rs[i]
    print(c)
