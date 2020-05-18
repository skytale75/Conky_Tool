# Conky_Tool

Contact Information

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

***Download (Clone repository)***

open terminal in home directory, copy/paste next line into
terminal and press enter.

git clone https://github.com/skytale75/Conky_Tool.git

note: if the terminal says git isn't installed use your systems
package manager to install git. In apt you would type . . .

sudo apt install git

***updated***

2 things i forgot . . .
open terminal
type 'ls' (no quotes) and hit enter, look for a folder named 'bin'.
if the folder is not there, type copy and paste the next line.

***mkdir bin***

next, copy and paste the next line

***cd ~/.config***

type 'ls -a' and hit enter, if you do not see a conky file then do the following
one line at a time

***mkdir conky***

***cd ~/Conky_Tool/Utilise_Conky/Conky_Themes***

***cp basic_example ~/.config/conky/conky.conf***


***Install***
in the terminal . . .
make sure you are in the home directory, if not, just type cd and
press enter.

1) The Conky_Tool file should have cloned directly into your home file.
If it doesn't (I am new to the github repository) move it there.

2) Inside the Conky_Tool directory, there is a file called "utilise".
Copy that to the ~/bin direcory. Copy and paste the following 2 lines
into the terminal, one at a time.

***cd ~/Conky_Tool***

***cp utilise ~/bin/utilise***

3) Navigate to the bin file and execute chmod +x utilise,
copy and paste the following 2 lines into the terminal one at
a time.

***cd ~/bin***

***chmod +x utilise***

4) Copy the "Utilise_Conky" folder from inside of the "Conky_Tool"
folder by copying and pasting the next 2 lines into your terminal,
one at a time. Press enter after each.

***cd ~/Conky_Tool***

***cp -r Utilise_Conky ~/.config/Utilise_Conky***

5) Type utilise into the terminal window to launch Utilise Conky.
