from .triaged_request import TriagedReuqestHandler
import os
import urllib.parse
import logging

from playback_handlers.audio import AudioController

from params.server import MUSIC_LIBRARY_PATH

class PlayTracksRequestHandler(TriagedReuqestHandler):
	debug_message="Play request detected"
	path_regex_pattern = r"/play/"

	def _execute(self):
		self.unquoted_path = urllib.parse.unquote(self.request.path[len(self.path_regex_pattern):])
		self.filepath = os.path.join(MUSIC_LIBRARY_PATH, self.unquoted_path)
		logging.debug(f"Playing {self.filepath}")
		AudioController().load_file(self.filepath)