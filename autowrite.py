from os import listdir


temp = open("temporary.txt", 'w')

def write_this_true(x):
	y = (x+" = Commands('"+x+"', def_file('"+x+"'), 'true')\nfunctions.update({'"+x+"': "+x+".command})")
	return y

def write_this_false(x):
	y = (x+" = Commands('"+x+"', def_file('"+x+"'), 'false')\nfunctions.update({'"+x+"': "+x+".command})")
	return y

for l in sorted(listdir("./coms/")):
	print(l)

	open_file = open("./coms/"+l, 'r')
	read_file = open_file.read().splitlines()
	q = str(read_file[0]).split()
	print(len(q))
	x = q[0]
	if len(q) > 1:
		temp.write(write_this_true(x)+'\n\n')
	if len(q) == 1:
		temp.write(write_this_false(x)+'\n\n')
	open_file.close()

temp.close()