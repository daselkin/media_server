from .triaged_request import TriagedReuqestHandler
import logging
import os

from external_sources.youtube import download_music_from_youtube
from playback_handlers.audio import AudioController

from params.server import YT_DOWNLOAD_PATH

class YouTubeRequestHandler(TriagedReuqestHandler):
	debug_message="Youtube request detected"
	path_regex_pattern = r"/youtube/"

	def _execute(self):
		downloaded_file = download_music_from_youtube(self.request.path[len(self.path_regex_pattern):], YT_DOWNLOAD_PATH)
		AudioController().load_file(os.path.join(YT_DOWNLOAD_PATH, downloaded_file))
		self.response = 200