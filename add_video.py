import keyboard
import tkinter
import time
import random

prev_urls = []
video_ids = []
root = tkinter.Tk()

time.sleep(0.6)

prev_clipboard = "fillerclipboard"
curr_clipboard = prev_clipboard

#limit loops to prevent infinite loop
for i in range(50):

    counter = 0
    #copy url using keyboard shortcuts and wait until it is actually copied
    while (prev_clipboard == curr_clipboard and counter < 20):
        keyboard.press_and_release('ctrl + l')
        keyboard.press_and_release('ctrl + c')
        time.sleep(0.1)
        curr_clipboard = root.clipboard_get()
        counter += 1

    prev_clipboard = curr_clipboard
    print("clip board received")

    #stop after cycling through all the tabs    
    if curr_clipboard in prev_urls:
        break

    prev_urls.append(curr_clipboard)
    #search url for youtube and get video id
    url_parts = curr_clipboard.split("/")
    if (len(url_parts) > 3):
        if url_parts[2] == "www.youtube.com" and url_parts[3][0:8] == "watch?v=":
            video_ids.append(url_parts[3][8:])
            print("added video id")
    
    #switch tabs
    keyboard.press_and_release('ctrl + tab')

#add ids to file
f = open('playlist.txt', 'a')
for i in range(len(video_ids)):
    f.write(',' + video_ids[i])
f.close()



