#my solution which was not accepted by codechef :(
number_test_cases=int(input())
for i in range(number_test_cases):
    number_songs=int(input())
    k=input()
    k1=k.split(' ')
    postion_song=int(input())
    m=k1[postion_song-1]
    n=m
    k1.sort()
    p=k1.index(n)
    print("Output: ",p+1)
