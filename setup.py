import os, shutil
from pathlib import Path

home_path = os.path.expanduser("~/")
bin_file_path = os.path.expanduser("~/bin")

if "bin" in os.listdir(home_path):
    print("Found '~/bin' directory . . .")
if "bin" not in os.listdir(home_path):
    print("'~/bin' directory not found, creating ~/bin directory . . .")
    os.mkdir(home_path+"bin")
    os.chmod(bin_file_path, 0o777)

conky_path = os.path.expanduser("~/.config/")

if "conky" in os.listdir(conky_path):
    print("Found 'conky' directory in '.config folder' . . .")
if "conky" not in os.listdir(conky_path):
    print("Creating 'conky' directory in '.config directory'")
    os.mkdir(conky_path+"conky")

config_file = "conky.conf"
config_path = os.path.expanduser("~/.config/conky/")

if config_file in os.listdir(config_path):
    print("'conky.conf' file found . . .")
if config_file not in os.listdir(config_path):
    print("no 'conky.conf' file found, creating one in '~/.config/conky/'")
    copy_file = open(os.path.expanduser("~/Conky_Tool/Utilise_Conky/Conky_Themes/basic_example"), 'r')
    read_copy = copy_file.read()
    copy_file.close()
    new_file = open(config_path+"conky.conf", 'w')
    new_file.write(read_copy)
    new_file.close()

bin_path = os.path.expanduser("~/bin/")
utilise = os.path.expanduser("~/Conky_Tool/utilise")
user_utilise = os.path.expanduser("~/bin/utilise")

if "utilise" in os.listdir(bin_path):
    print("'utlize' command found in ~/bin")
if "utilise" not in os.listdir(bin_path):
    print("'utilise' command not found in '~/bin', creating file . . .")
    old_u = open(utilise, 'r')
    read_u = old_u.read()
    new_u = open(bin_path+"utilise", 'w')
    new_u.write(read_u)
    old_u.close()
    new_u.close()
    os.chmod(user_utilise, 0o777)

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
    print("'Utilise_Conky' directory found in '~/.config' . . .")
if "Utilise_Conky" not in os.listdir(conky_path):
    print("'Utilise_Conky' directory not found in '~/.config', creating. . .")
    os.mkdir(os.path.expanduser("~/.config/"+"Utilise_Conky"))
    os.mkdir(utilise_path+"Conky_Themes")
    the_copy("basic_example")
    the_copy("new_transparent")
    the_copy(".fontlist.txt")
    the_copy(".themes.txt")

print("\nscript completed . . . \n\nMake sure you have python3-tk installed . . .")
print("sudo apt install python3-tk\nor whatever is appropriate for your distro")