from subprocess import run
import logging

# Volume percentage by volumn up/down buttons
VOLUME_INTERVAL = 10

class PulseAudioController:
	def _execute_pactl(self, flags: list) -> None:
		logging.debug(f'Executing pactl with flags {flags}')
		run(['pactl'] + flags)

	def volume_up(self) -> None:
		logging.info(f'Increasing volume by {VOLUME_INTERVAL}%')
		self._execute_pactl(['set-sink-volume', '@DEFAULT_SINK@', f'+{VOLUME_INTERVAL}%'])

	def volume_down(self) -> None:
		logging.info(f'Decreasing volume by {VOLUME_INTERVAL}%')
		self._execute_pactl(['set-sink-volume', '@DEFAULT_SINK@', f'-{VOLUME_INTERVAL}%'])

	def set_volume(self, volume: int) -> None:
		try:
			assert 0 <= volume <= 150
		except AssertionError:
			logging.exception(f'Illegal value {volume} for PulseAudioController.set_volume: volume must be between 0 and 150')
			return

		logging.info(f'Setting volume to {volume}%')
		self._execute_pactl(['set-sink-volume', '@DEFAULT_SINK@', f'{volume}%'])


	def mute_unmute(self) -> None:
		self._execute_pactl(['set-sink-mute', '@DEFAULT_SINK@', 'toggle'])

