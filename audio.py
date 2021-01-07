from audacious import AudaciousController
from pactl import PulseAudioController
import logging

class AudioController(PulseAudioController, AudaciousController):
	def __init__(self):
		logging.debug("Setting up AudioController class")

