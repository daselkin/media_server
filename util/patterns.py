import logging

class Borg:
	_shared_state = {}

	def _init(self):
		raise NotImplementedError

	def __init__(self):
		self.__dict__ = self._shared_state
		if not hasattr(self, '_initialized'):
			self._init()
			self._initialized = True
			logging.debug("Borg class initialized")
		