from pytube import YouTube
from params.youtube import (
	SEARCH_URL,
	DEFAULT_SEARCH_PARAMS,
	LIST_URL,
	DEFAULT_LIST_PARAMS,
	GENRES,
)
import requests
import logging
import json


class YoutubeAPIException(Exception):
	pass


class YoutubeVideo:
	def __init__(self, json_object):
		self.json_object = json_object
		self.id = json_object['id']
		self.watch_url = f"https://youtube.com/watch?v={self.id}"
		self.title = json_object['snippet']['title']
		self.description = json_object['snippet']['description']
		self.thumbnail_url = json_object['snippet']['thumbnails']['default']
		self.duration = json_object['contentDetails']['duration']
		self.is_music_video = '/m/04rlf' in json_object['topicDetails']['relevantTopicIds']
		self.genres = [
			GENRES[topic_id]
			for topic_id in json_object['topicDetails']['relevantTopicIds']
			if topic_id in GENRES
		]

def search_youtube(search_string: str) -> list:
	"Search youtube, return a list of video IDs"
	r = requests.get(
		url=SEARCH_URL,
		params={
			'q': search_string,
			**DEFAULT_SEARCH_PARAMS,
		}
	)

	if r.status_code == 200:
		return [item['id']['videoId'] for item in json.loads(r.text)['items']]
	else:
		raise YoutubeAPIException(f"{r.status_code}: {r.text}")


def list_videos(video_ids: list) -> list:
	r = requests.get(
		url=LIST_URL,
		params={
			'id': ','.join(video_ids),
			**DEFAULT_LIST_PARAMS
		},
	)
	if r.status_code == 200:
		return [
			YoutubeVideo(item) 
			for item in json.loads(r.text)['items']
		]
	else:
		raise YoutubeAPIException(f"{r.status_code}: {r.text}")



def download_music_from_youtube(youtube_url: str, download_path: str) -> str:
	logging.info(f'accessing Youtube URL {youtube_url}')

	yt = YouTube(youtube_url)
	audio_streams = yt.streams.filter(only_audio=True)

	logging.debug(f'{len(audio_streams)} found')

	best_audio_stream = audio_streams.order_by('abr').last()

	logging.info(f'Downloading {best_audio_stream.default_filename} (size {best_audio_stream.filesize_approx}')

	best_audio_stream.download(download_path)

	logging.info('Download successful')

	return best_audio_stream.default_filename 