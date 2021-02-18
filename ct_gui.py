from tkinter import Frame, Radiobutton, ttk, Entry, Label, Text, Button, Tk, END, INSERT, StringVar, OptionMenu, IntVar
from ct_fun import Commands, functions
from ct_mod import search_su, load_commands, load_configs, load_lua, load_options, toggle_gb, toggle_pb, \
    save_file, show_def, add_custom, search, load_hold_color, duplicate_press, open_file, load_by_line, \
    insert_line, insert_line, syntax_basic, fd_syntax_highlighting, cbl_update, theme_prompt, read_theme_list, \
    get_theme, make_font, resize_x, resize_y, image_dimensions, add_image, image_from_line, color_separator, \
    cb_syntax, font_list, theme_list
from common_stuff import Common_Stuff as cs
from os import listdir
from PIL import Image
from gui_names import gui_names as gn
import subprocess


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
        nb.frame = Frame(self.notebook)
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

            nb.com_list_box.delete(0.0, END)
            cs.selected = "commands"
            load_commands(nb.com_list_box)

        def cr_con():
            nb.com_list_box.delete(0.0, END)
            cs.selected = "configs"
            load_configs(nb.com_list_box)

        def cr_lua():
            nb.com_list_box.delete(0.0, END)
            cs.selected = "lua"
            load_lua(nb.com_list_box)

        def cr_options():
            cs.selected = "options"
            nb.com_list_box.delete(0.0, END)
            load_options(nb.wiki_window)
        
        nb.com_radio =Radiobutton(nb.frame, indicatoron=0, width=20, bg=cs.bgc, text=gn.rb_commands, variable=nb.v, value=1, command = cr_com)
        nb.com_radio.grid_configure(row=0, column=0, columnspan=5, sticky="NSEW")
        nb.com_radio.select()

        nb.con_radio =Radiobutton(nb.frame, indicatoron=0, width=20, bg=cs.bgc, text=gn.rb_configs, variable=nb.v, value=2, command = cr_con)
        nb.con_radio.grid_configure(row=1, column=0, columnspan=5, sticky="NSEW")

        nb.lua_radio =Radiobutton(nb.frame, indicatoron=0, width=20, bg=cs.bgc, text=gn.rb_lua, variable=nb.v, value=3, command = cr_lua)
        nb.lua_radio.grid_configure(row=2, column=0, columnspan=5, sticky="NSEW")

        nb.options_radio =Radiobutton(nb.frame, indicatoron=0, width=20, bg=cs.bgc, text=gn.rb_options, variable=nb.v, value=4, command = cr_options)
        nb.options_radio.grid_configure(row=3, column=0, columnspan=5, sticky="NSEW")

        nb.command_find =Entry(nb.frame, bg="darkblue", fg="white", font= ('Deja Vu Serif', 10))
        nb.command_find.grid_configure(row=4, column=0, columnspan=5, sticky="NSEW")

        nb.conky_label =Label(nb.frame, bg=cs.bgc, text=cs.config_file, justify='left')
        nb.conky_label.grid_configure(row=0, column=10, columnspan=10)

        nb.com_list_box =Text(nb.frame, height=10, width=25, bg="lightblue", font= ('Deja Vu Serif', 10))
        nb.com_list_box.grid_configure(row=5, column=0, columnspan=5, sticky="NSEW")

        nb.lnText = Text(nb.frame, width = 4, padx = 4, highlightthickness = 0, takefocus = 0,
                bd = 0, background = 'lightgrey', foreground = 'magenta', state='disabled')

        nb.file_display =Text(nb.frame, width=50, wrap = 'word', undo=True)
        nb.file_display.grid_configure(row=1, column=10, columnspan=10, rowspan=7, sticky="NSEW")
        nb.file_display.config(bg="black", fg="white", insertbackground = 'cyan', font= ('Deja Vu Serif', 10))

        nb.wiki_label =Label(nb.frame, bg=cs.bgc, text=gn.lbl_description)
        nb.wiki_label.grid_configure(row=6, column=0, columnspan=10)

        nb.wiki_window =Text(nb.frame, height=10, wrap='word', width=25, bg = "lightyellow", font= ('Deja Vu Serif', 10))
        nb.wiki_window.grid_configure(row=7, column=0, columnspan=10, sticky="NSEW")

        nb.color_button =Button(nb.frame, text=gn.btn_colors, command=nb.add_color_window)
        nb.color_button.grid_configure(row=8, column=0, columnspan=2, sticky="NESW")

        nb.fonts_button =Button(nb.frame, text=gn.btn_fonts, command=lambda: nb.font_window_fun(nb.file_display))
        nb.fonts_button.grid_configure(row=8, column=2, columnspan=2, sticky='NSEW')

        nb.image_button =Button(nb.frame, text=gn.btn_img, command =nb.image_window_fun)
        nb.image_button.grid_configure(row=8, column=4, columnspan=2, sticky="NSEW")

        nb.page_borders =Button(nb.frame, text="Page Border", command=lambda: toggle_pb(nb.file_display, nb.custom_window))
        nb.page_borders.grid_configure(row=8, column=12)

        nb.graph_borders =Button(nb.frame, text="Graph Border", command=lambda: toggle_gb(nb.file_display, nb.custom_window))
        nb.graph_borders.grid_configure(row=8, column=13)

        nb.themes_button =Button(nb.frame, text=gn.btn_themes, command=nb.themes_window)
        nb.themes_button.grid_configure(row=8, column=14, columnspan=2, sticky='NSE')

        nb.custom =Label(nb.frame, bg=cs.bgc, text=gn.lbl_custom)
        nb.custom.grid_configure(row=4, column=5, columnspan=5)

        nb.custom_window =Text(nb.frame, height=10, width=25, wrap="word", bg="darkgrey", fg="cyan")
        nb.custom_window.grid_configure(row=5, column=5, columnspan=5, sticky="NWSE")

        nb.save_button =Button(nb.frame, width=10, text=gn.btn_save, fg='red', command=lambda: save_file(nb.file_display, nb.custom_window))
        nb.save_button.grid_configure(row=8, column=16, columnspan=2, sticky='NSEW')

        nb.quit =Button(nb.frame, width=10, text=gn.btn_quit, fg="red", command=self.root.destroy)
        nb.quit.grid_configure(row=8, column=18, columnspan=2, sticky='NSEW')

        def command_line(self):
            """locate command in dictionary and enter
            into file_display, or open options window"""
            if cs.hold_command != '':
                if cs.selected == "commands":
                    the_input = cs.hold_command
                    functions[the_input](nb.file_display)
            
            return "break"

        def definition(self):
            """tie into show_def, which automatically
            displays definition iadd_cc window"""
            show_def(nb.com_list_box, nb.wiki_window)
        def ps_command(self):
            """tie into add_custom, which adds custom
            color or font to file"""
            add_custom(nb.custom_window, nb.file_display)
            return 'break'
        def search_com(self):
            if nb.command_find.get() == '' and cs.hold_command == "commands":
                cs.results = []
                nb.com_list_box.delete(0.0, END)
                load_commands(nb.com_list_box)
            if nb.command_find.get() == '' and cs.hold_command == "configs":
                cs.results = []
                nb.com_list_box.delete(0.0, END)
                load_configs(nb.com_list_box)
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
            nb.help_window(self, "help_editor.txt", "Editor Help")
            return "break"
        def search_help(self):
            nb.help_window(self, "help_search.txt", "Search Bar Help")
        def definitions_help(self):
            nb.help_window(self, "help_definitions.txt", "Help, Definitions")
        def command_box_help(self):
            nb.help_window(self, 'help_CL.txt', "Command Box Help")
        def custom_help(self):
            nb.help_window(self, "help_custom.txt", "Custom Colors Help")
        def save_kc(self):
            save_file(nb.file_display, nb.custom_window)
        def launch_conky(self):
            subprocess.call('nconky',shell="true")
        def check_window(self):
            if 'normal' == nb.font_window.state():
                print('font window open')
        def delete_cl(self):
            if cs.cl_toggle == 1:
                nb.command_find.delete(0, END)
                cs.cl_toggle = 0

        
        nb.com_list_box.tag_config("command", background="white")
        nb.com_list_box.bind('<KeyRelease-Down>', definition)
        nb.com_list_box.bind('<Down>', clear_tag)
        nb.com_list_box.bind('<KeyRelease-Up>', definition)
        nb.com_list_box.bind('<Up>', clear_tag)
        nb.com_list_box.bind('<Control-Return>', command_line)
        nb.com_list_box.bind('<Button-1>', clear_tag)
        nb.com_list_box.bind('<ButtonRelease-1>', definition)
        nb.com_list_box.bind('<Control-h>', command_box_help)
        nb.file_display.bind('<Control-p>', nb.conky_by_line)
        nb.file_display.bind('<Control-f>', check_window)
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
        nb.command_find.bind('<ButtonRelease-1>', delete_cl)
        nb.command_find.bind('<KeyRelease>', search_com)
        nb.command_find.bind('<Control-h>', search_help)
        nb.custom_window.bind('<Shift-Control-Return>', ps_command)
        nb.custom_window.bind('<ButtonRelease-1>', hc)
        nb.custom_window.bind('<KeyRelease-Up>', hc)
        nb.custom_window.bind('<KeyRelease-Down>', hc)
        nb.custom_window.bind('<Control-h>', custom_help)
        nb.file_display.bind("<Control-l>", launch_conky)
        nb.file_display.bind("<Control-h>", file_display_help)

        open_file(nb.file_display, nb.custom_window)
        nb.command_find.insert(INSERT, "Search commands . . .")

    def help_frame_fun(self):
        nb.help_frame =Frame(self.notebook)
        nb.help_frame.grid(row = 1, sticky='NSEW')
        self.notebook.add(nb.help_frame,text="help")
        nb.help_frame.rowconfigure(0, weight=1)
        nb.help_frame.columnconfigure(0, weight=1)

        open_in = open(cs.uc_home_path+"instructions.txt")
        instructions = open_in.read()
        open_in.close()

        nb.help_text =Text(nb.help_frame)
        nb.help_text.grid_configure(row=0, column=0, sticky="NESW")
        nb.help_text.insert(INSERT, instructions)

    def conky_by_line(self, foo):
        nb.cbl_window = Tk()
        nb.cbl_window.grid()
        nb.cbl_window.attributes("-topmost", 'true')
        nb.cbl_window.title("Conky by line")

        nb.cbl_text =Text(nb.cbl_window, width=40, height = 30)
        nb.cbl_text.grid_configure(row=0, column=0, columnspan=5)
        nb.cbl_text.config(bg="black", fg="white", insertbackground = 'cyan', font= ('Deja Vu Serif', 10))

        def cbl_command_custom(self):
            """add_custom to conky by line window"""
            add_custom(nb.custom_window, nb.cbl_text)
        def cbl_command_enter(self):
            if cs.selected == "commands":
                the_input = cs.hold_command
                functions[the_input](nb.cbl_text)
            return "break"

        load_by_line(nb.com_list_box, nb.custom_window, nb.file_display)
        insert_line(nb.cbl_text)

        syntax_basic(nb.cbl_text)
        fd_syntax_highlighting(nb.cbl_text)

        nb.cbl_enter =Button(nb.cbl_window, text="Update", command=lambda: cbl_update(nb.cbl_text, nb.com_list_box, nb.custom_window, nb.file_display))
        nb.cbl_enter.grid_configure(row=2, column=4, sticky="NSEW")

        nb.cbl_font =Button(nb.cbl_window, text="fonts", command = lambda: nb.font_window_fun(nb.cbl_text))
        nb.cbl_font.grid_configure(row=2, column=1, sticky="NWES")

        nb.cbl_exit =Button(nb.cbl_window, text="Exit", command=nb.cbl_window.destroy)
        nb.cbl_exit.grid_configure(row=2, column=0, sticky="NSEW")
        
        nb.cbl_text.bind("<Control-Return>", cbl_command_enter)
        nb.cbl_text.bind("<Control-Button-1>", cbl_command_enter)
        nb.cbl_text.bind("<Shift-Control-Return>", cbl_command_custom)
        nb.cbl_text.bind("<Shift-Control-Button-1>", cbl_command_custom)

        nb.cbl_window.after(5000, lambda: nb.cbl_window.focus_force())

    def themes_window(self):
        """create themes properties window"""

        nb.window = Tk()
        nb.window.grid()
        nb.window.title(gn.win_themes)
        nb.window.attributes("-topmost", True)

        theme_name =Label(nb.window, bg=cs.bgc, text=gn.lbl_theme_name)
        theme_name.grid_configure(row=0, column=0, columnspan=1)

        theme_display =Entry(nb.window)
        theme_display.grid_configure(row=0, column=1, columnspan=1, sticky="NSEW")

        save_theme_button =Button(nb.window, text=gn.btn_save_theme, command=lambda: theme_prompt(theme_display, nb.file_display))
        save_theme_button.grid_configure(row=0, column=2, columnspan=1, sticky="NSEW")

        open_theme_label =Label(nb.window, text=gn.lbl_open_theme)
        open_theme_label.grid_configure(row=1, column=0, sticky='NSEW')

        theme_list = read_theme_list()
        option_header =StringVar(nb.window)
        option_header.set(theme_list[0])

        themes_list =OptionMenu(nb.window, option_header, *theme_list)
        themes_list.grid_configure(row=1, column=1, columnspan=1, sticky="NSEW")

        theme_button =Button(nb.window, text=gn.btn_load_theme)
        theme_button.grid_configure(row=1, column=2, columnspan=1, sticky="NSEW")
        theme_button.config(command=lambda: get_theme(nb.file_display, option_header, nb.custom_window))

        nb.window.mainloop()

    def font_window_fun(self, file_display):
        """create font properties window"""
        nb.font_window = Tk()
        nb.font_window.grid()
        nb.font_window.title(gn.win_fonts)
        nb.font_window.attributes("-topmost", True)

        cs.toggle=0

        def font_search(foo):
            the_search = font_search_bar.get()
            fn_entry.delete(0.0, END)
            for l in cs.font_list:
                if the_search.lower() in str(l).lower():
                    fn_entry.insert(INSERT, l+"\n")

        def clear_entry(foo):
            search_su(font_search_bar)

        font_search_bar =Entry(nb.font_window, bg="darkblue", fg="white")
        font_search_bar.grid_configure(row=0, column=0, columnspan=2, sticky="NESW")
        font_search_bar.insert(INSERT, "Search fonts . . .")
        font_search_bar.bind("<Button-1>", clear_entry)
        font_search_bar.bind("<KeyPress>", font_search)

        font_label = Label(nb.font_window, bg=cs.bgc, text=gn.lbl_font_name)
        font_label.grid_configure(row=16, columnspan=1, sticky="NSW")

        fs_label =Label(nb.font_window, bg=cs.bgc, text=gn.lbl_size)
        fs_label.grid_configure(row=16, column=3, columnspan=1, sticky="NSEW")

        fn_entry =Text(nb.font_window, width=35, height=8)
        fn_entry.grid_configure(row=18, columnspan=2, sticky="NSEW")

        fn_entry.tag_config("backdrop", background=cs.bgc)
        fn_entry.delete(0.0, END)

        for l in cs.font_list:
            fn_entry.insert(INSERT, l+"\n")

        def clear_tag(foo):
            fn_entry.tag_remove("backdrop", 0.0, END)
        def tag_it(foo):
            fn_entry.tag_add("backdrop", "insert linestart", "insert lineend")
            cs.font_hold = fn_entry.get("insert linestart", "insert lineend")
            display_label.configure(font=(cs.font_hold, 18, "bold"))

        fs_entry =Entry(nb.font_window, width=5)
        fs_entry.grid_configure(row=18, column=2, columnspan=1, sticky="NEW")

        fn_entry.bind("<Button-1>", clear_tag)
        fn_entry.bind("<ButtonRelease-1>", tag_it)
        fn_entry.bind("<Up>", clear_tag)
        fn_entry.bind("<KeyRelease-Up>", tag_it)
        fn_entry.bind("<Down>", clear_tag)
        fn_entry.bind("<KeyRelease-Down>", tag_it)
        font_submit = Button(nb.font_window, text=gn.btn_enter)
        font_submit.grid_configure(row=18, column=3, columnspan=1, sticky="NEW")
        font_submit.config(command=lambda: make_font(cs.font_hold, fs_entry, file_display, nb.conky_by_line))

        display_label = Label(nb.font_window, text="AaBbCc123:!#")
        display_label.grid_configure(row=20, column=0, columnspan=4, sticky="NSEW")

        nb.font_window.mainloop()

    def add_color_window(self):
        """color management window"""
        def update(color_alias, field_entry):
            """enter new colors based on hex, if not hex locate
            color name in file and return hex code"""
            config_window = nb.file_display.get(0.0, END)
            nb.file_display.delete(0.0, END)
            file_split = config_window.split("conky.text")
            config_split = file_split[0].splitlines()
            the_rest = file_split[1]
            for line in config_split:
                if str(color_alias) not in str(line):
                    nb.file_display.insert(INSERT, line+"\n")
                if str(color_alias) in str(line):
                    if field_entry.get().lower() in cs.color_names:
                        nb.file_display.insert(INSERT, "    "+color_alias+" = '"+cs.color_dict[field_entry.get().lower()]+"',\n")
                    if field_entry.get().lower() not in cs.color_names:
                        nb.file_display.insert(INSERT, "    "+color_alias+" = '"+field_entry.get().replace("#", '')+"',\n")
            nb.file_display.insert(INSERT, "conky.text"+the_rest)
            save_file(nb.file_display, nb.custom_window)

        nb.color_manager_window = Tk()
        nb.color_manager_window.grid()
        nb.color_manager_window.title(gn.win_colors)
        nb.color_manager_window.attributes("-topmost", True)
        file_colors = nb.custom_window.get(0.0, "end-1c").splitlines()

        default_color_label =Label(nb.color_manager_window, text="default_color")
        default_color_label.grid_configure(row=0, column=0, sticky="E")

        default_color_entry =Entry(nb.color_manager_window, width=8)
        default_color_entry.grid_configure(row=0, column=1)    

        default_color_button =Button(nb.color_manager_window, width=8, text=gn.btn_update, command=lambda: update("default_color", default_color_entry))
        default_color_button.grid_configure(row=0, column=2)
        
        color0_label =Label(nb.color_manager_window, text="color0")
        color0_label.grid_configure(row=1, column=0, sticky="E")

        color0_entry =Entry(nb.color_manager_window, width=8)
        color0_entry.grid_configure(row=1, column=1)

        color0_button =Button(nb.color_manager_window, width=8, text=gn.btn_update, command=lambda: update("color0", color0_entry))
        color0_button.grid_configure(row=1, column=2)
    
        color1_label =Label(nb.color_manager_window, text="color1")
        color1_label.grid_configure(row=2, column=0, sticky="E")

        color1_entry =Entry(nb.color_manager_window, width=8)
        color1_entry.grid_configure(row=2, column=1)

        color1_button =Button(nb.color_manager_window, width=8, text=gn.btn_update, command=lambda: update("color1", color1_entry))
        color1_button.grid_configure(row=2, column=2)
    
        color2_label =Label(nb.color_manager_window, text="color2")
        color2_label.grid_configure(row=3, column=0, sticky="E")

        color2_entry =Entry(nb.color_manager_window, width=8)
        color2_entry.grid_configure(row=3, column=1)

        color2_button =Button(nb.color_manager_window, width=8, text=gn.btn_update, command=lambda: update("color2", color2_entry))
        color2_button.grid_configure(row=3, column=2)
    
        color3_label =Label(nb.color_manager_window, text="color3")
        color3_label.grid_configure(row=4, column=0, sticky="E")

        color3_entry =Entry(nb.color_manager_window, width=8)
        color3_entry.grid_configure(row=4, column=1)

        color3_button =Button(nb.color_manager_window, width=8, text=gn.btn_update, command=lambda: update("color3", color3_entry))
        color3_button.grid_configure(row=4, column=2)
    
        color4_label =Label(nb.color_manager_window, text="color4")
        color4_label.grid_configure(row=5, column=0, sticky="E")

        color4_entry =Entry(nb.color_manager_window, width=8)
        color4_entry.grid_configure(row=5, column=1)

        color4_button =Button(nb.color_manager_window, width=8, text=gn.btn_update, command=lambda: update("color4", color4_entry))
        color4_button.grid_configure(row=5, column=2)
        
        color5_label =Label(nb.color_manager_window, text="color5")
        color5_label.grid_configure(row=6, column=0, sticky="E")

        color5_entry =Entry(nb.color_manager_window, width=8)
        color5_entry.grid_configure(row=6, column=1)

        color5_button =Button(nb.color_manager_window, width=8, text=gn.btn_update, command=lambda: update("color5", color5_entry))
        color5_button.grid_configure(row=6, column=2)
        
        color6_label =Label(nb.color_manager_window, text="color6")
        color6_label.grid_configure(row=7, column=0, sticky="E")

        color6_entry =Entry(nb.color_manager_window, width=8)
        color6_entry.grid_configure(row=7, column=1)

        color6_button =Button(nb.color_manager_window, width=8, text=gn.btn_update, command=lambda: update("color6", color6_entry))
        color6_button.grid_configure(row=7, column=2)
        
        color7_label =Label(nb.color_manager_window, text="color7")
        color7_label.grid_configure(row=8, column=0, sticky="E")

        color7_entry =Entry(nb.color_manager_window, width=8)
        color7_entry.grid_configure(row=8, column=1)

        color7_button =Button(nb.color_manager_window, width=8, text=gn.btn_update, command=lambda: update("color7", color7_entry))
        color7_button.grid_configure(row=8, column=2)
        
        color8_label =Label(nb.color_manager_window, text="color8")
        color8_label.grid_configure(row=9, column=0, sticky="E")

        color8_entry =Entry(nb.color_manager_window, width=8)
        color8_entry.grid_configure(row=9, column=1)

        color8_button =Button(nb.color_manager_window, width=8, text=gn.btn_update, command=lambda: update("color8", color8_entry))
        color8_button.grid_configure(row=9, column=2)
        
        color9_label =Label(nb.color_manager_window, text="color9")
        color9_label.grid_configure(row=10, column=0, sticky="E")

        color9_entry =Entry(nb.color_manager_window, width=8)
        color9_entry.grid_configure(row=10, column=1)

        color9_button =Button(nb.color_manager_window, width=8, text=gn.btn_update, command=lambda: update("color9", color9_entry))
        color9_button.grid_configure(row=10, column=2)

        for color in file_colors:
            name = color.split()[0]
            value = str(color.split()[2]).replace("'", '')
            entry_name = eval(name+"_entry")
            entry_name.insert(INSERT, value[0:-1])

        nb.color_manager_window.mainloop()

    def help_window(self, foo, help_file, help_title):
        def save_help():
            open_save = open(str(cs.help_path)+str(help_file), 'w')
            open_save.write(nb.help_text.get(0.0, "end-1c"))
            open_save.close()

        nb.help_win = Tk()
        nb.help_win.grid()
        nb.help_win.title(help_title)

        help_open = open(cs.help_path+help_file, 'r')
        help_read = help_open.read()
        help_open.close()

        nb.help_text =Text(nb.help_win, width=70, height=20, wrap='word')
        nb.help_text.grid(row=0, column=0)
        nb.help_text.insert(INSERT, help_read)

        if cs.editable == 'on':
            nb.help_save =Button(nb.help_win, text="save", command=save_help)
            nb.help_save.grid_configure(row=1, column=0, sticky="W")

        def help_exit():

            nb.help_win.destroy()

        nb.help_exit =Button(nb.help_win, text=gn.btn_exit, command=help_exit)
        nb.help_exit.grid(row=1, column=0, sticky="E")

        nb.help_win.mainloop()

    def image_window_fun(self):
        """create image command window"""
        def rs_x(self):
            """resize y when x is changed"""
            resize_x(size_x, size_y)

        def rs_y(self):
            """resize x when y is changed"""
            resize_y(size_x, size_y)

        def pic_size(self):
            image_dimensions(image_entry, size_x, size_y)
            align_image_x.insert(INSERT, '0')
            align_image_y.insert(INSERT, '0')

        nb.image_window = Tk()
        nb.image_window.title(gn.win_image)
        nb.image_window.grid()
        nb.image_window.config(bg="white")
        nb.image_window.attributes("-topmost", True)

        image_path_label =Label(nb.image_window, bg=cs.bgc, text="Image Path:")
        image_path_label.grid_configure(row=0, column=0, columnspan=3, sticky="NSEW")

        image_entry =Entry(nb.image_window, width=15)
        image_entry.grid_configure(row=1, column=0, columnspan=3, sticky="NSEW")

        size_label =Label(nb.image_window, bg=cs.bgc, text=gn.lbl_size, justify="left", width=20)
        size_label.grid_configure(row=2, column=0, columnspan=1, sticky="NSEW")

        size_x =Entry(nb.image_window, width=5)
        size_x.grid_configure(row=2, column=1, sticky='NSE')

        size_y =Entry(nb.image_window, width=5)
        size_y.grid_configure(row=2, column=2, sticky='NSW')

        im_align =Label(nb.image_window, bg=cs.bgc, text=gn.lbl_align, justify="left")
        im_align.grid_configure(row=3, column=0, columnspan=1, sticky="NSEW")

        align_image_x =Entry(nb.image_window, width=5)
        align_image_x.grid_configure(row=3, column=1, sticky='NSE')

        align_image_y =Entry(nb.image_window, width=5)
        align_image_y.grid_configure(row=3, column=2, sticky='NSW')

        enter_button =Button(nb.image_window, text=gn.btn_enter)
        enter_button.grid_configure(row=5, column=0, sticky="W")

        exit_button =Button(nb.image_window, text=gn.btn_exit, command=nb.image_window.destroy)
        exit_button.grid_configure(row=5, column=2, sticky="E")

        enter_button.config(command=lambda: add_image(image_entry, size_x, size_y, align_image_x, align_image_y, nb.file_display, nb.image_window))

        image_entry.bind('<Return>', pic_size)
        size_x.bind('<Return>', rs_x)
        size_y.bind('<Return>', rs_y)
        check = nb.file_display.get("insert linestart", "insert lineend")
        if "${image" in check:
            cs.image_toggle = "true"
        if "${image" not in check:
            cs.image_toggle = "false"
        image_from_line(nb.file_display, image_entry, size_x, size_y, align_image_x, align_image_y)

        nb.image_window.mainloop()

    def run(self):
        self.root.mainloop()

nb = Notebook(gn.win_main)
com = Notebook
nb.create_widgets(gn.editor)
nb.help_frame_fun()
load_commands(nb.com_list_box)
color_separator()
syntax_basic(nb.file_display)
fd_syntax_highlighting(nb.file_display)
cb_syntax(nb.custom_window)
font_list()
theme_list()

nb.run()