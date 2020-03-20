import random

#read file to display new shuffled playlist url
f = open('playlist.txt', 'r')
playlist_ids = f.read().split(',')
random.shuffle(playlist_ids)
f.close()

#generate new playlist link
link_to_clipboard = "www.youtube.com/watch_videos?video_ids=" + playlist_ids[0]
for i in range(1, len(playlist_ids)):
    link_to_clipboard += "," + playlist_ids[i]

#print new link
print(link_to_clipboard)
input()