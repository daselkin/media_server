from .triaged_request import TriagedReuqestHandler
import logging
from collections import namedtuple
import re

from playback_handlers.audio import AudioController


PlaybackCommand = namedtuple(
	"PlaybackCommand",
	[
		"regex",
		"function",
		"debug_comment"
	],
)

PLAYABACK_COMMANDS = [
	PlaybackCommand(
		r"play",
		AudioController.play,
		"Play command received"
	),

	PlaybackCommand(
		r"stop",
		AudioController.stop,
		"Stop command received"
	),

	PlaybackCommand(
		r"pause",
		AudioController.pause,
		"Pause command received"
	),

	PlaybackCommand(
		r"next",
		AudioController.skip_forward,
		"Skip forward command received"
	),

	PlaybackCommand(
		r"prev",
		AudioController.skip_back,
		"Skip back command received"
	),
]

class PlayerControlsRequestHandler(TriagedReuqestHandler):
	debug_message = "Player control request received"
	path_regex_pattern = r"/player/*"

	def interpret_command(self):
		for command in PLAYABACK_COMMANDS:
			if re.match(path_regex_pattern+command.regex, self.request.path):
				return command
		return None

	def _execute(self):
		command = self.interpret_command()
		if command is not None:
			command.function()
		else:
			raise AssertionError(f"Unknwon command {self.request.path}")