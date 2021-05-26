import requests
import downloadYT
import listPlaylist
import downloadYT
import time,os.path

from tkinter import Tk, filedialog

root = Tk()
root.withdraw()
root.attributes('-topmost', True)



url = input("enter playlist link(must be public):")
open_file = filedialog.askdirectory()
songs = listPlaylist.get_playlist_tracks(url)
for song in songs:
	downloadYT.title_to_mp3(song, open_file)
	print("downloaded : " + song)
	time.sleep(5) #prevents from spamming the youtube download api 
print("done")
