from .audacious import AudaciousController
from .pactl import PulseAudioController
from .playlist import Playlist

from util.patterns import Borg

import logging

class AudioController(Borg, PulseAudioController, AudaciousController):
	def __init__(self):
		Borg.__init__(self)


	def _init(self):
		logging.debug("Setting up AudioController class")
		self.playlist = Playlist()

	def load_file(self, file_name: str, enqueue: bool = False) -> None:
		AudaciousController.load_file(self, file_name)
		self.playlist.add_file_or_directory(file_name, enqueue)