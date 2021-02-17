from ct_fun import Commands, active_highlighting
from common_stuff import Common_Stuff as cs
from tkinter import Label, END, INSERT
from tkinter import simpledialog as sd
from os import listdir, path
from PIL import Image
from re import sub
from pathlib import Path
from gui_names import gui_names as gn
import subprocess

def search_su(entry_name):
    if cs.toggle == 0:
        entry_name.delete(0, END)
        cs.toggle = 1

def duplicate_press(file_display):
    """duplicate line in file_display"""
    cs.duplicate_hold = file_display.get("insert linestart", "insert lineend")
    file_display.mark_set(INSERT, "insert lineend")
    file_display.insert("insert lineend", "\n"+cs.duplicate_hold)
    file_display.mark_set(INSERT, "insert linestart")

def color_separator():
    """separate color names from color hex and build dictionary"""
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

def add_cc(input_file, Custom_AB):
    """find custom colors in file and list them in the
    custom colors box"""

    split_file = input_file.splitlines()
    start = 0
    while start < len(split_file):
        for l in cs.aliases[0:10]:
            if l in split_file[start]:
                Custom_AB.insert(INSERT, split_file[start].strip()+"\n")
        start += 1

def load_conf(the_path, file_display, custom_AB):
    """ load conf file """

    open_file = open(the_path, 'r')
    read_file = open_file.read()
    open_file.close()
    if len(read_file) != 0:
        add_cc(read_file, custom_AB)
        file_display.insert(INSERT, read_file)
    if len(read_file) == 0:
        file_display.insert(INSERT, "file empty\nplease load theme.")

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
    open corresponding theme file in Conky_Themes"""
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
            if l in t and "-[[" not in t:
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
        open_theme_list = open(cs.user_theme_path+".themes.txt", 'r')
        read_theme_list = open_theme_list.read()
        open_theme_list.close()
        open_theme_list = open(cs.user_theme_path+".themes.txt", 'r')
        read_theme_list = open_theme_list.read()
        open_theme_list.close()
    if "Utilise_Conky" not in str(listdir(cs.config_path)):
        open_theme_list = open(cs.theme_path+".themes.txt", 'r')
        read_theme_list = open_theme_list.read()
        open_theme_list.close()
        open_theme_list = open(cs.theme_path+".themes.txt", 'r')
        read_theme_list = open_theme_list.read()
        open_theme_list.close()
    end_theme_list = read_theme_list.split()
    return end_theme_list

def theme_prompt(get_theme_name, file_display):
    """get theme name from theme name entry widget
    add it to the .themes.txt file, and save file
    to the cs.theme_path"""
    theme_name = get_theme_name.get()
    theme_file = open(cs.user_theme_path+".themes.txt", "a")
    theme_check = open(cs.user_theme_path+".themes.txt", "r")
    check_default = ["basic_example", "new_transparent"]
    check_added = theme_check.read()
    theme_check.close()
    if len(theme_name) != 0:
        if theme_name not in check_default and theme_name not in check_added:
            theme_file.write("\n"+theme_name)
            write_theme = open(cs.user_theme_path+theme_name, 'w')
            the_script = file_display.get(0.0, "end -1c")
            write_theme.write(the_script)
            write_theme.close()
        if theme_name in check_added and theme_name not in check_default:
            write_theme = open(cs.user_theme_path+theme_name, 'w')
            the_script = file_display.get(0.0, "end -1c")
            write_theme.write(the_script)
            write_theme.close()
        if theme_name in check_default:
            pass
    else:
        pass
    theme_file.close()

def save_file(file_display, Custom_AB):
    """open file and save to .conkyrc"""
    open_file = open(cs.conky_config_path+"conky.conf", "w")
    write_this = file_display.get(0.0, "end-1c")
    Custom_AB.delete(0.0, END)
    add_cc(write_this, Custom_AB)
    cb_syntax(Custom_AB)
    syntax_basic(file_display)
    fd_syntax_highlighting(file_display)
    open_file.write(write_this)
    open_file.close()

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
    font_list = []
    get = subprocess.Popen("fc-list", shell=True, stdout=subprocess.PIPE)
    read_output = str(get.stdout.read()).split("usr")
    for L in read_output:
        font = L.split(":")
        if len(font) > 1:
            print_font = str(font[1]).split(",")
            for f in print_font[1:]:
                if "\\x" not in str(print_font) and "\\u" not in str(print_font):
                    font_name = f.replace("|\\n/", "")
                    font_list.append(font_name)
    for l in sorted(font_list):
        if "\\" not in str(l) and len(l) > 2 and l not in cs.font_list:
            cs.font_list.append(l)

def make_font(font_n, font_s, file_display, cbl_window):
    name = font_n
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
        for file in Path(cs.search_path).glob('**/*.txt'): # change cs.coms_path to cs.search_path, change search path based on radio button selection
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

def add_image(ip, isx, isy, iax, iay, file_display, Custom_AB):
    """get image path and dimensions/placement from
    appropriate entry widgets, format and paste to
    file_display"""
    check = file_display.get("insert linestart", "insert lineend")
    if cs.image_toggle == "true" and "${image" in check:
        file_display.delete("insert linestart", "insert lineend")
    pst = "${image "+ip.get()+" (-p "+iax.get()+","+iay.get()+ " ) "+"(-s "+ isx.get()+ "x"+ isy.get()+ " )"+"}"
    cs.image_hold = pst
    file_display.insert(INSERT, pst)
    save_file(file_display, Custom_AB)

def image_from_line(file_display, file_path, size_x, size_y, align_x, align_y):
    current_line = file_display.get("insert linestart", "insert lineend")
    if "${image" in current_line:
        replace_list = ["${image", " (-p ", ",", ") (-s ", "x", " )}"]
        for replace in replace_list:
            current_line = current_line.replace(replace, ' ')
        split_line = current_line.split()
        file_path.insert(INSERT, split_line[0])
        size_x.insert(INSERT, split_line[3])
        cs.x = int(split_line[3])
        size_y.insert(INSERT, split_line[4])
        cs.y = int(split_line[4])
        align_x.insert(INSERT, split_line[1])
        align_y.insert(INSERT, split_line[2])

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
    if cs.hold_color != '':
        line = cs.hold_color
        com = line.split()[0]
        if com != "default_color":
            file_display.insert(INSERT, "${"+com+"}")
        if com == "default_color":
            file_display.insert(INSERT, "${color}")

def cb_syntax(attributes_box):
    """custom box add list items and syntax highlighting"""
    color_open = open(cs.options_path+"colornames.txt", 'r')
#    color_file = color_open.read()
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

def show_def(com_list_box, wiki_window,):
    """load definition in wiki window"""
    exceptions = ["else", "exec", "eval"] # exceptions are also python functions and cause problems
    if cs.selected == "commands": #         it just so happens they all start with an 'e' lol
        x = str(com_list_box.get("insert linestart", "insert lineend"))
        if x in exceptions:
            x = x.replace("e", "E", 1)
        defi_open = open(cs.coms_path+x+".txt", 'r')
        defi = defi_open.read()
        defi_open.close()
        wiki_window.delete(0.0, END)
        wiki_window.insert(INSERT, defi)
        com_list_box.tag_add("command", "insert linestart", "insert lineend")
    if cs.selected == "configs":
        x = str(com_list_box.get("insert linestart", "insert lineend"))
        defi_open = open(cs.configs_path+x+".txt", 'r')
        defi = defi_open.read()
        defi_open.close()
        wiki_window.delete(0.0, END)
        wiki_window.insert(INSERT, defi)
        com_list_box.tag_add("command", "insert linestart", "insert lineend")
    cs.hold_command = x

    if cs.selected == "lua":
        pass
    if cs.selected == "options":
        pass

def load_by_line(command_box, custom_box, file_display):
    """takes contents of line from nb.file_display and opens
    a window with each command on its own line"""
    cs.line_list = []
    load_line = file_display.get("insert linestart", "insert lineend")
    cs.line_hold = load_line
    
    format_this = cs.line_hold.split("$")
    for l in format_this:
        check = l.split("}")
        if len(check) > 1:
            if check[1] != '':
                cs.line_list.append("$"+check[0]+"}")
                cs.line_list.append(check[1])
            if check[1] == '':
                cs.line_list.append("$"+check[0]+"}")
        if len(check) == 1 and check[0] != '':
            cs.line_list.append("$"+check[0]+"}")

def cbl_update(cbl_text, command_box, custom_box, file_display):
    """updates current line of nb.file_display
    from conky by line window in appropriate format"""
    cs.line_list = cbl_text.get(0.0, END).splitlines()
    file_display.delete("insert linestart", "insert lineend")
    for line in cs.line_list:
        file_display.insert(INSERT, line)
    load_by_line(command_box, custom_box, file_display)
    save_file(file_display, custom_box)

def insert_line(cbl_text):
    cbl_text.delete(0.0, END)
    for line in cs.line_list:
        cbl_text.insert(INSERT, line+"\n")

def toggle_gb(file_display, custom_window):
    """toggles graph borders"""
    cs.file_list = file_display.get(0.0, "end-1c")
    true_false(file_display)
    file_display.delete(0.0, END)
    if cs.graph_border_toggle == -1:
        cs.file_list = cs.file_list.replace("draw_graph_borders = true,", "draw_graph_borders = false,")
    if cs.graph_border_toggle == 1:
        cs.file_list = cs.file_list.replace("draw_graph_borders = false,", "draw_graph_borders = true,")
    file_display.insert(INSERT, cs.file_list)
    cs.graph_border_toggle = cs.graph_border_toggle * -1
    save_file(file_display, custom_window)

def toggle_pb(file_display, custom_window):
    """toggles page_borders"""
    where = file_display.index(INSERT)
    print(where)
    cs.file_list = file_display.get(0.0, "end-1c")
    true_false(file_display)
    file_display.delete(0.0, END)
    if cs.page_border_toggle == -1:
        cs.file_list = cs.file_list.replace("draw_borders = true,", "draw_borders = false,")
    if cs.page_border_toggle == 1:
        cs.file_list = cs.file_list.replace("draw_borders = false,", "draw_borders = true,")
    file_display.insert(INSERT, cs.file_list)
    cs.page_border_toggle = cs.page_border_toggle * -1
    save_file(file_display, custom_window)
    file_display.see(where)
    file_display.mark_set("CURSOR", where)

def true_false(file_display):
    check = file_display.get(0.0, END).splitlines()
    for l in check:
        if "draw_borders" in str(l):
            if "true" in str(l):
                cs.page_border_toggle = -1
            if "false" in str(l):
                cs.page_border_toggle = 1
        if "draw_graph_borders" in str(l):
            if "true" in str(l):
                cs.graph_border_toggle = -1
            if "false" in str(l):
                cs.graph_border_toggle = 1