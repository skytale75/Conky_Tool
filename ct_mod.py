from ct_fun import *
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
configs_path = path.expanduser('~/Conky_Tool/configs/')
lua_path = path.expanduser('~/Conky_Tool/lua/')
options_path = path.expanduser('~/Conky_Tool/options/')
too_long = []
search_path = coms_path

custom_atttributes = ("color0 =", "color1 =", "color2 =", "color3 =", "color4 =",
"color5 =", "color6 =", "color7 =", "color8 =","color9 ="
"font0 =", "font1 =", "font2 =", "font3 =", "font4 =", "font5 ="
"font6 =", "font7 =", "font8 =", "font9 =")

def add_command(get_command, file_display):
	"""format text command into conky command and
	add to script at cursor location"""
	start_with = get_command.get("insert linestart", "end-1c")
	if "..." in start_with:
		for l in too_long:
			if start_with[0:-3] in str(l):
				then_format = "${"+l+"}"
				file_display.insert(INSERT, then_format)
	else:
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

def load_theme(get_theme_list, file_display, presets_window):
	"""get theme name from options menu and
	open corrisponding theme file in Conky_Themes"""
	theme = get_theme_list.get()
	theme_open = open(theme_path+theme, 'r')
	theme_read = theme_open.read()
	theme_open.close()
	presets_window.delete(0.0, END)
	file_display.delete(0.0, END)
	file_display.insert(INSERT, theme_read)

	theme_split = str(theme_read.split("$")[0])
	check_line = theme_split.splitlines()
	for l in custom_atttributes:
		for t in check_line:
			if l in t:
				presets_window.insert(INSERT, t+"\n")
	cb_syntax(presets_window)



def theme_list():
	""".themes.txt is a list of themes
	to feed to the themes drop down box"""

	if ".themes.txt" not in listdir(theme_path):
		make_tf = open(theme_path+".themes.txt", 'w')
		make_tf.write("test")
	else:
		pass

