# This file includes the main request handler: 
# MediaBoxRequestHandler which is the extention of BaseHTTPRequestHandler
# And TriagedRequestHandler which is the superclass for the actual worker threads.

from http.server import BaseHTTPRequestHandler
from .triaged_request import TriagedReuqestHandler
import logging
import re

from .empty_request import EmptyRequestHandler
from .asset_handler import AssetRequestHandler
from .play_tracks import PlayTracksRequestHandler
from .file_system_request import FileSystemRequestHandler
from .unknown_request import UnknownRequestHandler
from .player_controls import PlayerControlsRequestHandler
from .youtube_handler import YouTubeRequestHandler

TRIAGE_ORDER = (
	EmptyRequestHandler,
	AssetRequestHandler,
	PlayTracksRequestHandler,
	FileSystemRequestHandler,	
	PlayerControlsRequestHandler,
	YouTubeRequestHandler,
	UnknownRequestHandler,
)

class MediaBoxRequestHandler(BaseHTTPRequestHandler):
	# Determine what basic kind of request this is
	def triage(self):
		for handler in TRIAGE_ORDER:
			if re.match(handler.path_regex_pattern, self.path) is not None:
				return handler

	def do_GET(self):
		# Log the request
		logging.info(f"Request received for {self.path} from {self.client_address}")
		
		# Triage
		sub_handler_type = self.triage()
		sub_handler = sub_handler_type(self)
		logging.debug(sub_handler.debug_message)
		sub_handler.execute()

		# Send response
		self.send_response(sub_handler.response)
		for key, value in sub_handler.response_headers.items():
			self.send_header(key, value)
		self.end_headers()
		if sub_handler.response_bytes is None:
			self.wfile.write(bytes(sub_handler.response_text, "utf-8"))
		else:
			self.wfile.write(sub_handler.response_bytes)	

		# Close connection. Goodbye!
		self.close_connection = True
