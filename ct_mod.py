from ct_fun import *
from common_stuff import Common_Stuff as cs
from tkinter import *
from tkinter import simpledialog as sd
from os import listdir, path
from PIL import Image
from re import sub
from pathlib import Path
from gui_names import gui_names as gn
 

def duplicate_press(file_display):
    """duplicate line in file_display"""
    cs.duplicate_hold = file_display.get("insert linestart", "insert lineend")
    file_display.mark_set(INSERT, "insert lineend")
    file_display.insert("insert lineend", "\n"+cs.duplicate_hold)
    file_display.mark_set(INSERT, "insert linestart")

def color_separator():
    """seperate color names from color hex and build dictionary"""
    open_file = open(cs.options_path+"colornames.txt", 'r')
    read_file = open_file.read().splitlines()
    open_file.close()
    for line in read_file:
        color_split = line.split("*")
        color_name = str(color_split[1]).lower()
        color_code = color_split[0]
        cs.color_names.append(color_name)
        cs.color_codes.append(color_code)
        cs.color_dict.update({color_name: color_code})

def add_command(get_command, file_display):
    """format text command into conky command and
    add to script at cursor location"""
    start_with = get_command.get("insert linestart", "end-1c")
    then_format = "${"+start_with+"}"
    active_highlighting(file_display, then_format)
    file_display.insert(INSERT, then_format)

def add_CA(input_file, Custom_AB):
    """find custom attributes in file and list them in the
    custom attributes box"""

    split_file = input_file.splitlines()
    start = 0
    while start < len(split_file):
        for l in cs.aliases[0:10]:
            if l in split_file[start]:
                Custom_AB.insert(INSERT, split_file[start].strip()+"\n")
        start += 1

def conky_command(my_input, my_output):
    """compare user input to conky options and return
    possibilities"""

    the_input = my_input.get("insert linestart", "end-1c")
    if the_input in cs.functions:
        my_output.insert(INSERT, cs.functions[the_input])
    return 'break'

def load_conf(the_path, file_display, custom_AB):
    """ load conf file """

    open_file = open(the_path, 'r')
    read_file = open_file.read()
    open_file.close()
    add_CA(read_file, custom_AB)
    file_display.insert(INSERT, read_file)

def open_file(file_display, custom_AB):
    """look for current conky file
    and prepare it for editing and
    save as conky.conf, autoname 
    user_theme1"""

    if "conky.conf" in listdir(cs.conky_config_path):
        print("conky.conf found")
        the_path = cs.conky_config_path+"conky.conf"
        load_conf(the_path, file_display, custom_AB)
    elif ".conkyrc" in listdir(cs.user_home_path):
        print('.conkyrc found')
        the_path = cs.user_home_path+".conkyrc"
        load_conf(the_path, file_display, custom_AB)
    else:
        print("nothing found")

def load_theme(get_theme_list, file_display, presets_window):
    """get theme name from options menu and
    open corrisponding theme file in Conky_Themes"""
    theme = get_theme_list.get()
    if "Utilise_Conky" in listdir(cs.config_path):
        theme_open = open(cs.user_theme_path+theme, 'r')
        theme_read = theme_open.read()
        theme_open.close()
    if "Utilise_Conky" not in listdir(cs.config_path):
        theme_open = open(cs.theme_path+theme, 'r')
        theme_read = theme_open.read()
        theme_open.close()
    presets_window.delete(0.0, END)
    file_display.delete(0.0, END)
    file_display.insert(INSERT, theme_read)
    theme_split = str(theme_read.split("$")[0])
    check_line = theme_split.splitlines()
    for l in cs.color_aliass:
        for t in check_line:
            if l in t:
                t = str(t).strip()
                presets_window.insert(INSERT, t+"\n")
    cb_syntax(presets_window)

def theme_list():
    """.themes.txt is a list of themes
    to feed to the themes drop down box"""

    if ".themes.txt" not in listdir(cs.theme_path):
        make_tf = open(cs.theme_path+".themes.txt", 'w')
        make_tf.write("test")
    else:
        pass

