test_cases = int(input())
for j in range(test_cases):
    x = int(input())
    if x<1500:
        print(2*x)
    else:
        DA = 0.98*x 
        print(x+500+DA)
