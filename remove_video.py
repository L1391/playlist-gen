request = input("Videos numbers to remove (separate with a comma) ")
playlist_name = input("name of playlist to edit ")

numbers_to_remove = request.split(',')

#read file
f = open('playlist' + playlist_name + '.txt', 'r')
playlist_ids = f.read().split(',')
f.close()

#remove videos from unshuffled list
for i in range(len(numbers_to_remove)):
    playlist_ids[int(numbers_to_remove[i]) - 1] = 'remove'

#rewrite file
f = open('playlist' + playlist_name + '.txt', 'w')
f.write(playlist_ids[0])
for i in range(1, len(playlist_ids)):
    if not playlist_ids[i] == 'remove':
        f.write("," + playlist_ids[i])

f.close()

