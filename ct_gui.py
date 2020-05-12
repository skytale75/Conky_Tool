from tkinter import *
import tkinter as tk
from tkinter import ttk
from ct_fun import *
from ct_mod import *
from os import listdir
from PIL import Image

# main file for Scrapbook

class Notebook:

    def __init__(self, title):
        self.root = Tk()
        self.root.title(title)
        self.root.bind('<Control-q>', exit)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.grid(row = 1, column = 0, rowspan = 50,
            columnspan = 49, sticky = 'NESW')

        rows = 0
        while rows < 50:
            self.root.rowconfigure(rows, weight = 1)
            self.root.columnconfigure(rows, weight = 1)
            rows += 1

    def create_widgets(self, title):
        """create all widgets"""
        nb.frame = tk.Frame(self.notebook)
        nb.frame.grid(row = 1, sticky='NSEW')
        self.notebook.add(nb.frame,text=title)
        nb.frame.columnconfigure(0, weight = 0)
        nb.frame.columnconfigure(1, weight = 0)
        nb.frame.columnconfigure(2, weight = 0)
        nb.frame.columnconfigure(3, weight = 0)
        nb.frame.columnconfigure(15, weight = 10)
        nb.frame.rowconfigure(1, weight = 0)
        nb.frame.rowconfigure(7, weight = 10)
        nb.frame.rowconfigure(3, weight = 0)
        nb.frame.config(bg=cs.bgc)

        nb.v =IntVar()

        def cr_com():
            search_path = coms_path
            cs.selected = "commands"
            load_commands(nb.com_list_box)

        def cr_con():
            search_path = configs_path
            cs.selected = "configs"
            load_configs(nb.com_list_box)

        def cr_lua():
            search_path = lua_path
            cs.selected = "lua"
            load_lua(nb.com_list_box)

        def cr_options():
            search_path = options_path
            cs.selected = "options"
            nb.com_list_box.delete(0.0, END)
            load_options(nb.wiki_window)
        
        nb.com_radio = tk.Radiobutton(nb.frame, indicatoron=0, width=20, bg=cs.bgc, text='commands', variable=nb.v, value=1, command = cr_com)
        nb.com_radio.grid_configure(row=0, column=0, columnspan=4, sticky="NSEW")
        nb.com_radio.select()

        nb.con_radio = tk.Radiobutton(nb.frame, indicatoron=0, width=20, bg=cs.bgc, text='configs', variable=nb.v, value=2, command = cr_con)
        nb.con_radio.grid_configure(row=1, column=0, columnspan=4, sticky="NSEW")

        nb.lua_radio = tk.Radiobutton(nb.frame, indicatoron=0, width=20, bg=cs.bgc, text='lua', variable=nb.v, value=3, command = cr_lua)
        nb.lua_radio.grid_configure(row=2, column=0, columnspan=4, sticky="NSEW")

        nb.options_radio = tk.Radiobutton(nb.frame, indicatoron=0, width=20, bg=cs.bgc, text='options', variable=nb.v, value=4, command = cr_options)
        nb.options_radio.grid_configure(row=3, column=0, columnspan=4, sticky="NSEW")

        nb.find_label = tk.Label(nb.frame, bg=cs.bgc, text="Search:")
        nb.find_label.grid_configure(row=0, column=4, columnspan=1)

        # row 1 coumn 0

        nb.command_find = tk.Entry(nb.frame, bg="darkblue", fg="white", font= ('Deja Vu Serif', 10))
        nb.command_find.grid_configure(row=0, column=5, columnspan=5, sticky="NSEW")

        # row 2 column 0

        nb.com_label = tk.Label(nb.frame, bg=cs.bgc, text="Commands", justify="left")
        nb.com_label.grid_configure(row=4, column=0, columnspan=5)

        # row 2 column 10

        nb.conky_label = tk.Label(nb.frame, bg=cs.bgc, text="~/.config/conky/conky.conf", justify='left')
        nb.conky_label.grid_configure(row=0, column=10, columnspan=10)

        # row 3 column 0

        nb.com_list_box = tk.Text(nb.frame, height=10, width=25, bg="lightblue", font= ('Deja Vu Serif', 10))
        nb.com_list_box.grid_configure(row=5, column=0, columnspan=5, sticky="NSEW")

        nb.file_display = tk.Text(nb.frame, width=50, wrap = 'word')
        nb.file_display.grid_configure(row=1, column=10, columnspan=10, rowspan=7, sticky="NSEW")
        nb.file_display.config(bg="black", fg="white", insertbackground = 'cyan', font= ('Deja Vu Serif', 10))

        # row 4

        nb.wiki_label = tk.Label(nb.frame, bg=cs.bgc, text="Description")
        nb.wiki_label.grid_configure(row=6, column=0, columnspan=10)

        # row 5

        nb.wiki_window = tk.Text(nb.frame, height=10, wrap='word', width=25, bg = "lightyellow", font= ('Deja Vu Serif', 10))
        nb.wiki_window.grid_configure(row=7, column=0, columnspan=10, sticky="NSEW")

        # row 7

        nb.color_button = tk.Button(nb.frame, text="Colors", command=lambda: add_color_window())
        nb.color_button.grid_configure(row=8, column=0, columnspan=2, sticky="NESW")

        nb.fonts_button = tk.Button(nb.frame, text='Fonts', command=lambda: font_window(nb.file_display))
        nb.fonts_button.grid_configure(row=8, column=2, columnspan=2, sticky='NSEW')

        nb.image_button = tk.Button(nb.frame, text="Add Image", command =lambda: image_window(nb.file_display))
        nb.image_button.grid_configure(row=8, column=4, columnspan=2, sticky="NSEW")

        # row 8

        nb.custom = tk.Label(nb.frame, bg=cs.bgc, text="Custom")
        nb.custom.grid_configure(row=4, column=5, columnspan=5)

        # row 9

        nb.custom_window = tk.Text(nb.frame, height=10, width=25, wrap="word", bg="darkgrey", fg="cyan")
        nb.custom_window.grid_configure(row=5, column=5, columnspan=5, sticky="NWSE")
        def themes_command(self):
            themes_window(nb.file_display, nb.custom_window)

        nb.themes_button = tk.Button(nb.frame, text='Themes', command=lambda: themes_command(self))
        nb.themes_button.grid_configure(row=8, column=14, columnspan=2, sticky='NSE')

        nb.save_button = tk.Button(nb.frame, width=10, text="Save", fg='red', command=lambda: save_file(nb.file_display))
        nb.save_button.grid_configure(row=8, column=16, columnspan=2, sticky='NSEW')

        nb.quit = tk.Button(nb.frame, width=10, text="QUIT", fg="red", command=self.root.destroy)
        nb.quit.grid_configure(row=8, column=18, columnspan=2, sticky='NSEW')

        def command_line(self):
            if cs.selected == "commands":
                the_input = str(nb.com_list_box.get("insert linestart", "insert lineend"))
                if "..." not in the_input:
                    functions[the_input](nb.file_display)
                if "..." in the_input:
                    for l in too_long:
                        if the_input[0:-3] in str(l):
                            functions[l](nb.file_display)
            return 'break'

        def show_def(self):
            """load definition in wiki window"""
            exceptions = ["else", "exec", "eval"] # exceptions are also python functions and cause problems
            if cs.selected == "commands": #         it just so happens they all start with an 'e' lol
                x = str(nb.com_list_box.get("insert linestart", "insert lineend"))
                if x in exceptions:
                    x = x.replace("e", "E", 1)
                if "..." not in x:
                    the_input = eval(x)
                    the_input.definition_out(nb.wiki_window)
                if "..." in x:
                    for l in too_long:
                        if x[0:-3] in str(l):
                            the_input = eval(l)
                            the_input.definition_out(nb.wiki_window)
                nb.com_list_box.tag_add("command", "insert linestart", "insert lineend")
            if cs.selected == "configs":
                x = str(nb.com_list_box.get("insert linestart", "insert lineend"))
                defi_open = open(configs_path+x+".txt", 'r')
                defi = defi_open.read()
                defi_open.close()
                nb.wiki_window.delete(0.0, END)
                nb.wiki_window.insert(INSERT, defi)
            if cs.selected == "lua":
                pass
            if cs.selected == "options":
                pass

        def ps_command(self):
            """tie into add_custom"""
            add_custom(nb.custom_window, nb.file_display)
            return 'break'

        def search_com(self):
            if nb.command_find.get() == '':
                conky_stuff.results = []
                nb.com_list_box.delete(0.0, END)
                load_commands(nb.com_list_box)
            else:
                search(nb.command_find, nb.com_list_box)

        def force_def(self):
            Commands.force_file(self, nb.wiki_window, nb.file_display)

        def clear_tag(self):
            nb.com_list_box.tag_remove("command", 0.0, END)

        nb.com_list_box.tag_config("command", background="white")
        nb.com_list_box.bind('<KeyRelease-Down>', show_def)
        nb.com_list_box.bind('<Down>', clear_tag)
        nb.com_list_box.bind('<KeyRelease-Up>', show_def)
        nb.com_list_box.bind('<Up>', clear_tag)
        nb.com_list_box.bind('<Control-Return>', command_line)
        nb.file_display.bind('<Control-Return>', command_line)
        nb.file_display.bind('<Control-ButtonRelease-1>', command_line)        
        nb.com_list_box.bind('<Button-1>', clear_tag)
        nb.com_list_box.bind('<ButtonRelease-1>', show_def)
        nb.wiki_window.bind('<Control-Return>', force_def)
        nb.wiki_window.bind('<Control-Button-1>', force_def)
        nb.command_find.bind('<Return>', search_com)
        nb.custom_window.bind('<Shift-Control-Return>', ps_command)
        nb.file_display.bind('<Shift-Control-Return>', ps_command)
        nb.file_display.bind('<Shift-Control-ButtonRelease-1>', ps_command)        
        open_file(nb.file_display, nb.custom_window)

    def run(self):
        self.root.mainloop()

cs = conky_stuff
nb = Notebook("Utilize Conky")
com = Notebook
nb.create_widgets('Conky Editor')
load_commands(nb.com_list_box)
syntax_basic(nb.file_display)
fd_syntax_highlighting(nb.file_display)
cb_syntax(nb.custom_window)
font_list()
theme_list()

nb.run()