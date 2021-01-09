from http.server import HTTPServer
import logging
import sys
import os

from request_handlers.main import MediaBoxRequestHandler
from params.server import HOST_NAME, PORT


class MediaBoxServer(HTTPServer):
	pass


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