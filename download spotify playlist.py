import requests
import downloadYT
import listPlaylist
import downloadYT
import time,os.path

from tkinter import Tk, filedialog
import os
root = Tk()
root.withdraw()
root.attributes('-topmost', True)


url = input("enter playlist link(must be public):")
convert =True if (input("Do you want to convert the songs to mp3 from webm(requires ffmpeg) y/n: \n") == "y" ) else False
open_file = filedialog.askdirectory()
songs = listPlaylist.get_playlist_tracks(url)
for song in songs:
	downloadYT.title_to_mp3(song, open_file)
	print("downloaded : " + song)
	time.sleep(4)  #prevents from spamming the youtube download api
if not convert:
	quit()
print("converting songs to mp3...")
songs = os.listdir(open_file)
"""
FILE="the-file-you-want-to-process.webm";
ffmpeg -i "${FILE}" -vn -ab 128k -ar 44100 -y "${FILE%.webm}.mp3";
"""
webm_files = []
for song in songs:
	if (song.split(".")[-1] == "webm"):
		webm_files.append(song)

for song in webm_files:
	song = os.path.abspath(open_file + '/'+song)
	cmd = f'ffmpeg -i "{song}" -vn -ab 128k -ar 44100 -y "{song.replace(".webm","")}.mp3'
	os.system(cmd)
	os.remove(song)
print("done")
