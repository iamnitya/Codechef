# cook your dish here
testcases = int(input())
for i in range(testcases):
    k = input()
    if "101" in k or "010" in k:
        print("Good")
    else:
        print("Bad")