def read_theme_list():
    """create theme list from .themes.txt file and
    apply to themes option menu"""
    if "Utilise_Conky" in str(listdir(cs.config_path)):
        print("user config file found . . .")
        open_theme_list = open(cs.user_theme_path+".themes.txt", 'r')
        read_theme_list = open_theme_list.read()
        open_theme_list.close()
        open_theme_list = open(cs.user_theme_path+".themes.txt", 'r')
        read_theme_list = open_theme_list.read()
        open_theme_list.close()
    if "Utilise_Conky" not in str(listdir(cs.config_path)):
        print("user config file not found . . .")
        open_theme_list = open(cs.theme_path+".themes.txt", 'r')
        read_theme_list = open_theme_list.read()
        open_theme_list.close()
        open_theme_list = open(cs.theme_path+".themes.txt", 'r')
        read_theme_list = open_theme_list.read()
        open_theme_list.close()
    end_theme_list = read_theme_list.split()
    return end_theme_list

def save_theme(get_theme_name, file_display):
    """get theme name from theme name entry widget
    add it to the .themes.txt file, and save file
    to the cs.theme_path"""
    theme_name = get_theme_name.get()
    theme_file = open(cs.theme_path+".themes.txt", "a")
    theme_check = open(cs.theme_path+".themes.txt", "r")
    check = theme_check.read()
    theme_check.close()
    if len(theme_name) != 0:
        if theme_name not in check:
            theme_file.write("\n"+theme_name)
        save_theme = open(cs.theme_path+theme_name, 'w')
        the_script = file_display.get(0.0, "end -1c")
        save_theme.write(the_script)
        save_theme.close()
    else:
        pass
    theme_file.close()

def save_file(file_display, Custom_AB):
    """open file and save to .conkyrc"""

    open_file = open(cs.conky_config_path+"conky.conf", "w")
    write_this = file_display.get(0.0, "end-1c")
    # file_display.delete(0.0, END)
    # file_display.insert(INSERT, write_this)
    Custom_AB.delete(0.0, END)
    add_CA(write_this, Custom_AB)
    cb_syntax(Custom_AB)
    syntax_basic(file_display)
    fd_syntax_highlighting(file_display)
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

def make_font(font_n, font_s, file_display):
    name = font_n.get()
    size = font_s.get()
    font_output = ("${font "+name+":size="+size+"}")
    file_display.insert(INSERT, font_output)

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
        for file in Path(cs.search_path).glob('**/*.txt'): # change cs.coms_path to cs.search_path, change search path based on radiobuttn selection
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
    for file in Path(cs.coms_path).glob('**/*.txt'):
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

def load_configs(clo):
    """load configs to commands window"""
    cs.results = []
    clo.delete(0.0, END)
    for file in Path(cs.configs_path).glob('**/*.txt'):
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
    for file in Path(cs.lua_path).glob('**/*.txt'):
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
    open_file = open(cs.options_path+"options.txt", 'r')
    read_file = open_file.read()
    open_file.close()
    clo.insert(INSERT, read_file)

def search_for(file_display, word, tag):
    """syntax highlighter template"""
    offset = '+%dc' % len(word)
    pos_start = file_display.search(word, '1.0', END)
    while pos_start:
        pos_end = pos_start + offset
        file_display.tag_add(tag, pos_start, pos_end)
        pos_start = file_display.search(word, pos_end, END)

def syntax_basic(file_display):
    """generic syntax highlight for all commands"""
    file_display.tag_config("{", foreground = "grey")
    file = file_display.get(0.0, END).split("$", 1)
    if len(file) != 1:
        term = file[1].split("$")
        for t in term[1:len(term)]:
            if "{" in str(t):
                a = t[t.find("{"):t.find("}")+1]
                offset = '+%dc' % len(a)
                pos_start = file_display.search(a, '1.0', END)
                while pos_start:
                    pos_end = pos_start + offset
                    file_display.tag_add("{", pos_start, pos_end)
                    pos_start = file_display.search(a, pos_end, END)
    if len(file) == 1:
        pass

