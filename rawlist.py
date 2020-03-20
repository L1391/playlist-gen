
#read file to display new shuffled playlist url
f = open('playlist.txt', 'r')
playlist_ids = f.read()
f.close()

#generate new playlist link
link_to_clipboard = "www.youtube.com/watch_videos?video_ids=" + playlist_ids

#print new link
print(link_to_clipboard)
input()