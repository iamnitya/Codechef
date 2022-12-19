test_cases = int(input())
for i in range(test_cases):
    x = int(input())
    if 35<=x<=65:
        print("Normal")
    elif x>65:
        print("Overload ")
    else:
        print("Underload ")
