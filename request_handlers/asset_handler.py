from .triaged_request import TriagedReuqestHandler
from params.assets import ASSET_DIRECTORY
import logging
import os
import urllib

ASSET_CONTENT_TYPE_BY_SUFFIX = [
	('.ico', 'image/x-icon'),
	('.css', 'text/css'),
	('.js', 'text/javascript'),
	('', 'text/plain-text')
]

class AssetRequestHandler(TriagedReuqestHandler):
	debug_message = "Asset request received"
	path_regex_pattern = r"/assets/"

	def get_asset_content_type(self, filename):
		for suffix, content_type in ASSET_CONTENT_TYPE_BY_SUFFIX:
			if filename[-len(suffix):] == suffix:
				return content_type
		return content_type


	def _execute(self):
		self.unquoted_path = (
			urllib.parse.unquote(self.request.path).
			replace(self.path_regex_pattern, ASSET_DIRECTORY)
		)
		logging.debug(f"Searching for asset {self.unquoted_path}")

		if os.path.isfile(self.unquoted_path):
			logging.debug("File found")
			self.response = 200
			self.response_headers['Content-Type'] = self.get_asset_content_type(self.unquoted_path)
			logging.debug(f"Content type is {self.response_headers['Content-Type']}")
			self.response_bytes = open(self.unquoted_path, 'rb').read()
		else:
			logging.debug("File not found")
			self.response = 404
			self.response_headers['Content-Type'] = 'text/plain-text'
			self.response_text = f"File {self.unquoted_path} not found."