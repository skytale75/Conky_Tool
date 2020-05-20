from tkinter import *
import tkinter as tk
from tkinter import ttk
from ct_fun import *
from ct_mod import *
from common_stuff import Common_Stuff as cs
from os import listdir
from PIL import Image
from gui_names import gui_names as gn

class Notebook:

    def __init__(self, title):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry("1024x768")
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
            search_path = cs.coms_path
            cs.selected = "commands"
            load_commands(nb.com_list_box)

        def cr_con():
            search_path = cs.configs_path
            cs.selected = "configs"
            load_configs(nb.com_list_box)

        def cr_lua():
            search_path = cs.lua_path
            cs.selected = "lua"
            load_lua(nb.com_list_box)

        def cr_options():
            search_path = cs.options_path
            cs.selected = "options"
            nb.com_list_box.delete(0.0, END)
            load_options(nb.wiki_window)
        
        nb.com_radio = tk.Radiobutton(nb.frame, indicatoron=0, width=20, bg=cs.bgc, text=gn.rb_commands, variable=nb.v, value=1, command = cr_com)
        nb.com_radio.grid_configure(row=0, column=0, columnspan=4, sticky="NSEW")
        nb.com_radio.select()

        nb.con_radio = tk.Radiobutton(nb.frame, indicatoron=0, width=20, bg=cs.bgc, text=gn.rb_configs, variable=nb.v, value=2, command = cr_con)
        nb.con_radio.grid_configure(row=1, column=0, columnspan=4, sticky="NSEW")

        nb.lua_radio = tk.Radiobutton(nb.frame, indicatoron=0, width=20, bg=cs.bgc, text=gn.rb_lua, variable=nb.v, value=3, command = cr_lua)
        nb.lua_radio.grid_configure(row=2, column=0, columnspan=4, sticky="NSEW")

        nb.options_radio = tk.Radiobutton(nb.frame, indicatoron=0, width=20, bg=cs.bgc, text=gn.rb_options, variable=nb.v, value=4, command = cr_options)
        nb.options_radio.grid_configure(row=3, column=0, columnspan=4, sticky="NSEW")

        nb.find_label = tk.Label(nb.frame, bg=cs.bgc, text=gn.lbl_search)
        nb.find_label.grid_configure(row=0, column=4, columnspan=1)

        nb.command_find = tk.Entry(nb.frame, bg="darkblue", fg="white", font= ('Deja Vu Serif', 10))
        nb.command_find.grid_configure(row=0, column=5, columnspan=5, sticky="NSEW")

        nb.in_button = tk.Button(nb.frame, text=gn.how_to, command=lambda: instructions_window())
        nb.in_button.grid_configure(row=1, column=5, sticky="NESW")


        nb.com_label = tk.Label(nb.frame, bg=cs.bgc, text=gn.rb_commands, justify="left")
        nb.com_label.grid_configure(row=4, column=0, columnspan=5)

        nb.conky_label = tk.Label(nb.frame, bg=cs.bgc, text=cs.config_file, justify='left')
        nb.conky_label.grid_configure(row=0, column=10, columnspan=10)

        nb.com_list_box = tk.Text(nb.frame, height=10, width=25, bg="lightblue", font= ('Deja Vu Serif', 10))
        nb.com_list_box.grid_configure(row=5, column=0, columnspan=5, sticky="NSEW")

        nb.file_display = tk.Text(nb.frame, width=50, wrap = 'word', undo=True)
        nb.file_display.grid_configure(row=1, column=10, columnspan=10, rowspan=7, sticky="NSEW")
        nb.file_display.config(bg="black", fg="white", insertbackground = 'cyan', font= ('Deja Vu Serif', 10))

        nb.wiki_label = tk.Label(nb.frame, bg=cs.bgc, text=gn.lbl_description)
        nb.wiki_label.grid_configure(row=6, column=0, columnspan=10)

        nb.wiki_window = tk.Text(nb.frame, height=10, wrap='word', width=25, bg = "lightyellow", font= ('Deja Vu Serif', 10))
        nb.wiki_window.grid_configure(row=7, column=0, columnspan=10, sticky="NSEW")

        nb.color_button = tk.Button(nb.frame, text=gn.btn_colors, command=lambda: add_color_window(nb.file_display, nb.custom_window))
        nb.color_button.grid_configure(row=8, column=0, columnspan=2, sticky="NESW")

        nb.fonts_button = tk.Button(nb.frame, text=gn.btn_fonts, command=lambda: font_window(nb.file_display))
        nb.fonts_button.grid_configure(row=8, column=2, columnspan=2, sticky='NSEW')

        nb.image_button = tk.Button(nb.frame, text=gn.btn_img, command =lambda: image_window(nb.file_display))
        nb.image_button.grid_configure(row=8, column=4, columnspan=2, sticky="NSEW")

        nb.themes_button = tk.Button(nb.frame, text=gn.btn_themes, command=lambda: themes_window(nb.file_display, nb.custom_window))
        nb.themes_button.grid_configure(row=8, column=14, columnspan=2, sticky='NSE')

        nb.custom = tk.Label(nb.frame, bg=cs.bgc, text=gn.lbl_custom)
        nb.custom.grid_configure(row=4, column=5, columnspan=5)

        nb.custom_window = tk.Text(nb.frame, height=10, width=25, wrap="word", bg="darkgrey", fg="cyan")
        nb.custom_window.grid_configure(row=5, column=5, columnspan=5, sticky="NWSE")

        nb.save_button = tk.Button(nb.frame, width=10, text=gn.btn_save, fg='red', command=lambda: save_file(nb.file_display, nb.custom_window))
        nb.save_button.grid_configure(row=8, column=16, columnspan=2, sticky='NSEW')

        nb.quit = tk.Button(nb.frame, width=10, text=gn.btn_quit, fg="red", command=self.root.destroy)
        nb.quit.grid_configure(row=8, column=18, columnspan=2, sticky='NSEW')

        def command_line(self):
            """locate command in dictionary and enter
            into file_display, or open options window"""
            if cs.selected == "commands":
                the_input = cs.hold_command
                functions[the_input](nb.file_display)
            return "break"

        def definition(self):
            """tie into show_def, which automatically
            displays definition in wiki window"""
            show_def(nb.com_list_box, nb.wiki_window)
        def ps_command(self):
            """tie into add_custom, which adds custom
            color or font to file"""
            add_custom(nb.custom_window, nb.file_display)
            return 'break'
        def search_com(self):
            if nb.command_find.get() == '':
                cs.results = []
                nb.com_list_box.delete(0.0, END)
                load_commands(nb.com_list_box)
            if nb.command_find.get() == '-e on':
                cs.editable = 'on'
            if nb.command_find.get() == '-e off':
                cs.editable = 'off'
            else:
                search(nb.command_find, nb.com_list_box)
        def force_def(self):
            Commands.force_file(self, nb.wiki_window, nb.file_display)
        def clear_tag(self):
            nb.com_list_box.tag_remove("command", 0.0, END)
        def tab(self):
            nb.file_display.insert(INSERT, "    ")
            return "break"
        def hc(self):
            load_hold_color(nb.custom_window)
        def dup_down(self):
            duplicate_press(nb.file_display)
            return "break"
        def file_display_help(self):
            help_window("help_editor.txt", "Editor Help")
            return "break"
        def search_help(self):
            help_window("help_search.txt", "Search Bar Help")
        def definitions_help(self):
            help_window("help_definitions.txt", "Help, Definitions")
        def command_box_help(self):
            help_window('help_CL.txt', "Command Box Help")
        def custom_help(self):
            help_window("help_custom.txt", "Custom Colors Help")
        def save_kc(self):
            save_file(nb.file_display, nb.custom_window)

        nb.com_list_box.tag_config("command", background="white")
        nb.com_list_box.bind('<KeyRelease-Down>', definition)
        nb.com_list_box.bind('<Down>', clear_tag)
        nb.com_list_box.bind('<KeyRelease-Up>', definition)
        nb.com_list_box.bind('<Up>', clear_tag)
        nb.com_list_box.bind('<Control-Return>', command_line)
        nb.com_list_box.bind('<Button-1>', clear_tag)
        nb.com_list_box.bind('<ButtonRelease-1>', definition)
        nb.com_list_box.bind('<Control-h>', command_box_help)
        nb.file_display.bind("<Tab>", tab)
        nb.file_display.bind('<Control-Return>', command_line)
        nb.file_display.bind('<Control-ButtonRelease-1>', command_line)
        nb.file_display.bind('<Shift-Control-Return>', ps_command)
        nb.file_display.bind('<Shift-Control-ButtonRelease-1>', ps_command)        
        nb.file_display.bind('<Control-d>', dup_down)   
        nb.file_display.bind('<Control-s>', save_kc)            
        nb.wiki_window.bind('<Control-Return>', force_def)
        nb.wiki_window.bind('<Control-Button-1>', force_def)
        nb.wiki_window.bind('<Control-h>', definitions_help)
        nb.command_find.bind('<Return>', search_com)
        nb.command_find.bind('<Control-h>', search_help)
        nb.custom_window.bind('<Shift-Control-Return>', ps_command)
        nb.custom_window.bind('<ButtonRelease-1>', hc)
        nb.custom_window.bind('<KeyRelease-Up>', hc)
        nb.custom_window.bind('<KeyRelease-Down>', hc)
        nb.custom_window.bind('<Control-h>', custom_help)

        nb.file_display.bind("<Control-h>", file_display_help)

        open_file(nb.file_display, nb.custom_window)

    def run(self):
        self.root.mainloop()

nb = Notebook(gn.win_main)
com = Notebook
nb.create_widgets(gn.editor)
load_commands(nb.com_list_box)
color_separator()
syntax_basic(nb.file_display)
fd_syntax_highlighting(nb.file_display)
cb_syntax(nb.custom_window)
font_list()
theme_list()

nb.run()