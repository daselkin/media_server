from .triaged_request import TriagedReuqestHandler
import logging


class PlayerControlsRequestHandler(TriagedReuqestHandler):
	debug_message = "Player control request received"
	path_regex_pattern = r"/player/.*"
