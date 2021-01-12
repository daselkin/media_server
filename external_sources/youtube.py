from pytube import YouTube
import logging


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