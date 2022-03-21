for i in range(int(input())):
    s=input()
    s_s=s.split(" ")
    m=int(s_s[0])
    n=int(s_s[1])
    o=int(s_s[2])
    sta=(m*(2**0.5))/n
    ele=m*2/o
    if sta<ele:
        print("Stairs")
    else:
        print("Elevator")
