test_cases = int(input())
for i in range (test_cases):
    he_can_spend, pizza, burger= map(int,input().split())
    if pizza<he_can_spend:
        print("PIZZA")
    elif burger<he_can_spend:
        print("BURGER")
    else:
        print("NOTHING")