def search_for2(file_display, word, tag):
    """syntax highlighter template for
    complete commands from { to }"""
    term = str(file_display.get(0.0, END)).split("$")
    for t in term[1:len(term)]:
        if word in str(t) and "{" in str(t):
            a = t[t.find("{"):t.find("}")+1]
            offset = '+%dc' % len(a)
            pos_start = file_display.search(a, '1.0', END)
            while pos_start:
                pos_end = pos_start + offset
                file_display.tag_add(tag, pos_start, pos_end)
                pos_start = file_display.search(a, pos_end, END)
        if word in str(t) and "{" not in str(t):
            offset = '+%dc' % len(t)
            pos_start = file_display.search(t, '1.0', END)
            while pos_start:
                pos_end = pos_start + offset
                file_display.tag_add(tag, pos_start, pos_end)
                pos_start = file_display.search(t, pos_end, END)

def fd_syntax_highlighting(file_display):
    """syntax highlighting for file display"""
    file_display.tag_config("image", foreground = 'lightgreen')
    file_display.tag_config("color", foreground = 'yellow')
    file_display.tag_config("font", foreground = 'magenta')
    file_display.tag_config("$", foreground = 'red')
    file_display.tag_config("voffset", foreground = 'cyan')

    search_for(file_display, "$", "$")

    search_for2(file_display, "color", "color")
    search_for2(file_display, "font", "font")
    search_for2(file_display, "image", "image")
    search_for2(file_display, "offset", "voffset")
    search_for2(file_display, "alignc", "voffset")
    search_for2(file_display, "alignr", "voffset")

def load_hold_color(attribute):
    attribute.tag_config("custom_BG", background="black")
    attribute.tag_remove("custom_BG", 0.0, END)
    attribute.tag_add("custom_BG", "insert linestart", "insert lineend")
    cs.hold_color = attribute.get("insert linestart", "insert lineend")

def add_custom(attribute, file_display):
    """get custom command and add it to the file"""
    line = cs.hold_color
    com = line.split()[0]
    file_display.insert(INSERT, "${"+com+"}")

def cb_syntax(attributes_box):
    """custom box add list items and syntax highlighting"""
    color_open = open(cs.options_path+"colornames.txt", 'r')
    color_file = color_open.read()
    color_open.close()
    get_list = attributes_box.get(0.0, "end-1c").splitlines()
    start = 0
    while start < len(get_list):
        name = str(str(get_list[start]).split()[0])
        color = str(get_list[start]).split()[2].replace("'", '').replace(",", '').capitalize()
        if color.lower() not in cs.color_names:
            cs.the_color = "#"+color
        if color.lower() in cs.color_names:
            cs.the_color = "#"+cs.color_dict[color.lower()]
        offset = '+%dc' % len(get_list[start])
        pos_start = attributes_box.search(get_list[start], '0.0', END)
        pos_end = pos_start + offset
        attributes_box.tag_config(name, foreground=str(cs.the_color))
        attributes_box.tag_add(name, pos_start, pos_end)
        start += 1

def get_theme(file_display, option_header, presets_window):
    """load theme and highlights"""
    load_theme(option_header, file_display, presets_window)
    syntax_basic(file_display)
    fd_syntax_highlighting(file_display)
    cb_syntax(presets_window)

def instructions_window():
    window = Tk()
    window.title(gn.win_ins)
    window.grid()
    window.config(bg='white')
    window.attributes("-topmost", True)

    dis_text = tk.Text(window, width=70, height=30)
    dis_text.grid_configure(row=0, column=0)

    open_in = open(cs.uc_home_path+"instructions.txt")
    instructions = open_in.read()
    open_in.close()

    dis_text.insert(INSERT, instructions)

    window.mainloop()

