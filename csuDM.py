def init(filename):
	f = open("Data/" + filename, 'w')
	f.write(filename[:-4] + "\n")
	f.close()

def write(filename, dArray):
	f = open("Data/" + filename, 'a')
	for val in dArray:
		f.write(str(val) + ', ')
	f.write('\n')
	f.close()

