from ct_fun import active_highlighting
from common_stuff import Common_Stuff as cs
from tkinter import END, INSERT
from os import listdir, path
from PIL import Image
from pathlib import Path
import subprocess
from tkinter.filedialog import askopenfilename
from tkcolorpicker import askcolor

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
    open_color_file = open(cs.options_path+"colornames.txt", 'r')
    color_file = open_color_file.read().splitlines()
    open_color_file.close()
    for line in color_file:
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
                print(split_file[start].strip())
        start += 1

def add_cc_update(the_list, Custom_AB):
    """find custom colors in file and list them in the
    custom colors box"""
    if cs.color_toggle == 0:
        start = 0
        while start < len(the_list):
            for l in cs.aliases[0:10]:
                if l in the_list[start]:
                    print(l)
                    Custom_AB.insert(INSERT, the_list[start].strip()+"\n")
            start += 1

def load_conf(uc, the_path, file_display, custom_AB):
    """ load conf file """
    uc.file_display.tag_config("grey", background = "#201a09")
    open_file = open(the_path, 'r')
    read_file = open_file.read()
    open_file.close()
    x = 1
    if len(read_file) > 10:
        # add_cc(read_file, custom_AB)
        for line in read_file.splitlines():
            uc.file_display.insert(INSERT, line+"\n")
            x = x * -1
            if x == -1:
                print(x)
                uc.file_display.tag_add("grey", "insert-1l linestart", "insert-1l lineend")
    if len(read_file) == 0:
        uc.file_display.insert(INSERT, "file empty\nplease load theme.")

def open_file(uc, file_display, custom_AB):
    """look for current conky file
    and prepare it for editing and
    save as conky.conf, autoname 
    user_theme1"""
    if "conky.conf" in listdir(cs.conky_config_path):
        print("conky.conf found")
        the_path = cs.conky_config_path+"conky.conf"
        load_conf(uc, the_path, file_display, custom_AB)
    elif ".conkyrc" in listdir(cs.user_home_path):
        print('.conkyrc found')
        the_path = cs.user_home_path+".conkyrc"
        load_conf(uc, the_path, file_display, custom_AB)
    else:
        print("nothing found")

def load_theme(uc, get_theme_list, file_display, presets_window):
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
            print(t)
            if l in t and "-[[" not in t:
                t = str(t).strip()
                presets_window.insert(INSERT, t+"\n")
    # cb_syntax(presets_window)
    print(len(cs.ab_colors))
    add_cc_update(cs.ab_colors, uc.custom_window)

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

def check_file(file_display):
    get_text = file_display.get(0.0, END)
    if "$$" in get_text:
        get_text = get_text.replace("$$", "$")
        file_display.delete(0.0, END)
        file_display.insert(INSERT, get_text)
    if "}{" in get_text:
        get_text = get_text.replace("}{", "}${")
        file_display.delete(0.0, END)
        file_display.insert(INSERT, get_text)

def save_file(uc, file_display, Custom_AB):
    """open file and save to .conkyrc"""
    check_file(file_display)
    open_file = open(cs.conky_config_path+"conky.conf", "w")
    write_this = cs.ab_colors
    Custom_AB.delete(0.0, END)
    open_file.write(file_display.get(0.0, END))
    open_file.close() 
    add_cc_update(write_this, Custom_AB)
    load_the_colors(uc, file_display)
    print(cs.ab_colors)
    cb_syntax(Custom_AB)
    syntax_basic(file_display)
    fd_syntax_highlighting(file_display)

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
    get_fonts = subprocess.Popen("fc-list", shell=True, stdout=subprocess.PIPE)
    grab_output = str(get_fonts.stdout.read())

    temp_list = grab_output.split("share")
    for t in temp_list:
        c = t[t.find(': ')+2:t.find('=')-6]
        if len(c) != 0 and "\\" not in c:
            if "," not in c:
                font_list.append(c)
            if "," in c:
                split_c = c.split(",")
                for f in split_c:
                    font_list.append(f)

    for l in sorted(font_list):
        if "\\" not in str(l) and len(l) > 2 and l not in cs.font_list:
            cs.font_list.append(l)

def make_font(font_n, font_s, file_display, cbl_window):
    """format font and insert to file"""
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
            with open(file, 'r') as open_file:
                cs.results.append(f"{str(str(file).split('/')[-1]).replace('.txt', '')} {open_file.read()}")
    clo.delete(0.0, END)
    for list_result in cs.results:
        result = str(list_result)
        if str(csi.get()) in result:
            humph = result.split()[0]
            clo.insert(INSERT, humph+'\n')

