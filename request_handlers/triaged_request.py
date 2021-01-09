from http.server import BaseHTTPRequestHandler
import logging


class TriagedReuqestHandler:
	debug_message = ""
	path_regex_pattern = r""

	def __init__(self, request: BaseHTTPRequestHandler):
		self.request = request
		self.response = 500
		self.response_headers = {}
		self.response_text = ""

	def execute(self):
		try:
			self._execute()
		except Exception as e:
			logging.exception(e)
			self.response = 400
			self.response_headers['Content-Type'] = 'text/html; charset=UTF-8'
			self.response_text = f"{e}"
	
	def _execute(self):
		raise NotImplementedError