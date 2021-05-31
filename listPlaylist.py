import requests
from song import Song
def get_playlist_tracks(url):
	res = requests.get(url)
	txt = res.text
	txt = txt[txt.find('"is_playable":true,"name"'):]
	songs = []
	while True:
		start = txt.find('"is_playable":true,"name":"')
		info_idx = start
		if (start == -1): break
		##name
		start = start + len('"is_playable":true,"name":"')
		end = start
		while True:
			if (txt[end] == '"'):
				break
			end = end + 1
		name = txt[start:end]
		
		##artist
		art = txt[info_idx::-1].find('"name":'[::-1])
		art_idx = info_idx - art
		art_idx = txt[art_idx:].find(":") + art_idx +2
		art_end = txt[art_idx:].find(',') + art_idx - 1
		artist = txt[art_idx:art_end]
		##duration
		dur = txt[info_idx::-1].find("duration_ms"[::-1])
		name_idx = info_idx - dur
		name_idx = txt[name_idx:].find(":") + name_idx
		name_end = txt[name_idx:].find(",") + name_idx
		duration = txt[name_idx + 1 :name_end]
		txt = txt[end + 1 :]
		sng = Song(name, artist, duration)
		songs.append(sng)
	return songs