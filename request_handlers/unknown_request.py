from .triaged_request import TriagedReuqestHandler
import logging


class UnknownRequestHandler(TriagedReuqestHandler):
	debug_message = "Unknown request received"
	path_regex_pattern = r".*"
	pass
