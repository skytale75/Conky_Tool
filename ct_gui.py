from tkinter import Frame, Radiobutton, ttk, Entry, Label, Text, Button, Tk, END, INSERT, StringVar, OptionMenu, IntVar, colorchooser, PhotoImage, LEFT
from ct_fun import Commands, functions
from ct_mod import search_su, load_commands, load_configs, load_lua, load_options, toggle_gb, toggle_pb, \
    save_file, show_def, add_custom, search, load_hold_color, duplicate_press, open_file, load_by_line, \
    insert_line, insert_line, syntax_basic, fd_syntax_highlighting, cbl_update, theme_prompt, read_theme_list, \
    get_theme, make_font, resize_x, resize_y, image_dimensions, add_image, image_from_line, color_separator, \
    cb_syntax, font_list, theme_list, open_color_file
from common_stuff import Common_Stuff as cs
from os import listdir
from PIL import Image, ImageTk
from gui_names import gui_names as gn
import subprocess
from tkcolorpicker import askcolor
from tkinter.filedialog import askopenfilename


class Utilize_Conky:

    def __init__(self, title):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry("1024x768")
        self.root.bind('<Control-q>', exit)
        self.root.grid()

        rows = 0
        while rows < 21:
            self.root.rowconfigure(rows, weight = 100)
            self.root.columnconfigure(rows, weight = 100)
            rows += 1

    def create_widgets(self, title):
        """create all widgets"""
        uc.frame = Frame(self.root)
        uc.frame.grid(row = 0, columnspan=21)
        uc.frame.grid_configure(sticky="NSEW")
        uc.frame.columnconfigure(17, weight = 100)
        uc.frame.columnconfigure(18, weight = 100)
        uc.frame.rowconfigure(5, weight = 100)
        uc.frame.rowconfigure(7, weight = 100)
        uc.frame.config(bg=cs.bgc)

        uc.v =IntVar()

        def cr_com():

            uc.com_list_box.delete(0.0, END)
            cs.selected = "commands"
            load_commands(uc.com_list_box)

        def cr_con():
            uc.com_list_box.delete(0.0, END)
            cs.selected = "configs"
            load_configs(uc.com_list_box)

        def cr_lua():
            uc.com_list_box.delete(0.0, END)
            cs.selected = "lua"
            load_lua(uc.com_list_box)

        def cr_options():
            cs.selected = "options"
            uc.com_list_box.delete(0.0, END)
            load_options(uc.wiki_window)
        
        uc.com_radio =Radiobutton(uc.frame, indicatoron=0, width=20, bg=cs.bgc, text=gn.rb_commands, variable=uc.v, value=1, command = cr_com)
        uc.com_radio.grid_configure(row=0, column=0, columnspan=5, sticky="NSEW")
        uc.com_radio.select()

        uc.con_radio =Radiobutton(uc.frame, indicatoron=0, width=20, bg=cs.bgc, text=gn.rb_configs, variable=uc.v, value=2, command = cr_con)
        uc.con_radio.grid_configure(row=1, column=0, columnspan=5, sticky="NSEW")

        uc.lua_radio =Radiobutton(uc.frame, indicatoron=0, width=20, bg=cs.bgc, text=gn.rb_lua, variable=uc.v, value=3, command = cr_lua)
        uc.lua_radio.grid_configure(row=2, column=0, columnspan=5, sticky="NSEW")

        uc.options_radio =Radiobutton(uc.frame, indicatoron=0, width=20, bg=cs.bgc, text=gn.rb_options, variable=uc.v, value=4, command = cr_options)
        uc.options_radio.grid_configure(row=3, column=0, columnspan=5, sticky="NSEW")

        uc.command_find =Entry(uc.frame, width=20, bg="darkblue", fg="white", font= ('Deja Vu Serif', 10))
        uc.command_find.grid_configure(row=4, column=0, columnspan=5, sticky="NSEW")

        uc.conky_label =Label(uc.frame, bg=cs.bgc, text=cs.config_file, justify='left')
        uc.conky_label.grid_configure(row=0, column=10, columnspan=11, sticky="NSEW")

        uc.com_list_box =Text(uc.frame, height=10, width=20, bg="lightblue", font= ('Deja Vu Serif', 10))
        uc.com_list_box.grid_configure(row=5, column=0, columnspan=5, sticky="NSEW")

        uc.lnText = Text(uc.frame, width = 4, padx = 4, highlightthickness = 0, takefocus = 0,
                bd = 0, background = 'lightgrey', foreground = 'magenta', state='disabled')

        uc.file_display =Text(uc.frame, wrap = 'word', undo=True, height=80)
        uc.file_display.grid_configure(row=1, column=10, columnspan=11, rowspan=20, sticky="NSEW")
        uc.file_display.config(bg="black", fg="white", insertbackground = 'cyan', font= ('Deja Vu Serif', 10))

        uc.wiki_label =Label(uc.frame, width=40, bg=cs.bgc, text=gn.lbl_description)
        uc.wiki_label.grid_configure(row=6, column=0, columnspan=10)

        uc.wiki_window =Text(uc.frame, wrap='word', width=20, bg = "lightyellow", font= ('Deja Vu Serif', 10))
        uc.wiki_window.grid_configure(row=7, column=0, rowspan=14, columnspan=10, sticky="NSEW")

        color_img = ImageTk.PhotoImage(Image.open (cs.image_path+"colors.png"))
        uc.color_button =Button(uc.frame, image=color_img, command=uc.add_color_window)
        uc.color_button.grid_configure(row=21, column=10, sticky="NESW")
        uc.color_button.image=color_img

        fonts_img = ImageTk.PhotoImage(Image.open (cs.image_path+"fonts.png"))
        uc.fonts_button =Button(uc.frame, image=fonts_img, command=lambda: uc.font_window_fun(uc.file_display))
        uc.fonts_button.grid_configure(row=21, column=11, sticky='NSEW')
        uc.fonts_button.image=fonts_img

        image_img = ImageTk.PhotoImage(Image.open (cs.image_path+"images.png"))
        uc.image_button =Button(uc.frame, image=image_img, command =uc.image_window_fun)
        uc.image_button.grid_configure(row=21, column=12, sticky="NSEW")
        uc.image_button.image=image_img

        page_borders_img = ImageTk.PhotoImage(Image.open (cs.image_path+"tog_page_border.png"))
        uc.page_borders =Button(uc.frame, image=page_borders_img, command=lambda: toggle_pb(uc.file_display, uc.custom_window))
        uc.page_borders.grid_configure(row=21, column=13)
        uc.page_borders.image=page_borders_img

        graph_borders_img = ImageTk.PhotoImage(Image.open (cs.image_path+"tog_graph_border.png"))
        uc.graph_borders =Button(uc.frame, image=graph_borders_img, command=lambda: toggle_gb(uc.file_display, uc.custom_window))
        uc.graph_borders.grid_configure(row=21, column=14, sticky="NSEW")
        uc.graph_borders.image=graph_borders_img

        pagify_img = ImageTk.PhotoImage(Image.open (cs.image_path+"pagify.png"))
        uc.pagify =Button(uc.frame, image=pagify_img, command=lambda: uc.conky_by_line(self))
        uc.pagify.grid_configure(row=21, column=15, sticky="NSEW")
        uc.pagify.image=pagify_img

        themes_img = ImageTk.PhotoImage(Image.open (cs.image_path+"themes.png"))
        uc.themes_button =Button(uc.frame, image=themes_img, command=uc.themes_window)
        uc.themes_button.grid_configure(row=21, column=16, sticky='NSEW')
        uc.themes_button.image=themes_img

        uc.custom = Label(uc.frame, width=20, bg=cs.bgc, text=gn.lbl_custom)
        uc.custom.grid_configure(row=0, column=5, columnspan=5)

        uc.custom_window =Text(uc.frame, height=10, width=20, wrap="word", bg="darkgrey", fg="cyan")
        uc.custom_window.grid_configure(row=1, column=5, columnspan=5, rowspan=5, sticky="NWSE")

        uc.save_button =Button(uc.frame, text=gn.btn_save, fg='red', command=lambda: save_file(uc.file_display, uc.custom_window))
        uc.save_button.grid_configure(row=21, column=19, sticky='NSEW')

        uc.quit =Button(uc.frame,text=gn.btn_quit, fg="red", command=self.root.destroy)
        uc.quit.grid_configure(row=21, column=20, sticky='NSEW')

        def command_line(self):
            """locate command in dictionary and enter
            into file_display, or open options window"""
            #check = uc.file_display.get("insert")
            #print(check)
            if cs.hold_command != '':
                if cs.selected == "commands":
                    the_input = cs.hold_command
                    functions[the_input](uc.file_display)
            
            return "break"

        def definition(self):
            """tie into show_def, which automatically
            displays definition iadd_cc window"""
            show_def(uc.com_list_box, uc.wiki_window)
        def ps_command(self):
            """tie into add_custom, which adds custom
            color or font to file"""
            add_custom(uc.custom_window, uc.file_display)
            return 'break'
        def search_com(self):
            if uc.command_find.get() == '' and cs.hold_command == "commands":
                cs.results = []
                uc.com_list_box.delete(0.0, END)
                load_commands(uc.com_list_box)
            if uc.command_find.get() == '' and cs.hold_command == "configs":
                cs.results = []
                uc.com_list_box.delete(0.0, END)
                load_configs(uc.com_list_box)
            if uc.command_find.get() == '-e on':
                cs.editable = 'on'
            if uc.command_find.get() == '-e off':
                cs.editable = 'off'
            else:
                search(uc.command_find, uc.com_list_box)
        def force_def(self):
            Commands.force_file(self, uc.wiki_window, uc.file_display)
        def clear_tag(self):
            uc.com_list_box.tag_remove("command", 0.0, END)
        def tab(self):
            uc.file_display.insert(INSERT, "    ")
            return "break"
        def hc(self):
            load_hold_color(uc.custom_window)
        def dup_down(self):
            duplicate_press(uc.file_display)
            return "break"
        def file_display_help(self):
            uc.help_window(self, "help_editor.txt", "Editor Help")
            return "break"
        def search_help(self):
            uc.help_window(self, "help_search.txt", "Search Bar Help")
        def definitions_help(self):
            uc.help_window(self, "help_definitions.txt", "Help, Definitions")
        def command_box_help(self):
            uc.help_window(self, 'help_CL.txt', "Command Box Help")
        def custom_help(self):
            uc.help_window(self, "help_custom.txt", "Custom Colors Help")
        def save_kc(self):
            save_file(uc.file_display, uc.custom_window)
        def launch_conky(self):
            subprocess.call('conky',shell="true")
        def check_window(self):
            if 'normal' == uc.font_window_fun.state():
                print('font window open')
        def delete_cl(self):
            if cs.cl_toggle == 1:
                uc.command_find.delete(0, END)
                cs.cl_toggle = 0

        
        uc.com_list_box.tag_config("command", background="white")
        uc.com_list_box.bind('<KeyRelease-Down>', definition)
        uc.com_list_box.bind('<Down>', clear_tag)
        uc.com_list_box.bind('<KeyRelease-Up>', definition)
        uc.com_list_box.bind('<Up>', clear_tag)
        uc.com_list_box.bind('<Control-Return>', command_line)
        uc.com_list_box.bind('<Button-1>', clear_tag)
        uc.com_list_box.bind('<ButtonRelease-1>', definition)
        uc.com_list_box.bind('<Control-h>', command_box_help)
        uc.file_display.bind('<Alt-p>', uc.conky_by_line)
        uc.file_display.bind('<Control-f>', check_window)
        uc.file_display.bind("<Tab>", tab)
        uc.file_display.bind('<Control-Return>', command_line)
        uc.file_display.bind('<Control-ButtonRelease-1>', command_line)
        uc.file_display.bind('<Shift-Control-Return>', ps_command)
        uc.file_display.bind('<Shift-Control-ButtonRelease-1>', ps_command)
        uc.file_display.bind('<Control-d>', dup_down)
        uc.file_display.bind('<Control-s>', save_kc)
        uc.wiki_window.bind('<Control-Return>', force_def)
        uc.wiki_window.bind('<Control-Button-1>', force_def)
        uc.wiki_window.bind('<Control-h>', definitions_help)
        uc.command_find.bind('<ButtonRelease-1>', delete_cl)
        uc.command_find.bind('<KeyRelease>', search_com)
        uc.command_find.bind('<Control-h>', search_help)
        uc.custom_window.bind('<Shift-Control-Return>', ps_command)
        uc.custom_window.bind('<ButtonRelease-1>', hc)
        uc.custom_window.bind('<KeyRelease-Up>', hc)
        uc.custom_window.bind('<KeyRelease-Down>', hc)
        uc.custom_window.bind('<Control-h>', custom_help)
        uc.file_display.bind("<Control-l>", launch_conky)
        uc.file_display.bind("<Control-h>", file_display_help)

        open_file(uc.file_display, uc.custom_window)
        uc.command_find.insert(INSERT, "Search commands . . .")

    def conky_by_line(self, foo):
        uc.cbl_window = Tk()
        uc.cbl_window.grid()
        uc.cbl_window.attributes("-topmost", 'true')
        uc.cbl_window.title("Conky by line")

        uc.cbl_text =Text(uc.cbl_window, width=40, height = 30)
        uc.cbl_text.grid_configure(row=0, column=0, columnspan=5)
        uc.cbl_text.config(bg="black", fg="white", insertbackground = 'cyan', font= ('Deja Vu Serif', 10))

        def cbl_command_custom(self):
            """add_custom to conky by line window"""
            add_custom(uc.custom_window, uc.cbl_text)
        def cbl_command_enter(self):
            if cs.selected == "commands":
                the_input = cs.hold_command
                functions[the_input](uc.cbl_text)
            return "break"

        load_by_line(uc.com_list_box, uc.custom_window, uc.file_display)
        insert_line(uc.cbl_text)

        syntax_basic(uc.cbl_text)
        fd_syntax_highlighting(uc.cbl_text)

        uc.cbl_enter =Button(uc.cbl_window, text="Update", command=lambda: cbl_update(uc.cbl_text, uc.com_list_box, uc.custom_window, uc.file_display))
        uc.cbl_enter.grid_configure(row=2, column=4, sticky="NSEW")

        uc.cbl_font =Button(uc.cbl_window, text="fonts", command = lambda: uc.font_window_fun(uc.cbl_text))
        uc.cbl_font.grid_configure(row=2, column=1, sticky="NWES")

        uc.cbl_exit =Button(uc.cbl_window, text="Exit", command=uc.cbl_window.destroy)
        uc.cbl_exit.grid_configure(row=2, column=0, sticky="NSEW")
        
        uc.cbl_text.bind("<Control-Return>", cbl_command_enter)
        uc.cbl_text.bind("<Control-Button-1>", cbl_command_enter)
        uc.cbl_text.bind("<Shift-Control-Return>", cbl_command_custom)
        uc.cbl_text.bind("<Shift-Control-Button-1>", cbl_command_custom)

        uc.cbl_window.after(5000, lambda: uc.cbl_window.focus_force())

    def themes_window(self):
        """create themes properties window"""

        uc.window = Tk()
        uc.window.grid()
        uc.window.title(gn.win_themes)
        uc.window.attributes("-topmost", True)

        theme_name =Label(uc.window, bg=cs.bgc, text=gn.lbl_theme_name)
        theme_name.grid_configure(row=0, column=0, columnspan=1)

        theme_display =Entry(uc.window)
        theme_display.grid_configure(row=0, column=1, columnspan=1, sticky="NSEW")

        save_theme_button =Button(uc.window, text=gn.btn_save_theme, command=lambda: theme_prompt(theme_display, uc.file_display))
        save_theme_button.grid_configure(row=0, column=2, columnspan=1, sticky="NSEW")

        open_theme_label =Label(uc.window, text=gn.lbl_open_theme)
        open_theme_label.grid_configure(row=1, column=0, sticky='NSEW')

        theme_list = read_theme_list()
        option_header =StringVar(uc.window)
        option_header.set(theme_list[0])

        themes_list =OptionMenu(uc.window, option_header, *theme_list)
        themes_list.grid_configure(row=1, column=1, columnspan=1, sticky="NSEW")

        theme_button =Button(uc.window, text=gn.btn_load_theme)
        theme_button.grid_configure(row=1, column=2, columnspan=1, sticky="NSEW")
        theme_button.config(command=lambda: get_theme(uc.file_display, option_header, uc.custom_window))

        uc.window.mainloop()

    def font_window_fun(self, file_display):
        """create font properties window"""
        uc.font_window = Tk()
        uc.font_window.grid()
        uc.font_window.title(str(len(cs.font_list))+" "+gn.win_fonts)
        uc.font_window.attributes("-topmost", True)

        cs.toggle=0

        def font_search(foo):
            the_search = font_search_bar.get()
            fn_entry.delete(0.0, END)
            for l in cs.font_list:
                if the_search.lower() in str(l).lower():
                    fn_entry.insert(INSERT, l+"\n")

        def clear_entry(foo):
            search_su(font_search_bar)

        # Font Search bar widget

        font_search_bar = Entry(uc.font_window, bg="darkblue", fg="white")
        font_search_bar.grid_configure(row=0, column=0, columnspan=2, sticky="NESW")
        font_search_bar.insert(INSERT, "Search fonts . . .")
        font_search_bar.bind("<Button-1>", clear_entry)
        font_search_bar.bind("<KeyPress>", font_search)

        # "Font Name:" label

        font_label = Label(uc.font_window, bg=cs.bgc, text=gn.lbl_font_name)
        font_label.grid_configure(row=16, columnspan=1, sticky="NSW")

        # Font "size" label

        fs_label = Label(uc.font_window, bg=cs.bgc, text=gn.lbl_size)
        fs_label.grid_configure(row=16, column=2, columnspan=1, sticky="NSEW")

        # Where fonts are listed

        fn_entry = Text(uc.font_window, width=35, height=8)
        fn_entry.grid_configure(row=18, columnspan=2, rowspan=8, sticky="NSEW")

        fn_entry.tag_config("backdrop", background=cs.bgc)
        fn_entry.delete(0.0, END)

        # Font Size entry widget

        fs_entry = Entry(uc.font_window, width=5)
        fs_entry.grid_configure(row=18, column=2, columnspan=1, sticky="NSEW")

        for l in cs.font_list:
            fn_entry.insert(INSERT, l+"\n")

        def get_fs():
            get_it = fs_entry.get()
            if get_it == "":
                get_it = 14
            cs.fs_hold = get_it

        def clear_tag(foo):
            fn_entry.tag_remove("backdrop", 0.0, END)

        def tag_it(foo):
            fn_entry.tag_add("backdrop", "insert linestart", "insert lineend")
            cs.font_hold = fn_entry.get("insert linestart", "insert lineend")
            get_fs()
            display_label.configure(font=(cs.font_hold, cs.fs_hold))

        fn_entry.bind("<Button-1>", clear_tag)
        fn_entry.bind("<ButtonRelease-1>", tag_it)
        fn_entry.bind("<Up>", clear_tag)
        fn_entry.bind("<KeyRelease-Up>", tag_it)
        fn_entry.bind("<Down>", clear_tag)
        fn_entry.bind("<KeyRelease-Down>", tag_it)

        font_submit = Button(uc.font_window, text=gn.btn_enter)
        font_submit.grid_configure(row=18, column=3, columnspan=1, sticky="NSEW")
        font_submit.config(command=lambda: make_font(cs.font_hold, fs_entry, file_display, uc.conky_by_line))

        display_label = Label(uc.font_window, text="AaBbCc123:!#")
        display_label.grid_configure(row=30, column=0, rowspan=4, columnspan=4, sticky="NSEW")

        uc.font_window.mainloop()


    def add_color_window(self):
        """color management window"""
        uc.color_manager_window = Tk()
        uc.color_manager_window.grid()
        uc.color_manager_window.title(gn.win_colors)
        uc.color_manager_window.attributes("-topmost", True)
        uc.color_manager_window.config(bg="#000000")
        file_colors = uc.custom_window.get(0.0, "end-1c").splitlines()

        def color_chooser(color_out, mbutton):
            grab_color = color_out.get()
            color_code = askcolor("#"+grab_color, title ="Choose color")
            if "None" not in str(color_code):
                color_out.delete(0, END)
                color_out.insert(INSERT, color_code[1][1:])
                mbutton.config(bg=color_code[1])

        def update(color_alias, field_entry, my_button):
            """enter new colors based on hex, if not hex locate
            color name in file and return hex code"""
            config_window = uc.file_display.get(0.0, END)
            uc.file_display.delete(0.0, END)
            file_split = config_window.split("conky.text")
            config_split = file_split[0].splitlines()
            the_rest = file_split[1]
            new_color = field_entry.get().lower()
            for line in config_split:
                if str(color_alias) not in str(line):
                    uc.file_display.insert(INSERT, line+"\n")
                if str(color_alias) in str(line):
                    if new_color in cs.color_names:
                        uc.file_display.insert(INSERT, "    "+color_alias+" = '"+cs.color_dict[new_color]+"',\n")
                    if new_color not in cs.color_names:
                        uc.file_display.insert(INSERT, "    "+color_alias+" = '"+new_color.replace("#", '')+"',\n")
            my_button.config(bg="#"+new_color)
            uc.file_display.insert(INSERT, "conky.text"+the_rest)
            save_file(uc.file_display, uc.custom_window)

        default_color_chooser = Button(uc.color_manager_window, text="default", command=lambda: color_chooser(default_color_entry, default_color_chooser))
        default_color_chooser.grid_configure(row=0, column=0, sticky="NSEW")

        default_color_entry =Entry(uc.color_manager_window, width=8)
        default_color_entry.grid_configure(row=0, column=1)    

        default_color_button =Button(uc.color_manager_window, width=8, text=gn.btn_update, command=lambda: update("default_color", default_color_entry, default_color_button))
        default_color_button.grid_configure(row=0, column=2)
        
        color0_chooser = Button(uc.color_manager_window, text="color0", command=lambda: color_chooser(color0_entry, color0_chooser))
        color0_chooser.grid_configure(row=1, column=0, sticky="NSEW")

        color0_entry =Entry(uc.color_manager_window, width=8)
        color0_entry.grid_configure(row=1, column=1)

        color0_button =Button(uc.color_manager_window, width=8, text=gn.btn_update, command=lambda: update("color0", color0_entry, color0_button))
        color0_button.grid_configure(row=1, column=2)
    
        color1_chooser = Button(uc.color_manager_window, text="color1", command=lambda: color_chooser(color1_entry, color1_chooser))
        color1_chooser.grid_configure(row=2, column=0, sticky="NSEW")

        color1_entry =Entry(uc.color_manager_window, width=8)
        color1_entry.grid_configure(row=2, column=1)

        color1_button =Button(uc.color_manager_window, width=8, text=gn.btn_update, command=lambda: update("color1", color1_entry, color1_button))
        color1_button.grid_configure(row=2, column=2)
    
        color2_chooser = Button(uc.color_manager_window, text="color2", command=lambda: color_chooser(color2_entry, color2_chooser))
        color2_chooser.grid_configure(row=3, column=0, sticky="NSEW")

        color2_entry =Entry(uc.color_manager_window, width=8)
        color2_entry.grid_configure(row=3, column=1)

        color2_button =Button(uc.color_manager_window, width=8, text=gn.btn_update, command=lambda: update("color2", color2_entry, color2_button))
        color2_button.grid_configure(row=3, column=2)
    
        color3_chooser = Button(uc.color_manager_window, text="color3", command=lambda: color_chooser(color3_entry, color3_chooser))
        color3_chooser.grid_configure(row=4, column=0, sticky="NSEW")

        color3_entry =Entry(uc.color_manager_window, width=8)
        color3_entry.grid_configure(row=4, column=1)

        color3_button =Button(uc.color_manager_window, width=8, text=gn.btn_update, command=lambda: update("color3", color3_entry, color3_button))
        color3_button.grid_configure(row=4, column=2)
    
        color4_chooser = Button(uc.color_manager_window, text="color4", command=lambda: color_chooser(color4_entry, color4_chooser))
        color4_chooser.grid_configure(row=5, column=0, sticky="NSEW")

        color4_entry =Entry(uc.color_manager_window, width=8)
        color4_entry.grid_configure(row=5, column=1)

        color4_button =Button(uc.color_manager_window, width=8, text=gn.btn_update, command=lambda: update("color4", color4_entry, color4_button))
        color4_button.grid_configure(row=5, column=2)
        
        color5_chooser = Button(uc.color_manager_window, text="color5", command=lambda: color_chooser(color5_entry, color5_chooser))
        color5_chooser.grid_configure(row=6, column=0, sticky="NSEW")

        color5_entry =Entry(uc.color_manager_window, width=8)
        color5_entry.grid_configure(row=6, column=1)

        color5_button =Button(uc.color_manager_window, width=8, text=gn.btn_update, command=lambda: update("color5", color5_entry, color5_button))
        color5_button.grid_configure(row=6, column=2)
        
        color6_chooser = Button(uc.color_manager_window, text="color6", command=lambda: color_chooser(color6_entry, color6_chooser))
        color6_chooser.grid_configure(row=7, column=0, sticky="NSEW")

        color6_entry =Entry(uc.color_manager_window, width=8)
        color6_entry.grid_configure(row=7, column=1)

        color6_button =Button(uc.color_manager_window, width=8, text=gn.btn_update, command=lambda: update("color6", color6_entry, color6_button))
        color6_button.grid_configure(row=7, column=2)
        
        color7_chooser = Button(uc.color_manager_window, text="color7", command=lambda: color_chooser(color7_entry, color7_chooser))
        color7_chooser.grid_configure(row=8, column=0, sticky="NSEW")

        color7_entry =Entry(uc.color_manager_window, width=8)
        color7_entry.grid_configure(row=8, column=1)

        color7_button =Button(uc.color_manager_window, width=8, text=gn.btn_update, command=lambda: update("color7", color7_entry, color7_button))
        color7_button.grid_configure(row=8, column=2)
        
        color8_chooser = Button(uc.color_manager_window, text="color8", command=lambda: color_chooser(color8_entry, color8_chooser))
        color8_chooser.grid_configure(row=9, column=0, sticky="NSEW")

        color8_entry =Entry(uc.color_manager_window, width=8)
        color8_entry.grid_configure(row=9, column=1)

        color8_button =Button(uc.color_manager_window, width=8, text=gn.btn_update, command=lambda: update("color8", color8_entry, color8_button))
        color8_button.grid_configure(row=9, column=2)
        
        color9_chooser = Button(uc.color_manager_window, text="color9", command=lambda: color_chooser(color9_entry, color9_chooser))
        color9_chooser.grid_configure(row=10, column=0, sticky="NSEW")

        color9_entry =Entry(uc.color_manager_window, width=8)
        color9_entry.grid_configure(row=10, column=1)

        color9_button =Button(uc.color_manager_window, width=8, text=gn.btn_update, command=lambda: update("color9", color9_entry, color9_button))
        color9_button.grid_configure(row=10, column=2)

        import_button = Button(uc.color_manager_window, text="Import Color Pallet", command=lambda: open_color_file(\
            color0_chooser, color0_entry, color1_chooser, color1_entry, color2_chooser, color2_entry, \
            color3_chooser, color3_entry, color4_chooser, color4_entry, color5_chooser, color5_entry, \
            color6_chooser, color6_entry, color7_chooser, color7_entry, color8_chooser, color8_entry, \
            color9_chooser, color9_entry))
        import_button.grid_configure(row=14, columnspan=3, sticky="NSEW")

        for color in file_colors:
            name = color.split()[0]
            value = str(color.split()[2][1:-2])
            entry_name = eval(name+"_entry")
            entry_name.insert(INSERT, value)
            button_name = eval(name+"_button")
            button_name.config(bg="#"+value)
            label_name = eval(name+"_chooser")
            label_name.config(bg='#'+value)


        uc.color_manager_window.mainloop()

    def help_window(self, foo, help_file, help_title):
        def save_help():
            open_save = open(str(cs.help_path)+str(help_file), 'w')
            open_save.write(uc.help_text.get(0.0, "end-1c"))
            open_save.close()

        uc.help_win = Tk()
        uc.help_win.grid()
        uc.help_win.title(help_title)

        help_open = open(cs.help_path+help_file, 'r')
        help_read = help_open.read()
        help_open.close()

        uc.help_text =Text(uc.help_win, width=70, height=20, wrap='word')
        uc.help_text.grid(row=0, column=0)
        uc.help_text.insert(INSERT, help_read)

        if cs.editable == 'on':
            uc.help_save =Button(uc.help_win, text="save", command=save_help)
            uc.help_save.grid_configure(row=1, column=0, sticky="W")

        def help_exit():

            uc.help_win.destroy()

        uc.help_exit =Button(uc.help_win, text=gn.btn_exit, command=help_exit)
        uc.help_exit.grid(row=1, column=0, sticky="E")

        uc.help_win.mainloop()

    def image_window_fun(self):
        """create image command window"""

        def open_file():
            name = askopenfilename(initialdir="~/Pictures/")
            image_entry.delete(0, END)
            image_entry.insert(INSERT, name)
            pic_size(self)

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

        uc.image_window = Tk()
        uc.image_window.title(gn.win_image)
        uc.image_window.grid()
        uc.image_window.config(bg="white")
        uc.image_window.attributes("-topmost", True)

        image_path_label =Label(uc.image_window, bg=cs.bgc, text="Image Path:")
        image_path_label.grid_configure(row=0, column=0, columnspan=3, sticky="NSEW")

        image_dialogue = Button(uc.image_window, width=15, fg="#ffffff", bg="#000000", command= open_file, text="Select Image")
        image_dialogue.grid_configure(row=1, column=0, columnspan=3, sticky="NSEW")

        size_label =Label(uc.image_window, bg=cs.bgc, text=gn.lbl_size, justify="left", width=20)
        size_label.grid_configure(row=2, column=0, columnspan=1, sticky="NSEW")

        size_x =Entry(uc.image_window, width=5)
        size_x.grid_configure(row=2, column=1, sticky='NSE')

        size_y =Entry(uc.image_window, width=5)
        size_y.grid_configure(row=2, column=2, sticky='NSW')

        im_align =Label(uc.image_window, bg=cs.bgc, text=gn.lbl_align, justify="left")
        im_align.grid_configure(row=3, column=0, columnspan=1, sticky="NSEW")

        align_image_x =Entry(uc.image_window, width=5)
        align_image_x.grid_configure(row=3, column=1, sticky='NSE')

        align_image_y =Entry(uc.image_window, width=5)
        align_image_y.grid_configure(row=3, column=2, sticky='NSW')

        image_entry = Entry(uc.image_window)
        image_entry.grid_configure(row=4, columnspan=3, sticky="NSEW")

        enter_button =Button(uc.image_window, text=gn.btn_enter)
        enter_button.grid_configure(row=5, column=0, sticky="W")

        exit_button =Button(uc.image_window, text=gn.btn_exit, command=uc.image_window.destroy)
        exit_button.grid_configure(row=5, column=2, sticky="E")

        enter_button.config(command=lambda: add_image(image_entry, size_x, size_y, align_image_x, align_image_y, uc.file_display, uc.custom_window))

        image_entry.bind('<Return>', pic_size)
        size_x.bind('<Return>', rs_x)
        size_y.bind('<Return>', rs_y)
        check = uc.file_display.get("insert linestart", "insert lineend")
        if "${image" in check:
            cs.image_toggle = "true"
        if "${image" not in check:
            cs.image_toggle = "false"
        image_from_line(uc.file_display, image_entry, size_x, size_y, align_image_x, align_image_y)

        uc.image_window.mainloop()

    def run(self):
        self.root.mainloop()

uc = Utilize_Conky(gn.win_main)
com = Utilize_Conky
uc.create_widgets(gn.editor)
load_commands(uc.com_list_box)
color_separator()
syntax_basic(uc.file_display)
fd_syntax_highlighting(uc.file_display)
cb_syntax(uc.custom_window)
font_list()
theme_list()

uc.run()