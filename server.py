from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import sys
import os

from youtube import download_music_from_youtube
from audio import AudioController

HOST_NAME = "0.0.0.0"
PORT = 8096

YT_DOWNLOAD_PATH = '/home/alon/youtube_downloads'

class MediaBoxServer(HTTPServer):
	pass

class MediaBoxRequestHandler(BaseHTTPRequestHandler):
	def __init__(self):
		BaseHTTPRequestHandler.__init__(self)
		logging.info("Server started")
		self.audio_controller = AudioController()

	def do_GET(self):
		# Log the request
		logging.info(f"Request received for {self.path} from {self.client_address}")
		self.send_response(200)

		LoggingServer.do_GET(self)
		try:
			downloaded_file = download_music_from_youtube(self.path[1:], YT_DOWNLOAD_PATH)
			AudioController.load_file(os.path.join(YT_DOWNLOAD_PATH, downloaded_file))
		except Exception as e:
			logging.exception(e)

		self.close_connection = True


if __name__ == '__main__':
	log = logging.getLogger()
	log.setLevel(logging.DEBUG)
	handler = logging.StreamHandler(sys.stdout)
	handler.setLevel(logging.DEBUG)
	handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
	log.addHandler(handler)

	server = MediaBoxServer((HOST_NAME, PORT), YouTubePlayerServer)
	logging.info("Starting server")

	try:
		server.serve_forever()
	except KeyboardInterrupt:
		pass

	server.server_close()
	logging.info("Server closed")