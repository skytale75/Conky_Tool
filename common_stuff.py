from os import listdir, path
from pathlib import Path

class Common_Stuff:
    '''variables to carry throughout execution of commands'''
        
    # variables

    x = 0
    y = 0
    selected = 'commands'
    bgc = "#6B959E"

    # paths
    the_color = ''
    uc_home_path = path.expanduser('~/Conky_Tool/')
    coms_path = path.expanduser('~/Conky_Tool/coms/')
    conky_config_path = path.expanduser('~/.config/conky/')
    user_home_path = path.expanduser('~/')
    theme_path = path.expanduser('~/Conky_Tool/Conky_Themes/')
 
    configs_path = path.expanduser('~/Conky_Tool/configs/')
    config_file = conky_config_path+"conky.conf"
    lua_path = path.expanduser('~/Conky_Tool/lua/')
    options_path = path.expanduser('~/Conky_Tool/options/')
    search_path = coms_path

    # lists

    aliases = ("default_color =", "color0 =", "color1 =", "color2 =", "color3 =", "color4 =",
    "color5 =", "color6 =", "color7 =", "color8 =","color9 =",
    "font0 =", "font1 =", "font2 =", "font3 =", "font4 =", "font5 ="
    "font6 =", "font7 =", "font8 =", "font9 =")
    dirty_list = []
    clean_list = []
    results = []
    current_colors = []

    # file pieces

    open_file = open(config_file, 'r')
    read_open_file = open_file.read()
    split_open_file = read_open_file.split("\n}\n", 1)[0]
    config_section = split_open_file[0]
    config_split = config_section.splitlines()
    text_section = split_open_file[1]
    text_split = text_section.split("$")
    open_file.close()