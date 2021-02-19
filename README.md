# Conky_Tool

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

***required packages***

with apt . . .

sudo apt install python3-tk python3-pil python3-pil.imagetk
sudo apt install git

with pacman

sudo pacman -S git
sudo pacman -S tk

with yum

sudo yum install git
sudo yum install python36u-tkinter

***Download (Clone repository)***

everyone shit have git, if you don't you can install it
in your terminal . . . "sudo apt install git" and so on . . .

after you install . . . continue . . 

open terminal in home directory, copy/paste next line into
terminal and press enter.

git clone https://github.com/skytale75/Conky_Tool.git



***install***

1) Copy and paste the following line into your terminal
and press 'Enter'.


***sudo python3 ~/Conky_Tool/setup.py***


2) Run, type 'utilise' in the terminal and press enter.

***updates as of May 20, 2020***

1) Changed font selection . . . *
2) Fixed theme issues, they weren't saving properly.

***Things to come***

Will add font fields similar to the "color management" window
that will automatically load the font aliases into the appropriate
fields. Will also add a text box to display fonts in use that aren't
set toan alias for older versions of conky.

Going to change the images window, when you add an image and change the
alignment, it will automatically delete the old insertion, and re-enter
the image command with the new alignment values.

Working on a line to page concept, Control-p will take the line the 
cursor is currently on, and open a window with a text field into
its own page, each command will be on it's own line. When you push
submit, the line in the original will be deleted and the new page will
re-insert in in a single line. I think this will help keep the
conky.conf much easier to read. If you make no changes you can hit
a cancel button.

Update February 16th 2021

Decided to start working on the program again . . . if I am making it just for me that is fine lol.

Known Issues as of right now.

Adding fonts doesn't work right . . . the window will give you an accurate list of fonts but you have to ommit the underscores and words like (bold italic or condensed), the font names should match the file names, if you have font manager installed (I reccomend it big time) just look through the list to find out the right font names. Also, once you close the font window you can't open it again until restarting the program. I will be fixing this . . . 