def image_window(file_display):
    """create image command window"""
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
    window.title(gn.win_image)
    window.grid()
    window.config(bg="white")
    window.attributes("-topmost", True)

    image_path_label = tk.Label(window, bg=cs.bgc, text="Image Path:")
    image_path_label.grid_configure(row=0, column=0, columnspan=3, sticky="NSEW")

    image_entry = tk.Entry(window, width=15)
    image_entry.grid_configure(row=1, column=0, columnspan=3, sticky="NSEW")

    size_label = tk.Label(window, bg=cs.bgc, text=gn.lbl_size, justify="left", width=20)
    size_label.grid_configure(row=2, column=0, columnspan=1, sticky="NSEW")

    size_x = tk.Entry(window, width=5)
    size_x.grid_configure(row=2, column=1, sticky='NSE')

    size_y = tk.Entry(window, width=5)
    size_y.grid_configure(row=2, column=2, sticky='NSW')

    im_align = tk.Label(window, bg=cs.bgc, text=gn.lbl_align, justify="left")
    im_align.grid_configure(row=3, column=0, columnspan=1, sticky="NSEW")

    align_image_x = tk.Entry(window, width=5)
    align_image_x.grid_configure(row=3, column=1, sticky='NSE')

    align_image_y = tk.Entry(window, width=5)
    align_image_y.grid_configure(row=3, column=2, sticky='NSW')

    enter_button = tk.Button(window, text=gn.btn_enter)
    enter_button.grid_configure(row=4, column=0, sticky="W")

    exit_button = tk.Button(window, text=gn.btn_exit, command=window.destroy)
    exit_button.grid_configure(row=4, column=2, sticky="E")

    enter_button.config(command=lambda: add_image(image_entry, size_x, size_y, align_image_x, align_image_y, file_display))

    image_entry.bind('<Return>', pic_size)
    size_x.bind('<Return>', rs_x)
    size_y.bind('<Return>', rs_y)

    window.mainloop()

