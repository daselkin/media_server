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


class TriagedReuqestHandler:
	def __init__(self, request: BaseHTTPRequestHandler):
		self.request = request
		self.response = 500
		self.response_headers = {}
		self.response_text = ""

	def execute(self) -> None:
		raise NotImplementedError


class EmptyRequestHandler(TriagedReuqestHandler):
	pass

class PlayerRequesHandler(TriagedReuqestHandler):
	pass

class YouTubeRequestHandler(TriagedReuqestHandler):
	def execute(self) -> None:
		try:
			downloaded_file = download_music_from_youtube(self.path[1:], YT_DOWNLOAD_PATH)
			AudioController().load_file(os.path.join(YT_DOWNLOAD_PATH, downloaded_file))
		except Exception as e:
			logging.exception(e)


class UnknownRequestHandler(TriagedReuqestHandler):
	pass



class MediaBoxRequestHandler(BaseHTTPRequestHandler):
	# Determine what basic kind of request this is
	def triage(self):
		parsed_path = self.path.split('/')[1:]
		if len(parsed_path) == 0:
			login.debug("Empty request received")
			return EmptyRequestHandler
		elif parsed_path[1] == 'player':
			logging.debug ("Player control request received")
			return PlayerRequesHandler
		elif parsed_path[1] in ['http', 'https']:
			logging.debug("Youtube request detected")
			return YouTubeRequestHandler
		else:
			logging.debug("Unknown request received")
			return UnknownRequestHandler


	def do_GET(self):
		# Log the request
		logging.info(f"Request received for {self.path} from {self.client_address}")
		
		# Triage
		sub_handler = self.triage()
		sub_handler.execute()

		# Send response
		self.send_response(sub_handler.response)
		for key, value in sub_handler.response_headers.items():
			self.send_headers(key, value)
		self.end_headers()
		self.wfile.write(bytes(sub_handler.response_text, "utf-8"))

		# Close connection. Goodbye!
		self.close_connection = True


if __name__ == '__main__':
	log = logging.getLogger()
	log.setLevel(logging.DEBUG)
	handler = logging.StreamHandler(sys.stdout)
	handler.setLevel(logging.DEBUG)
	handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
	log.addHandler(handler)

	server = MediaBoxServer((HOST_NAME, PORT), MediaBoxRequestHandler)
	logging.info("Starting server")

	try:
		server.serve_forever()
	except KeyboardInterrupt:
		pass

	server.server_close()
	logging.info("Server closed")