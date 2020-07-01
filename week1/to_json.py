import json
import functools

def to_json(func):

	@functools.wraps(func) # func saves its name
	def wrapped(*args, **kwargs):
		return json.dumps(func(*args, **kwargs))

	return wrapped