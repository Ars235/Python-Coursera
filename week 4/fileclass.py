import tempfile
import os

class File:

	def __init__(self, file_path):
		try :
			file_path = os.path.join(tempfile.gettempdir(), file_path)
			if not os.path.exists(file_path):
				file = open(file_path, 'w')
				file.close()
				self.file_path = file_path
			else:
				self.file_path = file_path
		except ValueError:
			print('Path to the file must be "str"')
		### attributes for iteration
		self.index = 0 
		self.sentence = self.read().split('\n')
		self.length = len(self.sentence)
		###
	def read(self):
		with open(self.file_path, 'r') as file:
			return file.read()

	def write(self, string):
		with open(self.file_path, 'w') as file:
			if type(string) == str:
				file.write(string)
			else:
				raise ValueError

	def __str__(self):
		return self.file_path
	def __add__(self, other):
		new_file_obj = self._new_class()
		if type(self) == type(other):
			new_file_obj.write(self.read() + other.read())
			return new_file_obj
		else:
			return

	def __iter__(self):
		file = open(self.file_path, 'r')
		return file

	def __next__(self):
		if self.index >= self.length:
			self.__iter__().close()
			raise StopIteration
		index = self.index
		self.index += 1
		return self.sentence[index]

	@classmethod
	def _new_class(cls):
		return cls('new_file')
