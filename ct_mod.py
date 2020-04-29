from ct_fun import conky_stuff
from tkinter import *
from os import listdir, path
from PIL import Image
from re import sub
from pathlib import Path

cs = conky_stuff

path1 = path.expanduser('~/.config/conky/')
path2 = path.expanduser('~/')
theme_path = path.expanduser('~/Conky_Tool/Conky_Themes/')
coms_path = path.expanduser('~/Conky_Tool/coms/')

custom_atttributes = ("color0 =", "color1 =", "color2 =", "color3 =", "color4 =",\
	"color5 =", "color6 =", "color7 =", "color8 =","color9 ="\
		"font0 =", "font1 =", "font2 =", "font3 =", "font4 =", "font5 ="\
			"font6 =", "font7 =", "font8 =", "font9 =")

def add_command(get_command, file_display):
	"""format text command into conky command and
	add to script at cursor location"""

	start_with = get_command.get("insert linestart", "end-1c")
	then_format = "${"+start_with+"}"
	file_display.insert(INSERT, then_format)

def add_CA(input_file, Custom_AB):
	"""find custom attributes in file and list them in the
	custom attributes box"""

	split_file = input_file.splitlines()
	start = 0
	while start < len(split_file):
		for l in custom_atttributes:
			if l in split_file[start]:
				Custom_AB.insert(INSERT, split_file[start].strip()+"\n")
		start += 1

def conky_command(my_input, my_output):
	"""compare user input to conky options and return
	possibilities"""

	cs = conky_stuff
	the_input = my_input.get("insert linestart", "end-1c")
	if the_input in cs.functions:
		my_output.insert(INSERT, cs.functions[the_input])
	return 'break'

def load_conf(the_path, output_window, custom_AB):
	""" load conf file """

	open_file = open(the_path, 'r')
	read_file = open_file.read()
	open_file.close()
	add_CA(read_file, custom_AB)
	output_window.insert(INSERT, read_file)

def open_file(output_window, custom_AB):
	"""look for current conky file
	and prepare it for editing and
	save as conky.conf, autoname 
	user_theme1"""

	if "conky.conf" in listdir(path1):
		print("conky.conf found")
		the_path = path1+"conky.conf"
		load_conf(the_path, output_window, custom_AB)
	elif ".conkyrc" in listdir(path2):
		print('.conkyrc found')
		the_path = path2+".conkyrc"
		load_conf(the_path, output_window, custom_AB)
	else:
		print("nothing found")

def load_theme(get_theme_list, file_display):
	"""get theme name from options menu and
	open corrisponding theme file in Conky_Themes"""

	theme = get_theme_list.get()
	theme_open = open(theme_path+theme, 'r')
	theme_read = theme_open.read()
	theme_open.close()
	file_display.delete(0.0, END)
	file_display.insert(INSERT, theme_read)


def theme_list():
	""".themes.txt is a list of themes
	to feed to the themes drop down box"""

	if ".themes.txt" not in listdir(theme_path):
		make_tf = open(theme_path+".themes.txt", 'w')
		make_tf.write("test")
	else:
		pass

def read_theme_list():
	"""create theme list fro .themes.txt file and
	apply to themes option menu"""

	open_theme_list = open(theme_path+".themes.txt", 'r')
	read_theme_list = open_theme_list.read()
	open_theme_list.close()
	end_theme_list = read_theme_list.split()
	return end_theme_list

def save_theme(get_theme_name, file_display):
	"""get theme name from theme name entry widget
	add it to the .themes.txt file, and save file
	to the theme_path"""

	theme_name = get_theme_name.get()
	theme_file = open(theme_path+".themes.txt", "a")
	if len(theme_name) != 0:
		theme_file.write("\n"+theme_name)
		save_theme = open(theme_path+theme_name, 'w')
		the_script = file_display.get(0.0, "end -1c")
		save_theme.write(the_script)
		save_theme.close()
	else:
		pass
	theme_file.close()

