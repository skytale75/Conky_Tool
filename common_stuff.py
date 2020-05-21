from os import listdir, path
from pathlib import Path

class Common_Stuff:
    '''variables and other stuff to carry
    throughout execution of commands'''
        
    # variables

    x = 0
    y = 0
    selected = 'commands'
    bgc = "#6B959E"

    temp_color = ''
    hold_command = ''
    hold_color = ''
    duplicate_hold = ''
    font_hold = ''

    # switches
    toggle = 0
    answer = ''
    editable = 'on'
    language = "english"

    # paths

    gui_names = path.expanduser('~/Conky_Tool/languages/'+language+"/gui_names.txt")

    the_color = ''
    uc_home_path = path.expanduser('~/Conky_Tool/')
    conky_config_path = path.expanduser('~/.config/conky/')
    user_home_path = path.expanduser('~/')
    theme_path = path.expanduser('~/Conky_Tool/Utilise_Conky/Conky_Themes/')
    user_theme_path = path.expanduser('~/.config/Utilise_Conky/Conky_Themes/')
    config_path = path.expanduser('~/.config/')

    configs_path = path.expanduser('~/Conky_Tool/languages/'+language+'/configs/')
    coms_path = path.expanduser('~/Conky_Tool/languages/'+language+'/coms/')
    help_path = path.expanduser('~/Conky_Tool/languages/'+language+'/help/')    
    lua_path = path.expanduser('~/Conky_Tool/languages/'+language+'/lua/')
    options_path = path.expanduser('~/Conky_Tool/languages/'+language+'/options/')
    config_file = conky_config_path+"conky.conf"
    search_path = coms_path

    # lists

    aliases = ("default_color =", "color0 =", "color1 =", "color2 =", "color3 =", "color4 =",
    "color5 =", "color6 =", "color7 =", "color8 =","color9 =",
    "font0 =", "font1 =", "font2 =", "font3 =", "font4 =", "font5 ="
    "font6 =", "font7 =", "font8 =", "font9 =")
    font_list = []
    dirty_list = []
    clean_list = []
    results = []
    current_colors = []
    color_aliass = ["default_color", "color0", "color1", "color2", "color3", "color4",
    "color5", "color6", "color7", "color8", "color9"]
    font_aliass = ["font0", "font1", "font2", "font3", "font4", "font5"
    "font6", "font7", "font8", "font9"]

    # file pieces

    open_file = open(config_file, 'r')
    read_open_file = open_file.read()
    split_open_file = read_open_file.split("\n}\n", 1)[0]
    config_section = split_open_file[0]
    config_split = config_section.splitlines()
    text_section = split_open_file[1]
    text_split = text_section.split("$")
    open_file.close()

    color_names = []
    color_codes = []

    color_dict = {}