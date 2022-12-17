test_cases = int(input())
for i in range(test_cases):
    length_list = int(input())
    list1 = list(map(int,input().split()))
    list2 = list(map(int,input().split()))
    count = 0
    for j in range(length_list):
        if list1[j]==list2[j]:
            count+=1 
    print(count)