def save_file(output_window):
	"""open file and save to .conkyrc"""

	open_file = open(path1+"conky.conf", "w")
	write_this = output_window.get(0.0, "end-1c")
	open_file.write(write_this)
	open_file.close()

def add_image(ip, isx, isy, iax, iay, file_display):
	"""get image path and dimensions/placement from
	appropriate entry widgets, format and paste to
	file_display"""

	pst = "${image "+ip.get()+" (-p "+iax.get()+","+iay.get()+ " ) "+"(-s "+ isx.get()+ "x"+ isy.get()+ " )"+"}"
	file_display.insert(INSERT, pst)

def image_dimensions(i_path, image_x, image_y):
	"""get picture height and width and load"""

	get_ip = path.expanduser(i_path.get())
	im = Image.open(get_ip)
	image_x.insert(INSERT, im.size[0])
	image_y.insert(INSERT, im.size[1])
	cs.x = im.size[0]
	cs.y = im.size[1]

def resize_x(isx, isy):
	"""get new x dimension insert y dimension"""

	get_x = isx.get()
	mult = int(get_x) / int(cs.x)
	isy.delete(0, END)
	isy.insert(INSERT, int(cs.y*mult))

def resize_y(isx, isy):
	"""get new y dimension calculate x dimension"""

	get_y = isy.get()
	mult = int(get_y) / int(cs.y)
	isx.delete(0, END)
	isx.insert(INSERT, int(cs.x*mult))
dirty_list = []
clean_list = []

def font_list():
	"""go to directory, copy file names,
	convert them to font names"""

	for file in Path('/usr/share/fonts/truetype').glob('**/*.ttf'):
		dirty_list.append(file)
	start = 0
	while start < len(dirty_list):
		filename = str(dirty_list[start]).split('/')
		str_file = str(filename[-1])
		str_file = str_file.replace('.ttf', '').replace('.otf', '').replace('-', '')\
			.replace('Bold', '').replace('Italic', '').replace('Oblique', '')
		z = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', str_file)
		if z not in clean_list:
			clean_list.append(z)
		start += 1
	open_font_list = open(".fontlist.txt", 'w')
	for l in sorted(clean_list):
		open_font_list.write(l+"\n")
	open_font_list.close()

def make_font(font_n, font_s, to_file):
	name = font_n.get()
	size = font_s.get()
	font_output = ("{font "+name+":size="+size+"}")
	to_file.insert(INSERT, font_output)

def color_ct(color_i, output_f):
	'''get color from color textbox, and paste into
	file display in appropriate format'''

	users_input = color_i.get()
	users_input = users_input.replace('#', '')
	color = "{color "+users_input+"}"
	if len(users_input) == 6:
		output_f.insert(INSERT, color)

def search(csi, clo):
	"""search for input from command search bar and
	load filenames with matching results to command
	list"""
	if len(cs.results) == 0:
		for file in Path(coms_path).glob('**/*.txt'):
			open_file = open(file, 'r')
			read_file = open_file.read()
			open_file.close()
			cf_str = str(file)
			cf_spl = cf_str.split('/')
			cf = str(cf_spl[-1])
			cf = cf.replace('.txt', '')
			cs.results.append(cf+" "+read_file)
	clo.delete(0.0, END)
	for l in cs.results:
		x = str(l)
		if str(csi.get()) in x:
			humph = x.split()[0]
			clo.insert(INSERT, humph+'\n')

def load_commands(clo):
	cs.results == []
	for file in Path(coms_path).glob('**/*.txt'):
		open_file = open(file, 'r')
		read_file = open_file.read()
		open_file.close()
		cf_str = str(file)
		cf_spl = cf_str.split('/')
		cf = str(cf_spl[-1])
		cf = cf.replace('.txt', '')
		cs.results.append(cf+" "+read_file)
	command_list = sorted(cs.results)
	start = 0
	while start < len(command_list):
		command = str(command_list[start]).split()[0]
		clo.insert(INSERT, command+'\n')
		start += 1