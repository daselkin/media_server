from subprocess import Popen
import logging

class AudaciousController:
	def _execute_audacious(self, flags: list, file_name: str = '') -> Popen:
		logging.debug(f'Executing audacious with flags {flags}')
		return Popen(['audacious'] + flags + ([file_name] if file_name != '' else []))

	def load_file(self, file_name: str, enqueue: bool = False) -> Popen:
		logging.info(f'Attempting to run {file_name} on Audacious')
		return self._execute_audacious(flags = (['--enqueue'] if enqueue else []), file_name=file_name)

	def play(self) -> Popen:
		logging.info("Starting/resuming playback")
		return self._execute_audacious(flags=['--play'])

	def stop(self) -> Popen:
		logging.info("Stopping playback")
		return self._execute_audacious(flags=['--stop'])

	def pause(self) -> Popen:
		logging.info("Pausing playback")
		return self._execute_audacious(flags=['--pause'])

	def skip_forward(self) -> Popen:
		logging.info("Skipping forward")
		return self._execute_audacious(flags=['--fwd'])

	def skip_back(self) -> Popen:
		logging.info("Skipping back")
		return self._execute_audacious(flags=['--rew'])