def load_commands(clo):
    """load commands list to commands window"""
    cs.results = []
    clo.delete(0.0, END)
    for file in Path(cs.coms_path).glob('**/*.txt'):
        with open(file, 'r') as open_file:
            cs.results.append(f"{str(str(file).split('/')[-1]).replace('.txt', '')} {open_file.read()}")
        # read_file = open_file.read()
        # open_file.close()
        # cf_str = str(file)
        # cf_spl = cf_str.split('/')
        # cf = str(cf_spl[-1])
        # cf = cf.replace('.txt', '')
        # cs.results.append(cf+" "+read_file)
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
        with open(file, 'r') as open_file:
            cs.results.append(f"{str(str(file).split('/')[-1]).replace('.txt', '')}\
                 {open_file.read()}")
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
                if "{" and "}" in str(a) and "scroll" not in str(a):
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

def add_image(uc, ip, isx, isy, iax, iay, file_display, Custom_AB):
    """get image path and dimensions/placement from
    appropriate entry widgets, format and paste to
    file_display"""
    check = file_display.get("insert linestart", "insert lineend")
    if cs.image_toggle == "true" and "${image" in check:
        file_display.delete("insert linestart", "insert lineend")
    pst = "${image "+ip.get()+" (-p "+iax.get()+","+iay.get()+ " ) "+"(-s "+ isx.get()+ "x"+ isy.get()+ " )"+"}"
    cs.image_hold = pst
    file_display.insert(INSERT, pst)
    save_file(uc, file_display, Custom_AB)

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
    attribute.tag_config("custom_BG", background="black", foreground="red")
    attribute.tag_remove("custom_BG", 0.0, END)
    attribute.tag_add("custom_BG", "insert linestart", "insert lineend-9c")
    cs.hold_color = attribute.get("insert linestart", "insert lineend")

def add_custom(attribute, file_display, x):
    """get custom command and add it to the file"""
    if cs.hold_color != '':
        line = cs.hold_color
        com = line.split()[0]
        if com != "default_color":
            file_display.insert(INSERT, "${"+com+"}")
        if com == "default_color":
            file_display.insert(INSERT, "${color}")
    if x == 1:
        return 'break'

def cb_syntax(attributes_box):
    """custom box add list items and syntax highlighting"""
    color_open = open(cs.options_path+"colornames.txt", 'r')
    def add_color(attributes_box):
        start = 0
        while start < len(get_list):
            name = str(str(get_list[start]).split()[0])
            color = str(get_list[start]).split()[2].replace("'", '').replace(",", '').capitalize()
            print(color)
            if color.lower() not in cs.color_names:
                cs.the_color = "#"+color
            if color.lower() in cs.color_names:
                cs.the_color = "#"+cs.color_dict[color.lower()]
            offset = '+%dc' % len(get_list[start])
            pos_start = attributes_box.search(get_list[start], '0.0', END)
            pos_end = pos_start + offset
            print("pos_start", get_list[start], '-', pos_end)
            print(cs.the_color)
            if "''" not in str(get_list[start]):
                attributes_box.tag_config(name, background=str(cs.the_color))
                attributes_box.tag_add(name, pos_start, pos_end)
            if "''" in str(get_list[start]):
                attributes_box.tag_config(name, background="#555555")
                attributes_box.tag_add(name, pos_start, "7.0+19c")
            start += 1

    color_open.close()
    if len(cs.ab_colors) != 0:
        attributes_box.delete(0.0, END)
        for item in cs.ab_colors:
            attributes_box.insert(INSERT, item+"\n")
        get_list = attributes_box.get(0.0, "end-1c").splitlines()
        add_color(attributes_box)

def get_theme(uc, file_display, option_header, presets_window):
    """load theme and highlights"""
    load_theme(uc, option_header, file_display, presets_window)
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

def cbl_update(uc, cbl_text, command_box, custom_box, file_display):
    """updates current line of nb.file_display
    from conky by line window in appropriate format"""
    cs.line_list = cbl_text.get(0.0, END).splitlines()
    file_display.delete("insert linestart", "insert lineend")
    for line in cs.line_list:
        file_display.insert(INSERT, line)
    load_by_line(command_box, custom_box, file_display)
    save_file(uc, file_display, custom_box)

def insert_line(cbl_text):
    cbl_text.delete(0.0, END)
    for line in cs.line_list:
        cbl_text.insert(INSERT, line+"\n")

def toggle_gb(uc, file_display, custom_window):
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
    save_file(uc, file_display, custom_window)

