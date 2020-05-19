import os, shutil
from pathlib import Path

home_path = os.path.expanduser("~/")

if "bin" in os.listdir(home_path):
    pass
if "bin" not in os.listdir(home_path):
    os.mkdir(home_path+"bin")

conky_path = os.path.expanduser("~/.config/")

if "conky" in os.listdir(conky_path):
    pass
if "conky" not in os.listdir(conky_path):
    os.mkdir(conky_path+"conky")

config_file = "conky.conf"
config_path = os.path.expanduser("~/.config/conky/")

if config_file in os.listdir(config_path):
    pass
if config_file not in os.listdir(config_path):
    copy_file = open(os.path.expanduser("~/Conky_Tool/Utilise_Conky/Conky_Themes/basic_example"), 'r')
    read_copy = copy_file.read()
    copy_file.close()
    new_file = open(config_path+"conky.conf", 'w')
    new_file.write(read_copy)
    new_file.close()

bin_path = os.path.expanduser("~/bin/")
utilise = os.path.expanduser("~/Conky_Tool/utilise")

if "utilise" in os.listdir(bin_path):
    pass
if "utilise" not in os.listdir(bin_path):
    old_u = open(utilise, 'r')
    read_u = old_u.read()
    new_u = open(bin_path+"utilise", 'w')
    new_u.write(read_u)
    old_u.close()
    new_u.close()

utilise_path = os.path.expanduser("~/.config/Utilise_Conky/")
conky_themes_path = os.path.expanduser(utilise_path+"/Conky_Themes/")
template_path = os.path.expanduser("~/Conky_Tool/Utilise_Conky/Conky_Themes/")

def the_copy(s_file):
    open_template = open(template_path+s_file, 'r')
    read_template = open_template.read()
    open_template.close()
    open_copy = open(conky_themes_path+s_file, 'w')
    open_copy.write(read_template)
    open_copy.close()

if "Utilise_Conky" in os.listdir(conky_path):
    pass
if "Utilise_Conky" not in os.listdir(conky_path):
    os.mkdir(os.path.expanduser("~/.config/"+"Utilise_Conky"))
    os.mkdir(utilise_path+"Conky_Themes")
    the_copy("basic_example")
    the_copy("new_transparent")
    the_copy(".fontlist.txt")
    the_copy(".themes.txt")