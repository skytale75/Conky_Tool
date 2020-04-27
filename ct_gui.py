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
        nb.frame = ttk.Frame(self.notebook)
        nb.frame.grid(row = 1, sticky='NSEW')
        self.notebook.add(nb.frame,text=title)
        nb.frame.columnconfigure(0, weight = 0)
        nb.frame.columnconfigure(1, weight = 0)
        nb.frame.columnconfigure(2, weight = 0)
        nb.frame.columnconfigure(3, weight = 0)
        nb.frame.columnconfigure(17, weight = 10)
        nb.frame.rowconfigure(1, weight = 0)
        nb.frame.rowconfigure(5, weight = 10)
        nb.frame.rowconfigure(3, weight = 2)

        nb.find_label = tk.Label(nb.frame, text="Search Commands:", justify='center', width=20)
        nb.find_label.grid_configure(row=0, column=0, columnspan=8)

        # row 0 column 8

        nb.theme_label = tk.Label(nb.frame, text="Themes:", justify='center', width=30)
        nb.theme_label.grid_configure(row=0, column=8, columnspan=10)

        # row 0 column 10

        nb.Logo = tk.Text(nb.frame, height=3, width=20)
        nb.Logo.grid_configure(row=0, column=18, columnspan=3, rowspan=3, sticky="NSEW")

        # row 1 coumn 0

        nb.command_find = tk.Entry(nb.frame, width=20)
        nb.command_find.grid_configure(row=1, column=0, columnspan=8, sticky="NSEW")

        # row 1 column 8'

        # list for options menu
        nb.theme_list = read_theme_list()
        nb.option_header = tk.StringVar()
        nb.option_header.set(nb.theme_list[0])

        nb.themes_list = tk.OptionMenu(nb.frame, nb.option_header, *nb.theme_list)
        nb.themes_list.grid_configure(row=1, column=8, columnspan=8, sticky="NSEW")

        # row 1 column 10

        nb.theme_button = tk.Button(nb.frame, text="Load")
        nb.theme_button.grid_configure(row=1, column=16, columnspan=2, sticky="NSEW")

        # row 2 column 0

        nb.com_label = tk.Label(nb.frame, text="Commands:", justify='center', width=20)
        nb.com_label.grid_configure(row=2, column=0, columnspan=8)

        # row 2 column 10

        nb.conky_label = tk.Label(nb.frame, text="~/.config/conky/conky.conf", justify='left')
        nb.conky_label.grid_configure(row=2, column=8)

        # row 3 column 0

        nb.com_list_box = tk.Text(nb.frame, height=5, width=20)
        nb.com_list_box.grid_configure(row=3, column=0, columnspan=8, sticky="NSEW")

        nb.file_display = tk.Text(nb.frame, width=50, wrap = 'word')
        nb.file_display.grid_configure(row=3, column=8, columnspan=13, rowspan=15, sticky="NSEW")
        nb.file_display.config(bg="darkblue", fg="lightblue")

        # row 4

        nb.wiki_label = tk.Label(nb.frame, text="Description and Usage:", width=20)
        nb.wiki_label.grid_configure(row=4, column=0, columnspan=8)

        # row 5

        nb.wiki_window = tk.Text(nb.frame, height=15, width=30, wrap=WORD)
        nb.wiki_window.grid_configure(row=5, column=0, columnspan=8, sticky="NSEW")

        # row 6

        nb.image_path_label = tk.Label(nb.frame, text="Image Path:")
        nb.image_path_label.grid_configure(row=6, column=0, columnspan=8)

        # row 7

        nb.image_entry = tk.Entry(nb.frame)
        nb.image_entry.grid_configure(row=7, column=0, columnspan=6, sticky="NSEW")

        nb.image_button = tk.Button(nb.frame, text="Submit")
        nb.image_button.grid_configure(row=7, column=6, columnspan=2, sticky="NSEW")

        # row 8

        nb.size_label = tk.Label(nb.frame, text="img\nsize", width=10)
        nb.size_label.grid_configure(row=8, column=0, columnspan=2)

        nb.im_align = tk.Label(nb.frame, text="img\nalign", width=10)
        nb.im_align.grid_configure(row=8, column=2, columnspan=2)

        nb.presets = tk.Label(nb.frame, text="custom\nattributes")
        nb.presets.grid_configure(row=8, column=4, columnspan=4)

        # row 9
        
        nb.size_x = tk.Entry(nb.frame, width=5)
        nb.size_x.grid_configure(row=9, column=0, sticky='N')

        nb.size_y = tk.Entry(nb.frame, width=5)
        nb.size_y.grid_configure(row=9, column=1, sticky='N')

        nb.align_image_x = tk.Entry(nb.frame, width=5)
        nb.align_image_x.grid_configure(row=9, column=2, sticky='N')

        nb.align_image_y = tk.Entry(nb.frame, width=5)
        nb.align_image_y.grid_configure(row=9, column=3, sticky='N')

        nb.presets_window = tk.Text(nb.frame, height=9, width=30)
        nb.presets_window.grid_configure(row=9, column=4, columnspan=4, rowspan=9, sticky="NSEW")

        # row 10

        nb.txt_label = tk.Label(nb.frame, text="Text:")
        nb.txt_label.grid_configure(row=10, columnspan=4, sticky="N")

        # row 11

        nb.txt_input = tk.Entry(nb.frame)
        nb.txt_input.grid_configure(row=11, columnspan=3, sticky="EW")

        nb.txt_submit = tk.Button(nb.frame, text="Enter:")
        nb.txt_submit.grid_configure(row=11, column=3, sticky="EW")

        # row 12

        nb.color_label = tk.Label(nb.frame, text="Color:")
        nb.color_label.grid_configure(row=12, columnspan=4, sticky="EW")

        # row 13
        nb.color_entry = tk.Entry(nb.frame)
        nb.color_entry.grid_configure(row=13, columnspan=3, sticky="EW")

        nb.color_button = tk.Button(nb.frame, text="Enter")
        nb.color_button.grid_configure(row=13, column=3, sticky="EW")

        # row 14 Align

        nb.align_label = tk.Label(nb.frame, text="Align:")
        nb.align_label.grid_configure(row=14, columnspan=4, sticky="EW")

        nb.align_x = tk.Entry(nb.frame, width=5)
        nb.align_x.grid_configure(row=15, columnspan=1, sticky="EW")

        nb.align_y = tk.Entry(nb.frame, width=5)
        nb.align_y.grid_configure(row=15, column=1, columnspan=1, sticky="EW")

        nb.align_submit = tk.Button(nb.frame, text="Enter")
        nb.align_submit.grid_configure(row=15, column=2, columnspan=2, sticky="E")

        # row 16 Font

        nb.font_label = tk.Label(nb.frame, text="Font Name:")
        nb.font_label.grid_configure(row=16, columnspan=3, sticky="NSEW")

        nb.fs_label = tk.Label(nb.frame, text="Size:")
        nb.fs_label.grid_configure(row=16, column=3, columnspan=1, sticky="NSEW")

        # row 18
        nb.font_list = open(".fontlist.txt", 'r').read().splitlines()
        nb.font_list_header = tk.StringVar()
        nb.font_list_header.set(nb.font_list[0])

        nb.fn_entry = tk.OptionMenu(nb.frame, nb.font_list_header, *nb.font_list)
        nb.fn_entry.grid_configure(row=18, columnspan=3, sticky="NSEW")

        nb.fs_entry = tk.Entry(nb.frame, width=5)
        nb.fs_entry.grid_configure(row=18, column=3, columnspan=1, sticky="NSEW")

        nb.font_submit = tk.Button(nb.frame, text="Enter")
        nb.font_submit.grid_configure(row=18, column=4, columnspan=1, sticky="NSEW")

        nb.save_button = tk.Button(nb.frame, text="save", command=lambda: save_file(nb.file_display))
        nb.save_button.grid_configure(row=18, column=18, columnspan=2, sticky="NSEW")

        nb.save_theme_button = tk.Button(nb.frame, text="save theme", command=lambda: save_theme(nb.theme_display, nb.file_display))
        nb.save_theme_button.grid_configure(row=18, column=16, columnspan=2, sticky="NSEW")

        nb.theme_name = tk.Label(nb.frame, text="Theme Name:")
        nb.theme_name.grid_configure(row=18, column=8, columnspan=2)

        nb.theme_display = tk.Entry(nb.frame)
        nb.theme_display.grid_configure(row=18, column=10, columnspan=2, sticky="NSEW")

        # final row

        nb.quit = tk.Button(nb.frame, text="QUIT", fg="red", command=self.root.destroy)
        nb.quit.grid_configure(row=18, column=20, sticky="WE")

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
            resize_x(nb.size_x, nb.size_y)
        nb.size_x.bind('<Return>', rs_x)

        def rs_y(self):
            resize_x(nb.size_x, nb.size_y)
        nb.size_y.bind('<Return>', rs_y)

        def command_line(self):
            the_input = str(nb.com_list_box.get("insert linestart", "insert lineend"))
            functions[the_input](nb.file_display)
            return 'break'

        def insert_command(self):
            add_command(nb.com_list_box, nb.file_display)

        def show_def(self):
            the_input = eval(str(nb.com_list_box.get("insert linestart", "insert lineend")))
            the_input.definition_out(nb.wiki_window)
            return 'break'
        
        nb.com_list_box.bind('<Alt-Return>', show_def)
        nb.com_list_box.bind('<Control-Return>', command_line)

        open_file(nb.file_display, nb.presets_window)

    def run(self):
        self.root.mainloop()


nb = Notebook("Work in progress")
com = Notebook
nb.create_widgets('Conky Editor')
font_list()
theme_list()

nb.run()