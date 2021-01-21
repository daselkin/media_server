from .triaged_request import TriagedReuqestHandler
import logging
import os
import urllib.parse

from params.server import MUSIC_LIBRARY_PATH

class FileSystemRequestHandler(TriagedReuqestHandler):
	debug_message = "File system request received"
	path_regex_pattern = r"/browse/"

	def format_directory(self, directory_name):
		return f"""<li>
			<a href="{self.path_regex_pattern}{self.unquoted_path}{directory_name}/">
			{directory_name}/
			</a>
			</li>"""

	def format_file(self, file_name):
		return f"""<li>
			<a href="/play/{self.unquoted_path}/{file_name}">
			{file_name}
			</a>
			</li>"""

	def format_play_all(self):
		return f"""<li>
			<a href="/play/{self.unquoted_path}">
			!----PLAY ALL FILES----!
			</a>
			</li>"""

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
		self.response_text = f"""
		<html>
			<head>
				<title>Browsing Mediabox</title>
				<link href="/assets/favicon.ico" rel="icon">
			</head>
			<body><ul>
			{directory_contents_formatted}
			</ul></body>
		</html>
		"""



