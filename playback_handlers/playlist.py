import os
import logging

class Track():
	def __init__(self, filename):
		self.filename = filename
		self.display_name = os.path.basename(filename)

class Playlist():
	def __init__(self):
		self.clear()


	def clear(self):
		self.name = None
		self.tracks = []
		self.position = None		


	def add_file(self, filename: str) -> None:
		try:
			assert os.path.isfile(filename)
		except AssertionError:
			raise FileNotFoundError(f"File {filename} not found.") 
		self.tracks.append(Track(filename))


	def add_directory(self, directory_name: str) -> None:
		try:
			assert os.path.isdir(directory_name)
		except AssertionError:
			raise FileNotFoundError(f"Directory {directory_name} not found.") 

		for (dirpath, dirnames, filenames) in os.walk(directory_name):
			for filename in filenames:
				self.add_file(os.path.join(dirpath, filename))


	def set_file(self, filename: str) -> None:
		self.clear()
		self.add_file(filename)
		self.name = self.tracks[0].display_name


	def set_directory(self, directory_name: str) -> None:
		self.clear()
		self.add_directory(directory_name)
		self.name = os.path.basename(os.path.dirname(directory_name))


	def add_file_or_directory(self, path: str, enqueue: bool) -> None:
		try:
			assert os.path.exists(path)
		except AssertionError:
			raise FileNotFoundError(f"Path {path} not found.")
		if os.path.isfile(path):
			(self.add_file if enqueue else self.set_file)(path)
		elif os.path.isdir(path):
			(self.add_directory if enqueue else self.set_directory)(path)
		else:
			raise FileNotFoundError(f"{path} is neither file nor directory")

		logging.debug(f"Playlist is now titled {self.name}")