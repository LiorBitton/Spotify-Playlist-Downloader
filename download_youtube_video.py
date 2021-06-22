import requests
import pafy
def title_to_mp3(keywords,path):
	html = requests.get("https://www.youtube.com/results?search_query=" + keywords)
	#find the first video
	target = "/watch?v="
	idx = html.text.index(target) + len(target)
	vid_id = html.text[idx: idx + 11]
	url = "https://www.youtube.com/watch?v=" + vid_id
	video = pafy.new(url)
	audios = video.audiostreams
	bestaudio = video.getbestaudio()
	bestaudio.download(filepath=path)
