import requests
def get_playlist_tracks(url):
	res = requests.get(url)
	txt = res.text
	txt = txt[txt.find('"is_playable":true,"name"'):]
	songs = []
	while True:
		start = txt.find('"is_playable":true,"name":"') 
		if (start == -1): break
		start = start + len('"is_playable":true,"name":"')
		end = start
		while True:
			if (txt[end] == '"'):
				break
			end = end + 1
		songs.append(txt[start:end])
		txt = txt[end+1:]
	return songs