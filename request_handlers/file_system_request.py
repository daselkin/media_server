from .triaged_request import TriagedReuqestHandler
import logging
import os
import urllib.parse

from params.server import MUSIC_LIBRARY_PATH
from params.assets import (
	BROWSE_MEDIA_PAGE_HTML,
	MEDIA_LIBRARY_ITEM,
	MEDIA_ITEM,
)

class FileSystemRequestHandler(TriagedReuqestHandler):
	debug_message = "File system request received"
	path_regex_pattern = r"/browse/"

	def format_directory(self, directory_name):
		return MEDIA_LIBRARY_ITEM.format(
			link_url=f"{self.path_regex_pattern}{self.unquoted_path}{directory_name}/",
			link_text=f"{directory_name}/"
		)

	def format_file(self, file_name):
		return MEDIA_ITEM.format(
			link_url=f"/play/{self.unquoted_path}/{file_name}",
			link_text=f"{file_name}/"
		)

	def format_play_all(self):
		return MEDIA_ITEM.format(
			link_url=f"/play/{self.unquoted_path}",
			link_text="🎶🎶🎶 PLAY ALL FILES 🎶🎶🎶"
		)

	def _execute(self):
		self.unquoted_path = urllib.parse.unquote(self.request.path[len(self.path_regex_pattern):])
		logging.debug(f"Unquoted path: {self.unquoted_path}")
		self.filepath = os.path.join(MUSIC_LIBRARY_PATH, self.unquoted_path)
		logging.debug(f"Fetching directory contents for {self.filepath}")
		
		directory_contents = [
			(dir_entry.is_file(), dir_entry.name)
			for dir_entry in os.scandir(self.filepath)
		]

		directory_contents_formatted = "\n".join([
			self.format_play_all()
			] + [{
					True: self.format_file,
					False: self.format_directory,
				}[is_file](file_name)
				for is_file, file_name in sorted(directory_contents)
			]
		)

		self.response = 200
		self.response_headers['Content-Type'] = 'text/html; charset=UTF-8'
		self.response_text = BROWSE_MEDIA_PAGE_HTML.format(
			media_items_list=directory_contents_formatted
		)
