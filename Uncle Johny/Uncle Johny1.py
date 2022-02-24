num_test_cases = int(input())
for i in range(num_test_cases):
    number_songs = int(input())
    song_list = list(map(int,input().split()))
    selected_song = int(input())
    d = song_list[selected_song-1]
    song_list.sort()
    print(song_list.index(d)+1)
