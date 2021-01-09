from .triaged_request import TriagedReuqestHandler
import logging

class EmptyRequestHandler(TriagedReuqestHandler):
	debug_message = "Empty request received"
	path_regex_pattern = r"^/$"
