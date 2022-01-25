# Conky_Tool

Conky Tool (Utilise Conky), is a program I decided to put
together to try to help make the process of making a conky
file easier for everyone. It isn't like conky manager, it
essentially is a text editor, with syntax highlighting that
has the entire catalogue of definitions built in, and ready
to add at the push of a button. It has a long way to go, but
I am looking for brave testers :).

# 1270x768

Contact Information

Facebook group for questions and answers is
https://www.facebook.com/groups/666099570622915

My email is skytale75@yandex.com, if you have any issues
installing this, please let me know, and paste any output
that may result in the terminal window into the file. I am
confident it will launch.

Current Program Status

finished all the basics

what you will be testing is not the finished product. There
are many more functions to add. This is simply the minimal
I was willing to do before I would allow it to be tested.

The Syntax highlighting is complete. The entire
wiki reference of command definitions is integrated and comes
up automatically as you are scrolling through them. You have
simple control-click functionality. There are very few
keyboard commands in reality, I think 8.

I won't tell you what is to come, first i need to determine
what you like and don't like about my program. Again, this
is not intended to write your file for you, but make it as
easy as possible for you to write your own file.

Every graphical eliment on the main window has a help file.
All you need to do to open it is press 'Controll + h'.

**_required packages_**

with apt . . .

sudo apt install python3-tk python3-pil python3-pil.imagetk git

with pacman

sudo pacman -S git
sudo pacman -S tk

with yum

sudo yum install git
sudo yum install python36u-tkinter

**_Download (Clone repository)_**

everyone should have git, if you don't you can install it
in your terminal . . . "sudo apt install git" and so on . . .

after you install . . . continue . .

open terminal in home directory, copy/paste next line into
terminal and press enter.

git clone https://github.com/skytale75/Conky_Tool.git

pip3 install tkcolorpicker

**_install_**

1. Copy and paste the following line into your terminal
   and press 'Enter'.

**_sudo python3 ~/Conky_Tool/setup.py_**

2. Run, type 'utilise' in the terminal and press enter.

**_updates as of May 20, 2020_**

1. Changed font selection . . . \*
2. Fixed theme issues, they weren't saving properly.

**_Things to come_**

Will add font fields similar to the "color management" window
that will automatically load the font aliases into the appropriate
fields. Will also add a text box to display fonts in use that aren't
set toan alias for older versions of conky.

Update February 16th 2021

Decided to start working on the program again . . . if I am making it just for me that is fine lol.

added tkcolorpicker to the file since it is difficult to find in some cases . . .
