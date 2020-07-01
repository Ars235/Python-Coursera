import json
import tempfile
import argparse
import os

def get_data(storage_path):

	if not os.path.exists(storage_path): # check if file exists
		return None # if not then return empty dict 
	else: # if exists:
		with open(storage_path, 'r') as f:
			raw_data = f.read()
			return json.loads(raw_data) if raw_data else {}

def read_data(storage_path, args):

	data = get_data(storage_path)

	if data == None or args.key not in data:
		print(None)
		return None

	for i in range(len(data[args.key])):
		# надо это все через запятые высрать
		if i != len(data[args.key]) - 1: # костыли ну а хули и нет
			print(data[args.key][i], end = ', ')
		else:
			print(data[args.key][i])
	

def write_data(storage_path, args):

	data = get_data(storage_path) # dictionary with keys and values or empty dict

	if data == None:
		data = {args.key : [args.val]}
		with open(storage_path, 'w') as f:
			f.write(json.dumps(data))
			return None


	if args.key in data:
		data[args.key].append(args.val) # if we have this key then add value to the list of values
	else:
		data[args.key] = [args.val] # if we don't have the key then create a new key with 1 element list of values to be able to expand it 

	with open(storage_path, 'w') as f: # there we use 'w' because we store all data in 'data variable' and so we're able to rewrite the file
		f.write(json.dumps(data))

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--key', help = 'key word in dictionary')
	parser.add_argument('--val', help = 'value for certain key in dictionary', default = None)
	args = parser.parse_args()
	
	storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

	if args.val is None:
		read_data(storage_path, args) # read data from storage.data
	elif args.key and args.val:
		write_data(storage_path, args) # write data into storage.data
	else:
		print('Key and val are not specified')