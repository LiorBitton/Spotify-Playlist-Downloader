import requests, os
import list_spotify_playlist, download_youtube_video
from song import Song
import time,os.path
from tkinter import Tk, filedialog
root = Tk()
root.withdraw()
root.attributes('-topmost', True)


url = input("enter playlist link(must be public):")
convert =True if (input("Do you want to convert the songs to mp3 from webm(requires ffmpeg) y/n: \n") == "y" ) else False
open_file = filedialog.askdirectory()
songs = list_spotify_playlist.get_playlist_tracks(url)

i = 1
for song in songs:
	try:
		os.system("cls")
		print("downloading : " + song.name + f" [{i}/{len(songs)}]")
		download_youtube_video.title_to_mp3(song.name + " by " + song.artist, open_file)
	except:
		print("failed")
	i=i+1
	time.sleep(3)  #prevents from spamming the youtube download api
if not convert:
	quit()
print("converting songs to mp3...")
songs = os.listdir(open_file)

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
