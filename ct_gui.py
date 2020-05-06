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

################################### tab_note ##########################################

    def create_widgets(self, title):
        """create all widgets"""
        nb.frame = tk.Frame(self.notebook)
        nb.frame.grid(row = 1, sticky='NSEW')
        self.notebook.add(nb.frame,text=title)
        nb.frame.columnconfigure(0, weight = 0)
        nb.frame.columnconfigure(1, weight = 0)
        nb.frame.columnconfigure(2, weight = 0)
        nb.frame.columnconfigure(3, weight = 0)
        nb.frame.columnconfigure(19, weight = 10)
        nb.frame.rowconfigure(1, weight = 0)
        nb.frame.rowconfigure(5, weight = 10)
        nb.frame.rowconfigure(3, weight = 2)
        nb.frame.config(bg=cs.bgc)

        nb.find_label = tk.Label(nb.frame, bg=cs.bgc, text="Search:", justify='center')
        nb.find_label.grid_configure(row=1, column=0, columnspan=1)

        # row 0 column 8

        nb.theme_label = tk.Label(nb.frame, bg=cs.bgc, text="Themes:", justify='center')
        nb.theme_label.grid_configure(row=0, column=12, columnspan=1, sticky="W")

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
        
        nb.com_radio = tk.Radiobutton(nb.frame, bg=cs.bgc, text='commands', variable=nb.v, value=1, command = cr_com)
        nb.com_radio.grid_configure(row=0, column=0, sticky="NSW", columnspan=2)
        nb.com_radio.select()

        nb.con_radio = tk.Radiobutton(nb.frame, bg=cs.bgc, text='configs', variable=nb.v, value=2, command = cr_con)
        nb.con_radio.grid_configure(row=0, column=1, sticky="NSW", columnspan=2)

        nb.lua_radio = tk.Radiobutton(nb.frame, bg=cs.bgc, text='lua', variable=nb.v, value=3, command = cr_lua)
        nb.lua_radio.grid_configure(row=0, column=3, sticky="NSW", columnspan=2)

        nb.options_radio = tk.Radiobutton(nb.frame, bg=cs.bgc, text='options', variable=nb.v, value=4, command = cr_options)
        nb.options_radio.grid_configure(row=0, column=5, sticky="NSW")
        
        # row 0 column 10

        nb.Logo = tk.Text(nb.frame, height=3, width=20)
        nb.Logo.grid_configure(row=0, column=22, columnspan=3, rowspan=3, sticky="NSE")

        # row 1 coumn 0

        nb.command_find = tk.Entry(nb.frame)
        nb.command_find.grid_configure(row=1, column=1, columnspan=11, sticky="NSEW")

        # row 1 column 8'

        # list for options menu
        nb.theme_list = read_theme_list()
        nb.option_header = tk.StringVar()
        nb.option_header.set(nb.theme_list[0])

        nb.themes_list = tk.OptionMenu(nb.frame, nb.option_header, *nb.theme_list)
        nb.themes_list.grid_configure(row=1, column=12, columnspan=4, sticky="NSEW")

        # row 1 column 10

        nb.theme_button = tk.Button(nb.frame, text="Load")
        nb.theme_button.grid_configure(row=1, column=17, columnspan=2, sticky="NSEW")

        # row 2 column 0

        nb.com_label = tk.Label(nb.frame, bg=cs.bgc, text="Commands:", justify="left", width=18)
        nb.com_label.grid_configure(row=2, column=0, columnspan=1)

        # row 2 column 10

        nb.conky_label = tk.Label(nb.frame, bg=cs.bgc, text="~/.config/conky/conky.conf", justify='left')
        nb.conky_label.grid_configure(row=2, column=12)

        # row 3 column 0

        nb.com_list_box = tk.Text(nb.frame, height=15, width = 23)
        nb.com_list_box.grid_configure(row=3, column=0, rowspan=3, sticky="NSEW")

        nb.file_display = tk.Text(nb.frame, width=40, wrap = 'word')
        nb.file_display.grid_configure(row=3, column=12, columnspan=13, rowspan=15, sticky="NSEW")
        nb.file_display.config(bg="#323638", fg="#D3D8DA")

        # row 4

        nb.wiki_label = tk.Label(nb.frame, bg=cs.bgc, text="Description")
        nb.wiki_label.grid_configure(row=2, column=1, columnspan=1)

        # row 5

        nb.wiki_window = tk.Text(nb.frame, height=12, wrap=WORD, width=15)
        nb.wiki_window.grid_configure(row=3, column=1, columnspan=5, sticky="NSEW")

        # row 6

        nb.image_path_label = tk.Label(nb.frame, bg=cs.bgc, text="Image Path:")
        nb.image_path_label.grid_configure(row=6, column=0, columnspan=1, sticky="E")

        # row 7

        nb.image_entry = tk.Entry(nb.frame, width=15)
        nb.image_entry.grid_configure(row=6, column=1, columnspan=3, sticky="NSEW")

        nb.image_button = tk.Button(nb.frame, text="Submit")
        nb.image_button.grid_configure(row=8, column=3, columnspan=1, sticky="NSEW")

        # row 8

        nb.size_label = tk.Label(nb.frame, bg=cs.bgc, text="size", width=10, justify="left")
        nb.size_label.grid_configure(row=7, column=0, columnspan=1, sticky="E")

        nb.im_align = tk.Label(nb.frame, bg=cs.bgc, text="align", width=10, justify="left")
        nb.im_align.grid_configure(row=8, column=0, columnspan=1, sticky="E")

        nb.presets = tk.Label(nb.frame, bg=cs.bgc, text="custom:")
        nb.presets.grid_configure(row=4, column=1, columnspan=1, sticky="W")

        # row 9
        
        nb.size_x = tk.Entry(nb.frame, width=5)
        nb.size_x.grid_configure(row=7, column=1, sticky='NSE')

        nb.size_y = tk.Entry(nb.frame, width=5)
        nb.size_y.grid_configure(row=7, column=2, sticky='NSW')

        nb.align_image_x = tk.Entry(nb.frame, width=5)
        nb.align_image_x.grid_configure(row=8, column=1, sticky='NSE')

        nb.align_image_y = tk.Entry(nb.frame, width=5)
        nb.align_image_y.grid_configure(row=8, column=2, sticky='NSW')

        nb.presets_window = tk.Text(nb.frame, height=8, width=20, wrap="word")
        nb.presets_window.grid_configure(row=5, column=1, columnspan=6, sticky="NWSE")

        # row 10

        nb.txt_label = tk.Label(nb.frame, bg=cs.bgc, text="Text:")
        nb.txt_label.grid_configure(row=10, columnspan=4, sticky="N")

        # row 11

        nb.txt_input = tk.Entry(nb.frame)
        nb.txt_input.grid_configure(row=11, columnspan=3, sticky="EW")

        nb.txt_submit = tk.Button(nb.frame, text="Enter:")
        nb.txt_submit.grid_configure(row=11, column=3, sticky="EW")

        # row 12

        nb.color_label = tk.Label(nb.frame, bg=cs.bgc, text="Color:")
        nb.color_label.grid_configure(row=12, columnspan=4, sticky="EW")

        # row 13
        nb.color_entry = tk.Entry(nb.frame)
        nb.color_entry.grid_configure(row=13, columnspan=3, sticky="EW")

        nb.color_button = tk.Button(nb.frame, text="Enter")
        nb.color_button.grid_configure(row=13, column=3, sticky="EW")

        # row 16 Font

        nb.font_label = tk.Label(nb.frame, bg=cs.bgc, text="Font Name:")
        nb.font_label.grid_configure(row=16, columnspan=1, sticky="NSW")

        nb.fs_label = tk.Label(nb.frame, bg=cs.bgc, text="Size:")
        nb.fs_label.grid_configure(row=16, column=3, columnspan=1, sticky="NSEW")

        # row 18
        nb.font_list = open(main_path+".fontlist.txt", 'r').read().splitlines()
        nb.font_list_header = tk.StringVar()
        nb.font_list_header.set(nb.font_list[0])

        nb.fn_entry = tk.OptionMenu(nb.frame, nb.font_list_header, *nb.font_list)
        nb.fn_entry.grid_configure(row=18, columnspan=2, sticky="NSEW")

        nb.fs_entry = tk.Entry(nb.frame, width=5)
        nb.fs_entry.grid_configure(row=18, column=2, columnspan=1, sticky="NSEW")

        nb.font_submit = tk.Button(nb.frame, text="Enter")
        nb.font_submit.grid_configure(row=18, column=3, columnspan=1, sticky="NSEW")

        nb.save_button = tk.Button(nb.frame, text="save", command=lambda: save_file(nb.file_display))
        nb.save_button.grid_configure(row=18, column=23, columnspan=1, sticky="NSEW")

        nb.save_theme_button = tk.Button(nb.frame, text="save theme", command=lambda: save_theme(nb.theme_display, nb.file_display))
        nb.save_theme_button.grid_configure(row=18, column=22, columnspan=1, sticky="NSEW")

        nb.theme_name = tk.Label(nb.frame, bg=cs.bgc, text="Theme Name:")
        nb.theme_name.grid_configure(row=18, column=17, columnspan=2)

        nb.theme_display = tk.Entry(nb.frame)
        nb.theme_display.grid_configure(row=18, column=19, columnspan=2, sticky="NSEW")

        # final row

        nb.quit = tk.Button(nb.frame, text="QUIT", fg="red", command=self.root.destroy)
        nb.quit.grid_configure(row=18, column=24, sticky="WE")

        # imported modules / binds

        def sub_font(self):
            make_font(nb.font_list_header, nb.fs_entry, nb.file_display)
        nb.font_submit.config(command=lambda: sub_font(com))

        def get_theme(self):
            load_theme(nb.option_header, nb.file_display)
        nb.theme_button.config(command=lambda: get_theme(com))

        def add_color(self):
            color_ct(nb.color_entry, nb.file_display)
        nb.color_button.config(command=lambda: add_color(com))

        def add_picture(self):
            add_image(nb.image_entry, nb.size_x, nb.size_y, nb.align_image_x, nb.align_image_y, nb.file_display)
        nb.image_button.config(command=lambda: add_picture(com))

        def pic_size(self):
            image_dimensions(nb.image_entry, nb.size_x, nb.size_y)
            nb.align_image_x.insert(INSERT, '0')
            nb.align_image_y.insert(INSERT, '0')
        nb.image_entry.bind('<Return>', pic_size)

        def rs_x(self):
            """resize y when x is changed"""
            resize_x(nb.size_x, nb.size_y)
        nb.size_x.bind('<Return>', rs_x)

        def rs_y(self):
            """resize x when y is changed"""
            resize_x(nb.size_x, nb.size_y)
        nb.size_y.bind('<Return>', rs_y)

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
            if cs.selected == "commands":
                x = str(nb.com_list_box.get("insert linestart", "insert lineend"))
                if "..." not in x:
                    the_input = eval(x)
                    the_input.definition_out(nb.wiki_window)
                if "..." in x:
                    for l in too_long:
                        if x[0:-3] in str(l):
                            the_input = eval(l)
                            the_input.definition_out(nb.wiki_window)
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
            return 'break'

        def search_com(self):
            if nb.command_find.get() == '':
                conky_stuff.results = []
                nb.com_list_box.delete(0.0, END)
                load_commands(nb.com_list_box)
            else:
                search(nb.command_find, nb.com_list_box)
        
        nb.com_list_box.bind('<Alt-Return>', show_def)
        nb.com_list_box.bind('<Control-Return>', command_line)
        nb.command_find.bind('<Return>', search_com)

        open_file(nb.file_display, nb.presets_window)

    def run(self):
        self.root.mainloop()

cs = conky_stuff
nb = Notebook("Work in progress")
com = Notebook
nb.create_widgets('Conky Editor')
load_commands(nb.com_list_box)
font_list()
theme_list()

nb.run()