def read_theme_list():
	"""create theme list from .themes.txt file and
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
	theme_check = open(theme_path+".themes.txt", "r")
	check = theme_check.read()
	theme_check.close()
	if len(theme_name) != 0:
		if theme_name not in check:
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
	syntax_basic(output_window)
	fd_syntax_highlighting(output_window)
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
	font_output = ("${font "+name+":size="+size+"}")
	to_file.insert(INSERT, font_output)

def color_ct(color_i, output_f):
	'''get color from color textbox, and paste into
	file display in appropriate format'''

	users_input = color_i.get()
	users_input = users_input.replace('#', '')
	color = "${color "+users_input+"}"
	if len(users_input) == 6:
		output_f.insert(INSERT, color)

def search(csi, clo):
	"""search for input from command search bar and
	load filenames with matching results to command
	list"""
	if len(cs.results) == 0:
		for file in Path(search_path).glob('**/*.txt'): # change coms_path to search_path, change search path based on radiobuttn selection
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
	"""load commands list to commands window"""
	cs.results = []
	clo.delete(0.0, END)
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
		if len(command) > 23:
			if command not in too_long:
				too_long.append(command)
			clo.insert(INSERT, command[0:20]+"..."+'\n')
		if len(command) <= 23:
			clo.insert(INSERT, command+'\n')
		start += 1

def load_configs(clo):
	"""load configs to commands window"""
	cs.results = []
	clo.delete(0.0, END)
	for file in Path(main_path+"/configs").glob('**/*.txt'):
		open_file = open(file, 'r')
		read_file = open_file.read()
		open_file.close()
		cf_str = str(file)
		cf_spl = cf_str.split('/')
		cf = str(cf_spl[-1])
		cf = cf.replace('.txt', '')
		cs.results.append(cf+" "+read_file)
	configs_list = sorted(cs.results)
	start = 0
	while start < len(configs_list):
		config = str(configs_list[start]).split()[0]
		clo.insert(INSERT, config+"\n")
		start += 1

def load_lua(clo):
	"""load lua commands to commands window"""
	cs.results = []
	clo.delete(0.0, END)
	for file in Path(lua_path).glob('**/*.txt'):
		open_file = open(file, 'r')
		read_file = open_file.read()
		open_file.close()
		cf_str = str(file)
		cf_spl = cf_str.split('/')
		cf = str(cf_spl[-1])
		cf = cf.replace('.txt', '')
		cs.results.append(cf+" "+read_file)
	lua_list = sorted(cs.results)
	start = 0
	while start < len(lua_list):
		lua = str(lua_list[start]).split()[0]
		clo.insert(INSERT, lua+"\n")
		start += 1

def load_options(clo):
	"""load options text to wiki window"""
	clo.delete(0.0, END)
	open_file = open(options_path+"options.txt", 'r')
	read_file = open_file.read()
	open_file.close()
	clo.insert(INSERT, read_file)

def search_for(fd, word, tag):
	"""syntax highlighter template"""
	offset = '+%dc' % len(word)
	pos_start = fd.search(word, '1.0', END)
	while pos_start:
		pos_end = pos_start + offset
		fd.tag_add(tag, pos_start, pos_end)
		pos_start = fd.search(word, pos_end, END)

def syntax_basic(fd):
	"""generic syntax highlight for all commands"""
	fd.tag_config("{", foreground = "grey")
	file = fd.get(0.0, END).split("$", 1)
	if len(file) != 1:
		term = file[1].split("$")
		for t in term[1:len(term)]:
			if "{" in str(t):
				a = t[t.find("{"):t.find("}")+1]
				offset = '+%dc' % len(a)
				pos_start = fd.search(a, '1.0', END)
				while pos_start:
					pos_end = pos_start + offset
					fd.tag_add("{", pos_start, pos_end)
					pos_start = fd.search(a, pos_end, END)
	if len(file) == 1:
		pass

def search_for2(fd, word, tag):
	"""syntax highlighter template for
	complete commands from { to }"""
	term = str(fd.get(0.0, END)).split("$")
	for t in term[1:len(term)]:
		if word in str(t) and "{" in str(t):
			a = t[t.find("{"):t.find("}")+1]
			offset = '+%dc' % len(a)
			pos_start = fd.search(a, '1.0', END)
			while pos_start:
				pos_end = pos_start + offset
				fd.tag_add(tag, pos_start, pos_end)
				pos_start = fd.search(a, pos_end, END)
		if word in str(t) and "{" not in str(t):
			offset = '+%dc' % len(t)
			pos_start = fd.search(t, '1.0', END)
			while pos_start:
				pos_end = pos_start + offset
				fd.tag_add(tag, pos_start, pos_end)
				pos_start = fd.search(t, pos_end, END)

def fd_syntax_highlighting(fd):
	"""syntax highlighting for file display"""
	fd.tag_config("image", foreground = 'lightgreen')
	fd.tag_config("color", foreground = 'yellow')
	fd.tag_config("font", foreground = 'magenta')
	fd.tag_config("$", foreground = 'red')
	fd.tag_config("voffset", foreground = 'cyan')

	search_for(fd, "$", "$")

	search_for2(fd, "color", "color")
	search_for2(fd, "font", "font")
	search_for2(fd, "image", "image")
	search_for2(fd, "offset", "voffset")
	search_for2(fd, "alignc", "voffset")
	search_for2(fd, "alignr", "voffset")

def add_custom(attribute, file_display):
	"""get custom command and add it to the file"""
	line = attribute.get("insert linestart", "insert lineend")
	print(line)
	com = line.split()[0]
	file_display.insert(INSERT, "${"+com+"}")

def cb_syntax(attributes_box):
	the_color = ''
	get_list = attributes_box.get(0.0, END).splitlines()
	x = 1
	for l in get_list:
		if len(l) != 0 and x == 1:
			offset = '+%dc' % len(l)
			pos_start = attributes_box.search(l, '0.0', END)
			name = str(str(l).split()[0])
			attributes_box.tag_config(name, background=the_color)
			pos_end = pos_start + offset
			color = str(l).split()[2].replace("'", '')
			the_color = "#"+color[0:-1]
			attributes_box.tag_add(name, pos_start+"-1l", pos_end+"-1l")
			if "font" in str(l):
				x = 0

def get_theme(file_display, option_header, presets_window):
	load_theme(option_header, file_display, presets_window)
	syntax_basic(file_display)
	fd_syntax_highlighting(file_display)
	cb_syntax(presets_window)

def image_window(file_display):
    def rs_x(self):
        """resize y when x is changed"""
        resize_x(size_x, size_y)

    def rs_y(self):
        """resize x when y is changed"""
        resize_y(size_x, size_y)

    def pic_size(self):
        image_dimensions(image_entry, size_x, size_y)
        align_image_x.insert(INSERT, '0')
        align_image_y.insert(INSERT, '0')

    window = Tk()
    window.title("Add Image")
    window.grid()
    window.config(bg="white")
    window.attributes("-topmost", True)

    image_path_label = tk.Label(window, bg=cs.bgc, text="Image Path:")
    image_path_label.grid_configure(row=0, column=0, columnspan=3, sticky="NSEW")

    image_entry = tk.Entry(window, width=15)
    image_entry.grid_configure(row=1, column=0, columnspan=3, sticky="NSEW")

    size_label = tk.Label(window, bg=cs.bgc, text="size", justify="left", width=20)
    size_label.grid_configure(row=2, column=0, columnspan=1, sticky="NSEW")

    size_x = tk.Entry(window, width=5)
    size_x.grid_configure(row=2, column=1, sticky='NSE')

    size_y = tk.Entry(window, width=5)
    size_y.grid_configure(row=2, column=2, sticky='NSW')

    im_align = tk.Label(window, bg=cs.bgc, text="align", justify="left")
    im_align.grid_configure(row=3, column=0, columnspan=1, sticky="NSEW")

    align_image_x = tk.Entry(window, width=5)
    align_image_x.grid_configure(row=3, column=1, sticky='NSE')

    align_image_y = tk.Entry(window, width=5)
    align_image_y.grid_configure(row=3, column=2, sticky='NSW')

    enter_button = tk.Button(window, text="Enter")
    enter_button.grid_configure(row=4, column=0, sticky="W")

    exit_button = tk.Button(window, text="Exit", command=window.destroy)
    exit_button.grid_configure(row=4, column=2, sticky="E")

    enter_button.config(command=lambda: add_image(image_entry, size_x, size_y, align_image_x, align_image_y, file_display))

    image_entry.bind('<Return>', pic_size)
    size_x.bind('<Return>', rs_x)
    size_y.bind('<Return>', rs_y)

    window.mainloop()

def add_color_window():
	x=0
	color_name = ["color", "color0", "color1", "color2", "color3", "color4", "color5", "color6",
	"color7", "color8", "color9"]
	window = Tk()
	window.grid()
	window.title("Manage Colors")
	window.attributes("-topmost", True)
	for l in color_name:
		label = (l+"_label")
		win = (l+"_window")

		label = tk.Label(window, text=l+":")
		label.grid_configure(row=x, column=0)

		win = tk.Entry(window, width=8)
		win.grid_configure(row=x, column=1)

		x += 1
	update_button = tk.Button(window, text="update")
	update_button.grid_configure(row=11, column=0, columnspan=2, sticky='NSEW')
	window.mainloop()

def themes_window(file_display, presets_window):
	window = Tk()
	window.grid()
	window.title('Themes')
	window.attributes("-topmost", True)

	theme_name = tk.Label(window, bg=cs.bgc, text="Theme Name:")
	theme_name.grid_configure(row=0, column=0, columnspan=1)

	theme_display = tk.Entry(window)
	theme_display.grid_configure(row=0, column=1, columnspan=1, sticky="NSEW")

	save_theme_button = tk.Button(window, text="save theme", command=lambda: save_theme(theme_display, file_display))
	save_theme_button.grid_configure(row=0, column=2, columnspan=1, sticky="NSEW")

	open_theme_label = tk.Label(window, text="Open Theme:")
	open_theme_label.grid_configure(row=1, column=0, sticky='NSEW')

	theme_list = read_theme_list()
	option_header = tk.StringVar(window)
	option_header.set(theme_list[0])

	themes_list = tk.OptionMenu(window, option_header, *theme_list)
	themes_list.grid_configure(row=1, column=1, columnspan=1, sticky="NSEW")

	theme_button = tk.Button(window, text="Load")
	theme_button.grid_configure(row=1, column=2, columnspan=1, sticky="NSEW")
	theme_button.config(command=lambda: get_theme(file_display, option_header, presets_window))

	window.mainloop()

def font_window(file_display):
	window = Tk()
	window.grid()
	window.title('Fonts')
	window.attributes("-topmost", True)

	font_label = tk.Label(window, bg=cs.bgc, text="Font Name:")
	font_label.grid_configure(row=16, columnspan=1, sticky="NSW")

	fs_label = tk.Label(window, bg=cs.bgc, text="Size:")
	fs_label.grid_configure(row=16, column=3, columnspan=1, sticky="NSEW")

	open_font_list = open(main_path+".fontlist.txt", 'r')
	font_list = open_font_list.read().splitlines()
	open_font_list.close()
	font_list_header = tk.StringVar(window)
	font_list_header.set(font_list[0])

	fn_entry = tk.OptionMenu(window, font_list_header, *font_list)
	fn_entry.grid_configure(row=18, columnspan=2, sticky="NSEW")

	fs_entry = tk.Entry(window, width=5)
	fs_entry.grid_configure(row=18, column=2, columnspan=1, sticky="NSEW")

	font_submit = tk.Button(window, text="Enter")
	font_submit.grid_configure(row=18, column=3, columnspan=1, sticky="NSEW")
	font_submit.config(command=lambda: make_font(font_list_header, fs_entry, file_display))

	window.mainloop()
