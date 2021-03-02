import os, shutil
from pathlib import Path

home_path = os.path.expanduser("~/")
bin_file_path = os.path.expanduser("~/bin")

if "bin" in os.listdir(home_path):
    print("Found '~/bin' directory . . .")
    os.chmod(bin_file_path, 0o777)
if "bin" not in os.listdir(home_path):
    print("'~/bin' directory not found, creating ~/bin directory . . .")
    os.mkdir(home_path+"bin")
    os.chmod(bin_file_path, 0o777)

conky_path = os.path.expanduser("~/.config/")

if "conky" in os.listdir(conky_path):
    print("Found 'conky' directory in '.config folder' . . .")
    os.chmod(conky_path+"conky", 0o777)
if "conky" not in os.listdir(conky_path):
    print("Creating 'conky' directory in '.config directory'")
    os.mkdir(conky_path+"conky")
    os.chmod(conky_path+"conky", 0o777)

config_file = "conky.conf"
config_path = os.path.expanduser("~/.config/conky/")

if config_file in os.listdir(config_path):
    print("'conky.conf' file found . . .\nchanging permissions . . .")
    os.chmod(config_path+config_file, 0o777)

if config_file not in os.listdir(config_path):
    print("no 'conky.conf' file found, creating one in '~/.config/conky/'")
    copy_file = open(os.path.expanduser("~/Conky_Tool/Utilise_Conky/Conky_Themes/basic_example"), 'r')
    read_copy = copy_file.read()
    copy_file.close()
    new_file = open(config_path+"conky.conf", 'w')
    new_file.write(read_copy)
    new_file.close()
    os.chmod(config_path+config_file, 0o777)

bin_path = os.path.expanduser("~/bin/")
utilise = os.path.expanduser("~/Conky_Tool/utilise")
user_utilise = os.path.expanduser("~/bin/utilise")

if "utilise" in os.listdir(bin_path):
    print("'utilise' command found in ~/bin")
    os.chmod(user_utilise, 0o777)
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
conky_themes_path = os.path.expanduser(utilise_path+"Conky_Themes/")
template_path = os.path.expanduser("~/Conky_Tool/Utilise_Conky/Conky_Themes/")

def the_copy(s_file):
    print("Creating "+s_file+" and adding permissions . . .")
    open_template = open(template_path+s_file, 'r')
    read_template = open_template.read()
    open_template.close()
    open_copy = open(conky_themes_path+s_file, 'w')
    open_copy.write(read_template)
    open_copy.close()
    os.chmod(conky_themes_path+s_file, 0o777)

check_file = os.listdir(template_path)

def check_and_change(s_file):
    if s_file in check_file:
        print("found "+s_file+". . . \nchanging permissions . . .\n")
        os.chmod(template_path+s_file, 0o777)
    if s_file not in check_file:
        the_copy(s_file)

if "Utilise_Conky" in os.listdir(conky_path):
    print("'Utilise_Conky' directory found in '~/.config' . . .\nchecking files . . .\nchanging permissions")
    os.chmod(conky_path+"Utilise_Conky", 0o777)
    check_and_change("basic_example")
    check_and_change("new_transparent")
    check_and_change(".fontlist.txt")
    check_and_change(".themes.txt")

if "Utilise_Conky" not in os.listdir(conky_path):
    print("'Utilise_Conky' directory not found in '~/.config', creating. . .")
    util_fol = os.path.expanduser("~/.config/"+"Utilise_Conky")
    os.mkdir(util_fol)
    os.chmod(util_fol, 0o777)
    os.mkdir(utilise_path+"Conky_Themes")
    os.chmod(utilise_path+"Conky_Themes", 0o777)
    the_copy("basic_example")
    the_copy("new_transparent")
    the_copy(".fontlist.txt")
    the_copy(".themes.txt")

print("\nscript completed . . . \n\nMake sure you have python3-tk installed . . .")
print("sudo apt install python3-tk\nor whatever is appropriate for your distro")
print("pip3 install willow")
print("pip3 install tcolorpicker")