test_cases = int(input())
for i in range (test_cases):
    total, num_infected= map(int,input().split())
    num_not_infected = total - num_infected
    if num_infected<num_not_infected:
        print(num_infected)
    else:
        print(num_not_infected)
