from .triaged_request import TriagedReuqestHandler
from params.assets import LANDING_PAGE_HTML
import logging

class EmptyRequestHandler(TriagedReuqestHandler):
	debug_message = "Empty request received"
	path_regex_pattern = r"^/$"

	def _execute(self):
		self.response = 200
		self.response_headers['Content-Type'] = 'text/html; charset=UTF-8'
		self.response_text = LANDING_PAGE_HTML