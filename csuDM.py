def init(filename):
	f = open(filename, 'w')
	f.write(filename[:-4] + "\n")
	f.close()

def write(filename, dArray):
	f = open(filename, 'a')
	for val in dArray:
		f.write(str(val) + ', ')
	f.write('\n')
	f.close()