def toggle_pb(uc, file_display, custom_window):
    """toggles page_borders"""
    where = file_display.index(INSERT)
    cs.file_list = file_display.get(0.0, "end-1c")
    true_false(file_display)
    file_display.delete(0.0, END)
    if cs.page_border_toggle == -1:
        cs.file_list = cs.file_list.replace("draw_borders = true,", "draw_borders = false,")
    if cs.page_border_toggle == 1:
        cs.file_list = cs.file_list.replace("draw_borders = false,", "draw_borders = true,")
    file_display.insert(INSERT, cs.file_list)
    cs.page_border_toggle = cs.page_border_toggle * -1
    save_file(uc, file_display, custom_window)
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

def load_the_colors(uc, get_from="fd"):
    ccl = []
    if get_from == "list":
        ccl=cs.ab_colors
    if get_from =="fd":
        make_from_widget = uc.file_display.get(0.0, END).splitlines
        for l in make_from_widget:
            if "    default_color =" in str(l):
                cs.ab_colors.append(str(l).strip())
            if "    color" in str(l) and "=" in str(l):
                cs.ab_colors.append(str(l).strip())
        ccl=cs.ab_colors
    if get_from == "file":
        get_from_file = open(cs.config_file, 'r')
        make_from_file = get_from_file.read().splitlines()
        get_from_file.close()
        for l in make_from_file:
            if "    default_color =" in str(l):
                cs.ab_colors.append(str(l).strip())
            if "    color" in str(l) and "=" in str(l):
                cs.ab_colors.append(str(l).strip())
        ccl=cs.ab_colors
        cs.color_toggle = 1
    return ccl

def update_colors(uc):
    uc.custom_window.delete(0.0, END)
    current_config = uc.file_display.get(0.0, END) #
    upper_config = current_config.split("conky.text")[0].splitlines() #
    lower_config = "conky.text" + current_config.split("conky.text")[1]
    new_config = []
    cs.ab_colors = [] #
    for line in upper_config:
        for item in cs.color_aliass:
            alias = str(item.split()[0])
            if str(alias) not in str(line) and str(line) not in new_config and "  color" not in str(line) and "default_color =" not in str(line) and "-[[color" not in str(line):
                new_config.append(line)
            if str(alias) in str(line) and line not in new_config:
                color = str("uc."+item+"_entry")
                grab_color = eval(color).get()
                new_config.append("    "+item+" = '"+grab_color+"',")
                cs.ab_colors.append(item+" = '"+grab_color+"',")
    uc.file_display.delete(0.0, END)
    for f in new_config:
        uc.file_display.insert(INSERT, f+"\n")
    uc.file_display.insert(INSERT, lower_config)
    save_file(uc, uc.file_display, uc.custom_window)
    add_cc_update(cs.ab_colors, uc.custom_window)
    update_gui(uc, cs.ab_colors)

def update_gui(uc, color_list):
    for color in color_list:
        if "''" not in str(color):
            name = "uc."+color.split()[0]
            value = str(color.split()[2][1:-2])
            entry_name = eval(name+"_entry")
            entry_name.delete(0, END)
            entry_name.insert(INSERT, value)
            button_name = eval(name+"_button")
            button_name.config(bg="#"+value)
            label_name = eval(name+"_chooser")
            label_name.config(bg='#'+value)

def color_chooser(color_out, mbutton):
    if color_out.get() != "":
        grab_color = color_out.get()
        color_code = askcolor("#"+grab_color, title ="Choose color")
        if "None" not in str(color_code):
            color_out.delete(0, END)
            color_out.insert(INSERT, color_code[1][1:])
            mbutton.config(bg=color_code[1])
    if color_out.get() == "":
        color_code = askcolor("#F3F3F3")
        color_out.insert(INSERT, color_code[1][1:])
        mbutton.config(bg=color_code[1])

def filter_color_list(uc, read_colors):
    color_list = []
    if len(read_colors.splitlines()) == 1:
        color_list = read_colors.replace(",", " ").replace("#", "").split()
    if len(read_colors.splitlines()) > 1:
        color_list = read_colors.replace(",", " ").replace("#", "").split()
    finish = 0
    while finish < len(color_list):
        chooser = eval("uc.color"+str(finish)+"_chooser")
        the_entry = eval("uc.color"+str(finish)+"_entry")
        chooser.config(bg="#"+color_list[finish])
        the_entry.delete(0, END)
        the_entry.insert(INSERT, color_list[finish])
        finish = finish + 1

def open_color_file(uc):
    name = askopenfilename(initialdir="~/Documents/")
    if len(name) != 0:
        open_file = open(name, 'r')
        read_colors = open_file.read()
        open_file.close()
        filter_color_list(uc, read_colors)

def open_color_dialog(uc):
    read_colors = uc.import_dialog.get(0.0, END)
    if len(read_colors) > 5:
        filter_color_list(uc, read_colors)
    if len(read_colors) < 5:
        uc.import_dialog.insert(INSERT, "Add list of colors here . . .")