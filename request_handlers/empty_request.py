from .triaged_request import LANDING_PAGE_HTML
from params,assets import landing_page_html
import logging

class EmptyRequestHandler(TriagedReuqestHandler):
	debug_message = "Empty request received"
	path_regex_pattern = r"^/$"

	self.response = 200
	self.response_headers['Content-Type'] = 'text/html; charset=UTF-8'
	self.response_text = LANDING_PAGE_HTML