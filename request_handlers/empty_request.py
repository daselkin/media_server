from .triaged_request import TriagedReuqestHandler
from params.assets import LANDING_PAGE_HTML, NOW_PLAYING_BAR
from playback_handlers.audio import AudioController
import logging

class EmptyRequestHandler(TriagedReuqestHandler):
	debug_message = "Empty request received"
	path_regex_pattern = r"^/$"

	def _execute(self):
		self.response = 200
		self.response_headers['Content-Type'] = 'text/html; charset=UTF-8'
		if AudioController().playlist.name is not None:
			now_playing_bar = NOW_PLAYING_BAR.format(now_playing=AudioController().playlist.name)
		else:
			now_playing_bar = ""
		
		self.response_text = LANDING_PAGE_HTML.format(now_playing=now_playing_bar)