def add_color_window(file_display, custom):
    """color management window"""
    def update(color_alias, field_entry, file_display):
        """enter new colors based on hex, if not hex locate
        color name in file and return hex code"""
        config_window = file_display.get(0.0, END)
        file_display.delete(0.0, END)
        file_split = config_window.split("conky.text")
        config_split = file_split[0].splitlines()
        the_rest = file_split[1]
        for line in config_split:
            if str(color_alias) not in str(line):
                file_display.insert(INSERT, line+"\n")
            if str(color_alias) in str(line):
                if field_entry.get().lower() in cs.color_names:
                    file_display.insert(INSERT, "    "+color_alias+" = '"+cs.color_dict[field_entry.get().lower()]+"',\n")
                if field_entry.get().lower() not in cs.color_names:
                    file_display.insert(INSERT, "    "+color_alias+" = '"+field_entry.get().replace("#", '')+"',\n")
        file_display.insert(INSERT, "conky.text"+the_rest)
        save_file(file_display, custom)

    window = Tk()
    window.grid()
    window.title(gn.win_colors)
    window.attributes("-topmost", True)
    file_colors = custom.get(0.0, "end-1c").splitlines()

    default_color_label = tk.Label(window, text="default_color")
    default_color_label.grid_configure(row=0, column=0, sticky="E")

    default_color_entry = tk.Entry(window, width=8)
    default_color_entry.grid_configure(row=0, column=1)    

    default_color_button = tk.Button(window, width=8, text=gn.btn_update, command=lambda: update("default_color", default_color_entry, file_display))
    default_color_button.grid_configure(row=0, column=2)
    
    color0_label = tk.Label(window, text="color0")
    color0_label.grid_configure(row=1, column=0, sticky="E")

    color0_entry = tk.Entry(window, width=8)
    color0_entry.grid_configure(row=1, column=1)

    color0_button = tk.Button(window, width=8, text=gn.btn_update, command=lambda: update("color0", color0_entry, file_display))
    color0_button.grid_configure(row=1, column=2)
 
    color1_label = tk.Label(window, text="color1")
    color1_label.grid_configure(row=2, column=0, sticky="E")

    color1_entry = tk.Entry(window, width=8)
    color1_entry.grid_configure(row=2, column=1)

    color1_button = tk.Button(window, width=8, text=gn.btn_update, command=lambda: update("color1", color1_entry, file_display))
    color1_button.grid_configure(row=2, column=2)
  
    color2_label = tk.Label(window, text="color2")
    color2_label.grid_configure(row=3, column=0, sticky="E")

    color2_entry = tk.Entry(window, width=8)
    color2_entry.grid_configure(row=3, column=1)

    color2_button = tk.Button(window, width=8, text=gn.btn_update, command=lambda: update("color2", color2_entry, file_display))
    color2_button.grid_configure(row=3, column=2)
   
    color3_label = tk.Label(window, text="color3")
    color3_label.grid_configure(row=4, column=0, sticky="E")

    color3_entry = tk.Entry(window, width=8)
    color3_entry.grid_configure(row=4, column=1)

    color3_button = tk.Button(window, width=8, text=gn.btn_update, command=lambda: update("color3", color3_entry, file_display))
    color3_button.grid_configure(row=4, column=2)
   
    color4_label = tk.Label(window, text="color4")
    color4_label.grid_configure(row=5, column=0, sticky="E")

    color4_entry = tk.Entry(window, width=8)
    color4_entry.grid_configure(row=5, column=1)

    color4_button = tk.Button(window, width=8, text=gn.btn_update, command=lambda: update("color4", color4_entry, file_display))
    color4_button.grid_configure(row=5, column=2)
    
    color5_label = tk.Label(window, text="color5")
    color5_label.grid_configure(row=6, column=0, sticky="E")

    color5_entry = tk.Entry(window, width=8)
    color5_entry.grid_configure(row=6, column=1)

    color5_button = tk.Button(window, width=8, text=gn.btn_update, command=lambda: update("color5", color5_entry, file_display))
    color5_button.grid_configure(row=6, column=2)
    
    color6_label = tk.Label(window, text="color6")
    color6_label.grid_configure(row=7, column=0, sticky="E")

    color6_entry = tk.Entry(window, width=8)
    color6_entry.grid_configure(row=7, column=1)

    color6_button = tk.Button(window, width=8, text=gn.btn_update, command=lambda: update("color6", color6_entry, file_display))
    color6_button.grid_configure(row=7, column=2)
    
    color7_label = tk.Label(window, text="color7")
    color7_label.grid_configure(row=8, column=0, sticky="E")

    color7_entry = tk.Entry(window, width=8)
    color7_entry.grid_configure(row=8, column=1)

    color7_button = tk.Button(window, width=8, text=gn.btn_update, command=lambda: update("color7", color7_entry, file_display))
    color7_button.grid_configure(row=8, column=2)
    
    color8_label = tk.Label(window, text="color8")
    color8_label.grid_configure(row=9, column=0, sticky="E")

    color8_entry = tk.Entry(window, width=8)
    color8_entry.grid_configure(row=9, column=1)

    color8_button = tk.Button(window, width=8, text=gn.btn_update, command=lambda: update("color8", color8_entry, file_display))
    color8_button.grid_configure(row=9, column=2)
    
    color9_label = tk.Label(window, text="color9")
    color9_label.grid_configure(row=10, column=0, sticky="E")

    color9_entry = tk.Entry(window, width=8)
    color9_entry.grid_configure(row=10, column=1)

    color9_button = tk.Button(window, width=8, text=gn.btn_update, command=lambda: update("color9", color9_entry, file_display))
    color9_button.grid_configure(row=10, column=2)

    for color in file_colors:
        name = color.split()[0]
        value = str(color.split()[2]).replace("'", '')
        entry_name = eval(name+"_entry")
        entry_name.insert(INSERT, value[0:-1])

    window.mainloop()

def help_window(help_file, help_title):
    def save_help():
        open_save = open(str(cs.help_path)+str(help_file), 'w')
        open_save.write(help_text.get(0.0, "end-1c"))
        open_save.close()

    help_window = Tk()
    help_window.grid()
    help_window.title(help_title)

    help_open = open(cs.help_path+help_file, 'r')
    help_read = help_open.read()
    help_open.close()

    help_text = tk.Text(help_window, width=70, height=20, wrap='word')
    help_text.grid(row=0, column=0)
    help_text.insert(INSERT, help_read)

    if cs.editable == 'on':
        help_save = tk.Button(help_window, text="save", command=save_help)
        help_save.grid_configure(row=1, column=0, sticky="W")

    help_exit = tk.Button(help_window, text=gn.btn_exit, command=help_window.destroy)
    help_exit.grid(row=1, column=0, sticky="E")

    help_window.mainloop()


