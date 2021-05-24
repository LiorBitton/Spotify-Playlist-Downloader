import requests
import downloadYT
import listPlaylist
import downloadYT
import time,os.path
url = input("enter playlist link(must be public):")
songs = listPlaylist.get_playlist_tracks(url)
for song in songs:
	downloadYT.title_to_mp3(song, os.path.abspath("./music/"))
	print("downloaded : " + song)
	time.sleep(5) #prevents from spamming the youtube download api 
print("done")
