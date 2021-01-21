from .triaged_request import TriagedReuqestHandler
import logging
import os

from external_sources.youtube import download_music_from_youtube
from playback_handlers.audio import AudioController

from params.server import YT_DOWNLOAD_PATH

class YouTubeRequestHandler(TriagedReuqestHandler):
	debug_message="Youtube request detected"
	path_regex_pattern = r"/https://www.youtube.com/watch\?.*"

	def _execute(self):
		downloaded_file = download_music_from_youtube(self.request.path[1:], YT_DOWNLOAD_PATH)
		AudioController().load_file(os.path.join(YT_DOWNLOAD_PATH, downloaded_file))