def themes_window(file_display, presets_window):
    """create themes properties window"""
    window = Tk()
    window.grid()
    window.title(gn.win_themes)
    window.attributes("-topmost", True)

    theme_name = tk.Label(window, bg=cs.bgc, text=gn.lbl_theme_name)
    theme_name.grid_configure(row=0, column=0, columnspan=1)

    theme_display = tk.Entry(window)
    theme_display.grid_configure(row=0, column=1, columnspan=1, sticky="NSEW")

    save_theme_button = tk.Button(window, text=gn.btn_save_theme, command=lambda: save_theme(theme_display, file_display))
    save_theme_button.grid_configure(row=0, column=2, columnspan=1, sticky="NSEW")

    open_theme_label = tk.Label(window, text=gn.lbl_open_theme)
    open_theme_label.grid_configure(row=1, column=0, sticky='NSEW')

    theme_list = read_theme_list()
    option_header = tk.StringVar(window)
    option_header.set(theme_list[0])

    themes_list = tk.OptionMenu(window, option_header, *theme_list)
    themes_list.grid_configure(row=1, column=1, columnspan=1, sticky="NSEW")

    theme_button = tk.Button(window, text=gn.btn_load_theme)
    theme_button.grid_configure(row=1, column=2, columnspan=1, sticky="NSEW")
    theme_button.config(command=lambda: get_theme(file_display, option_header, presets_window))

    window.mainloop()

def font_window(file_display):
    """create font properties window"""
    window = Tk()
    window.grid()
    window.title(gn.win_fonts)
    window.attributes("-topmost", True)

    font_label = tk.Label(window, bg=cs.bgc, text=gn.lbl_font_name)
    font_label.grid_configure(row=16, columnspan=1, sticky="NSW")

    fs_label = tk.Label(window, bg=cs.bgc, text=gn.lbl_size)
    fs_label.grid_configure(row=16, column=3, columnspan=1, sticky="NSEW")

    open_font_list = open(cs.uc_home_path+".fontlist.txt", 'r')
    font_list = open_font_list.read().splitlines()
    open_font_list.close()
    font_list_header = tk.StringVar(window)
    font_list_header.set(font_list[0])

    fn_entry = tk.OptionMenu(window, font_list_header, *font_list)
    fn_entry.grid_configure(row=18, columnspan=2, sticky="NSEW")

    fs_entry = tk.Entry(window, width=5)
    fs_entry.grid_configure(row=18, column=2, columnspan=1, sticky="NSEW")

    font_submit = tk.Button(window, text=gn.btn_enter)
    font_submit.grid_configure(row=18, column=3, columnspan=1, sticky="NSEW")
    font_submit.config(command=lambda: make_font(font_list_header, fs_entry, file_display))

    window.mainloop()

def show_def(com_list_box, wiki_window,):
    """load definition in wiki window"""
    exceptions = ["else", "exec", "eval"] # exceptions are also python functions and cause problems
    if cs.selected == "commands": #         it just so happens they all start with an 'e' lol
        x = str(com_list_box.get("insert linestart", "insert lineend"))
        if x in exceptions:
            x = x.replace("e", "E", 1)
        the_input = eval(x)
        the_input.definition_out(wiki_window)
        com_list_box.tag_add("command", "insert linestart", "insert lineend")
    if cs.selected == "configs":
        x = str(com_list_box.get("insert linestart", "insert lineend"))
        defi_open = open(cs.configs_path+x+".txt", 'r')
        defi = defi_open.read()
        defi_open.close()
        wiki_window.delete(0.0, END)
        wiki_window.insert(INSERT, defi)

    cs.hold_command = x

    if cs.selected == "lua":
        pass
    if cs.selected == "options":
        pass