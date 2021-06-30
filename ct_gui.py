#testing
from tkinter import Frame, Radiobutton, ttk, Entry, Label, Text, Button, Tk, END, INSERT, StringVar, OptionMenu, IntVar, colorchooser, PhotoImage, LEFT
from ct_fun import Commands, functions
from ct_mod import search_su, load_commands, load_configs, load_lua, load_options, toggle_gb, toggle_pb, \
    save_file, show_def, add_custom, search, load_hold_color, duplicate_press, open_file, load_by_line, \
    insert_line, insert_line, syntax_basic, fd_syntax_highlighting, cbl_update, theme_prompt, read_theme_list, \
    get_theme, make_font, resize_x, resize_y, image_dimensions, add_image, image_from_line, color_separator, \
    cb_syntax, font_list, theme_list, add_cc_update, load_the_colors, update_colors, update_gui, color_chooser, \
    filter_color_list, open_color_dialog, open_color_file
from common_stuff import Common_Stuff as cs
from os import listdir
from PIL import Image, ImageTk
from gui_names import gui_names as gn
import subprocess
from tkinter.filedialog import askopenfilename
from new_tips import Tooltip as tt

class Utilize_Conky():

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
        """All the widgets in the main window"""
        uc.frame = Frame(self.root)
        uc.frame.grid(row = 0, columnspan=21)
        uc.frame.grid_configure(sticky="NSEW")
        uc.frame.columnconfigure(17, weight = 100)
        uc.frame.columnconfigure(18, weight = 100)
        uc.frame.rowconfigure(5, weight = 100)
        uc.frame.rowconfigure(7, weight = 100)
        uc.frame.config(bg=cs.bgc)

        uc.v =IntVar()

        # list of commands to clear com_list_box
        # and load appropriate commands after pushing
        # the radio button, top left hand corner of the
        # main window

        

        def cr_com():
            """commands button clear box
            and load commands"""
            uc.com_list_box.delete(0.0, END)
            cs.selected = "commands"
            load_commands(uc.com_list_box)

        def cr_con():
            """configurations button clear box
            and load configurations"""
            uc.com_list_box.delete(0.0, END)
            cs.selected = "configs"
            load_configs(uc.com_list_box)

        def cr_lua():
            """clear box and do nothing, this
            is yet to come"""
            uc.com_list_box.delete(0.0, END)
            cs.selected = "lua"
            load_lua(uc.com_list_box)

        def cr_options():
            """clear commands box and load
            definitions in definiton window"""
            cs.selected = "options"
            uc.com_list_box.delete(0.0, END)
            load_options(uc.wiki_window)
        
        tooltip_size = 12

        # radio button located on top left of main window

        uc.com_radio =Radiobutton(uc.frame, indicatoron=0, width=20, bg=cs.bgc, text=gn.rb_commands, variable=uc.v, value=1, command = cr_com)
        uc.com_radio.grid_configure(row=0, column=0, columnspan=5, sticky="NSEW")
        uc.com_radio.select()
        uc.com_radio_tt = tt(uc.com_radio, "Click to Show list \n of conky commands", text_size=tooltip_size)

        uc.con_radio =Radiobutton(uc.frame, indicatoron=0, width=20, bg=cs.bgc, text=gn.rb_configs, variable=uc.v, value=2, command = cr_con)
        uc.con_radio.grid_configure(row=1, column=0, columnspan=5, sticky="NSEW")

        uc.lua_radio =Radiobutton(uc.frame, indicatoron=0, width=20, bg=cs.bgc, text=gn.rb_lua, variable=uc.v, value=3, command = cr_lua)
        uc.lua_radio.grid_configure(row=2, column=0, columnspan=5, sticky="NSEW")
        uc.lua_tt = tt(uc.lua_radio, "try this", text_size=tooltip_size)

        uc.options_radio =Radiobutton(uc.frame, indicatoron=0, width=20, bg=cs.bgc, text=gn.rb_options, variable=uc.v, value=4, command = cr_options)
        uc.options_radio.grid_configure(row=3, column=0, columnspan=5, sticky="NSEW")
        uc.or_tt = tt(uc.options_radio, "click to show startup\noptions for conky.\nWill be adding conky\nconfiguration tips eventually", text_size=tooltip_size)

        # entry field that allows users to search through the dictionary of commands as defined in the 
        # ct_mod.py file

        uc.command_find =Entry(uc.frame, width=20, bg="darkblue", fg="white", font= ('Deja Vu Serif', 10))
        uc.command_find.grid_configure(row=4, column=0, columnspan=5, sticky="NSEW")
        uc.command_find_tt = tt(uc.command_find, "^ Search for commands", text_size=tooltip_size)

        # conky_label shows a readout of the file location of the current file displayed in the main window,
        # for now it only displays the .config file, will update to display a theme file if it hasn't been saved
        # to the .conf file yet.

        uc.conky_label =Label(uc.frame, bg=cs.bgc, text=cs.config_file, justify='left')
        uc.conky_label.grid_configure(row=0, column=10, columnspan=11, sticky="NSEW")
        uc.fd_tt = tt(uc.conky_label, \
        """Ctrl-LeftClick to add highlighted commands,\n\
Ctrl-Shift-LeftClick to insert highlighted color\n\
Make sure cursor isn't sitting to the right of \n\
a '$'. I will be adding file checks to make sure a\n\
two dollar signs don't get input side by side, but\n\
for now just check, it will make conky crash\n\
Ctrl-z undo\nCtrl-d duplicate line\nwhite=text\n\
grey=commands and dollar signs are red, marks the start\n\
of a new command. All other colors are visual commands.\n\
\nIf something doesn't work right, or you don't understan\n\
how something works, you can report an issue on the github\n\
link or the facebook page. Suggestions are more than \n\
welcome""", text_size=tooltip_size)

        # com_list_box is located under the radio buttons, it shows the output of the users search, if the user
        # presses ctrl-enter or control-left_click it will insert the command into the file at the point of the
        # cursors location, unless it needs options, in which case it opens a dialogue box.

        uc.com_list_box =Text(uc.frame, height=10, width=20, bg="lightblue", font= ('Deja Vu Serif', 10))
        uc.com_list_box.grid_configure(row=5, column=0, columnspan=5, sticky="NSEW")
        uc.clb_tt = tt(uc.com_list_box, "click to highlight command,\ninsert to file by pressing\nctrl-leftClick or Ctrl-Enter", text_size=tooltip_size)

        uc.lnText = Text(uc.frame, width = 4, padx = 4, highlightthickness = 0, takefocus = 0,
                bd = 0, background = 'lightgrey', foreground = 'magenta', state='disabled')

        # file_display is the window that shows the current file . . . the bindings for all these widgets are listed
        # at the bottom of this function.

        uc.file_display =Text(uc.frame, wrap = 'word', undo=True, height=80)
        uc.file_display.grid_configure(row=1, column=10, columnspan=11, rowspan=20, sticky="NSEW")
        uc.file_display.config(bg='black', fg="white", insertbackground = 'cyan', font= ('Deja Vu Serif', 10))

        # wiki_window shows the definition of the highlighted command, these definitions are stored as .txt
        # files in the languages/* directory, I set it up like this because if the program is ever translated
        # to other languages it would be easy enough to add them one at a time to alternative folders.

        uc.wiki_label =Label(uc.frame, width=40, bg=cs.bgc, text=gn.lbl_description)
        uc.wiki_label.grid_configure(row=6, column=0, columnspan=10)
        uc.wl_tt = tt(uc.wiki_label, "definitions and examples of all the commands", text_size=tooltip_size)

        uc.wiki_window =Text(uc.frame, wrap='word', width=20, bg = "lightyellow", font= ('Deja Vu Serif', 10))
        uc.wiki_window.grid_configure(row=7, column=0, rowspan=14, columnspan=10, sticky="NSEW")

        # the color_button opens the color manager window . . . "add_color_window"

        color_img = ImageTk.PhotoImage(Image.open (cs.image_path+"colors.png"))
        uc.color_button =Button(uc.frame, image=color_img, command=uc.add_color_window)
        uc.color_button.grid_configure(row=21, column=10, sticky="NESW")
        uc.color_button.image=color_img
        uc.cb_tt = tt(uc.color_button, "Open Color Manager", text_size=tooltip_size)

        # the fonts_button opens the font manager window "font_window_fun"

        fonts_img = ImageTk.PhotoImage(Image.open (cs.image_path+"fonts.png"))
        uc.fonts_button =Button(uc.frame, image=fonts_img, command=lambda: uc.font_window_fun(uc.file_display))
        uc.fonts_button.grid_configure(row=21, column=11, sticky='NSEW')
        uc.fonts_button.image=fonts_img
        uc.fontButton_tt = tt(uc.fonts_button, "Choose Font and Size", text_size=tooltip_size)

        # the image_button opens the image dialogue. The image dialogue allows the user to open a file
        # dialog and select an image from the directory. When they do the dimensions of the image will
        # automatically be added to the dialog. This dialog needs a little improvement, but it works.

        image_img = ImageTk.PhotoImage(Image.open (cs.image_path+"images.png"))
        uc.image_button =Button(uc.frame, image=image_img, command =uc.image_window_fun)
        uc.image_button.grid_configure(row=21, column=12, sticky="NSEW")
        uc.image_button.image=image_img
        uc.Img_button_tt = tt(uc.image_button, "Add Image", text_size=tooltip_size)

        # page_borders is a button that allows the user to toggle the page borders on the active conky window

        page_borders_img = ImageTk.PhotoImage(Image.open (cs.image_path+"tog_page_border.png"))
        uc.page_borders =Button(uc.frame, image=page_borders_img, command=lambda: toggle_pb(uc, uc.file_display, uc.custom_window))
        uc.page_borders.grid_configure(row=21, column=13)
        uc.page_borders.image=page_borders_img

        # graph_borders allows the user to toggle the border around graphs to make it easier to place them.

        graph_borders_img = ImageTk.PhotoImage(Image.open (cs.image_path+"tog_graph_border.png"))
        uc.graph_borders =Button(uc.frame, image=graph_borders_img, command=lambda: toggle_gb(uc, uc.file_display, uc.custom_window))
        uc.graph_borders.grid_configure(row=21, column=14, sticky="NSEW")
        uc.graph_borders.image=graph_borders_img

        # pagyify button allows users to trigger the function "conky_by_line", which is a dialogue bocks
        # that takes a single line of conky code and returns it in the form of a list to make it easier to
        # read. You can add fonts, colors, commands, directly to this dialogue, it works . . .and is probably
        # my favorite part of this project so far.

        pagify_img = ImageTk.PhotoImage(Image.open (cs.image_path+"pagify.png"))
        uc.pagify =Button(uc.frame, image=pagify_img, command=lambda: uc.conky_by_line(self))
        uc.pagify.grid_configure(row=21, column=15, sticky="NSEW")
        uc.pagify.image=pagify_img
        uc.pagify_tt = tt(uc.pagify, "View and edit current\nline in a new window\nas a list.", text_size=tooltip_size)

        # themes_button allows a really aweful dialog to be opened that allows users to save their file as a theme, it works
        # but it needs some adjustment so users can understand what they are looking at.

        themes_img = ImageTk.PhotoImage(Image.open (cs.image_path+"themes.png"))
        uc.themes_button =Button(uc.frame, image=themes_img, command=uc.themes_window)
        uc.themes_button.grid_configure(row=21, column=16, sticky='NSEW')
        uc.themes_button.image=themes_img
        uc.cb_tt = tt(uc.themes_button, "Load and save themes\nwill be adding standard\ndialogue box soon.", text_size=tooltip_size)

        # custom_window is the name I gave to the area where the custom colors can be accessed by the user, if the user
        # presses ctrl-shift-enter (thinking about changing it to alt-enter) the color will be added to the file at the cursor
        # location.

        uc.custom = Label(uc.frame, width=20, bg=cs.bgc, text="Colors In File")
        uc.custom.grid_configure(row=0, column=5, columnspan=5)
        # adjust font size to fill window . . .
        uc.custom_window = Text(uc.frame, height=10, width=20, wrap="word", bg="darkgrey", fg="cyan", font=("times", "14", "normal"))
        uc.custom_window.grid_configure(row=1, column=5, columnspan=5, rowspan=5, sticky="NWSE")

        # save button

        uc.save_button =Button(uc.frame, text=gn.btn_save, fg='red', command=lambda: save_file(uc, uc.file_display, uc.custom_window))
        uc.save_button.grid_configure(row=21, column=19, sticky='NSEW')
        uc.save_tt = tt(uc.save_button, "Saves config file.\nsave theme when you\nare at a good save point.", text_size=tooltip_size)

        # quit button

        uc.quit =Button(uc.frame,text=gn.btn_quit, fg="red", command=self.root.destroy)
        uc.quit.grid_configure(row=21, column=20, sticky='NSEW')

        def command_line(self):
            """locate command in dictionary and enter
            into file_display, or open options window"""
            if cs.hold_command != '':
                if cs.selected == "commands":
                    the_input = cs.hold_command
                    functions[the_input](uc.file_display)           
            return "break"

        # the following are a list of commands imported from ct_mod for the purpose
        # of binding them to buttons and commands.

        def ps_command(self):
            """tie into add_custom, which adds custom
            color or font to file"""
            add_custom(uc.custom_window, uc.file_display, x=1)
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
        def clear_tag(self):
            uc.com_list_box.tag_remove("command", 0.0, END)
        def tab(self):
            uc.file_display.insert(INSERT, "    ")
            return "break"
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
            save_file(uc, uc.file_display, uc.custom_window)
        def launch_conky(self):
            subprocess.call('conky &',shell="true")
        def delete_cl(self):
            if cs.cl_toggle == 1:
                uc.command_find.delete(0, END)
                cs.cl_toggle = 0

        # binds for the main gui

        uc.com_list_box.tag_config("command", background="white")
        uc.com_list_box.bind('<KeyRelease-Down>', lambda event, a=uc.com_list_box,b=uc.wiki_window: show_def(a, b))
        uc.com_list_box.bind('<Down>', clear_tag)
        uc.com_list_box.bind('<KeyRelease-Up>', lambda event, a=uc.com_list_box,b=uc.wiki_window: show_def(a, b))
        uc.com_list_box.bind('<Up>', clear_tag)
        uc.com_list_box.bind('<Control-Return>', command_line)
        uc.com_list_box.bind('<Button-1>', clear_tag)
        uc.com_list_box.bind('<ButtonRelease-1>', lambda event, a=uc.com_list_box,b=uc.wiki_window: show_def(a, b))
        uc.com_list_box.bind('<Control-h>', command_box_help)
        uc.file_display.bind('<Alt-p>', uc.conky_by_line)
        uc.file_display.bind("<Tab>", tab)
        uc.file_display.bind('<Control-Return>', command_line)
        uc.file_display.bind('<Control-ButtonRelease-1>', command_line)
        uc.file_display.bind('<Shift-Control-Return>', ps_command)
        uc.file_display.bind('<Shift-Control-ButtonRelease-1>', ps_command)
        uc.file_display.bind('<Control-d>', dup_down)
        uc.file_display.bind('<Control-s>', save_kc)
        uc.wiki_window.bind('<Control-Return>', lambda event, a=self, b=uc.wiki_window, c=uc.file_display: Commands.force_file(a, b, c))
        uc.wiki_window.bind('<Control-Button-1>', lambda event, a=self, b=uc.wiki_window, c=uc.file_display: Commands.force_file(a, b, c))
        uc.wiki_window.bind('<Control-h>', definitions_help)
        uc.command_find.bind('<ButtonRelease-1>', delete_cl)
        uc.command_find.bind('<KeyRelease>', search_com)
        uc.command_find.bind('<Control-h>', search_help)
        uc.custom_window.bind('<Shift-Control-Return>', ps_command)
        uc.custom_window.bind('<ButtonRelease-1>', lambda event, a=uc.custom_window: load_hold_color(a))
        uc.custom_window.bind('<KeyRelease-Up>', lambda event, a=uc.custom_window: load_hold_color(a))
        uc.custom_window.bind('<KeyRelease-Down>', lambda event, a=uc.custom_window: load_hold_color(a))
        uc.custom_window.bind('<Control-h>', custom_help)
        uc.file_display.bind("<Control-l>", launch_conky)
        uc.file_display.bind("<Control-h>", file_display_help)

        # open current conky.conf file in the file_display widget

        open_file(uc, uc.file_display, uc.custom_window)
        uc.command_find.insert(INSERT, "Search commands . . .")

    # conky by line is a stand alone window dialog that allws the user to grab a line
    # of code from the conky.conf file, and open it as a list in a new dialog box. The
    # line can be edited, and re-entered into the main file_display, just like it was 
    # being edited in the main file itself.

    def conky_by_line(self, foo):
        """dialog window for the "conky_by_line" function"""
        uc.cbl_window = Tk()
        uc.cbl_window.grid()
        uc.cbl_window.attributes("-topmost", 'true')
        uc.cbl_window.title("Conky by line")

        # main display window

        uc.cbl_text =Text(uc.cbl_window, width=40, height = 30)
        uc.cbl_text.grid_configure(row=0, column=0, columnspan=5)
        uc.cbl_text.config(bg="black", fg="white", insertbackground = 'cyan', font= ('Deja Vu Serif', 10))

        def cbl_command_custom(self):
            """add_custom to conky by line window"""
            add_custom(uc.custom_window, uc.cbl_text, x=0)
        def cbl_command_enter(self):
            if cs.selected == "commands":
                the_input = cs.hold_command
                functions[the_input](uc.cbl_text)
            return "break"

        # load information in the C.B.L. window

        load_by_line(uc.com_list_box, uc.custom_window, uc.file_display)
        insert_line(uc.cbl_text)

        # add syntax highlighting to window

        syntax_basic(uc.cbl_text)
        fd_syntax_highlighting(uc.cbl_text)

        # replaces the line in the main file, with the line generated in C.B.L

        uc.cbl_enter = Button(uc.cbl_window, text="Update", command=lambda: cbl_update(uc, uc.cbl_text, uc.com_list_box, uc.custom_window, uc.file_display))
        uc.cbl_enter.grid_configure(row=2, column=4, sticky="NSEW")

        #  opens font_dialog from C.B.L.

        uc.cbl_font =Button(uc.cbl_window, text="fonts", command = lambda: uc.font_window_fun(uc.cbl_text))
        uc.cbl_font.grid_configure(row=2, column=1, sticky="NWES")

        uc.cbl_exit =Button(uc.cbl_window, text="Exit", command=uc.cbl_window.destroy)
        uc.cbl_exit.grid_configure(row=2, column=0, sticky="NSEW")
        
        uc.cbl_text.bind("<Control-Return>", cbl_command_enter)
        uc.cbl_text.bind("<Control-Button-1>", cbl_command_enter)
        uc.cbl_text.bind("<Shift-Control-Return>", cbl_command_custom)
        uc.cbl_text.bind("<Shift-Control-Button-1>", cbl_command_custom)

        uc.cbl_window.after(5000, lambda: uc.cbl_window.focus_force())

    def font_window_fun(self, file_display):
        """create font properties window"""
        uc.font_window = Tk()
        uc.font_window.grid()
        uc.font_window.title(str(len(cs.font_list))+" "+gn.win_fonts)
        uc.font_window.attributes("-topmost", True)

        cs.toggle=0

        # searches for the font typed by the user in the font_search_bar

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
        font_search_bar.bind("<Button-1>", clear_entry) # clears search bar when user clicks in it
        font_search_bar.bind("<KeyPress>", font_search) # searches for fonts after every key pressed
        fsb_tt = tt(font_search_bar, "search fonts here", text_size=12)

        # "Font Name:" label

        font_label = Label(uc.font_window, bg=cs.bgc, text=gn.lbl_font_name)
        font_label.grid_configure(row=16, columnspan=1, sticky="NSW")
        font_label_tt = tt(font_label, "selected font will  be displayed below the dialog box, if you enter a font size it will give the example at that font size", text_size=12)

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

        # font_submit inserts font in file_display or C.B.L at cursor location

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
        uc.color_manager_window.attributes("-topmost", False)
        uc.color_manager_window.config(bg="#000000")
        file_colors = uc.custom_window.get(0.0, "end-1c").splitlines()

        # tts is the size of the text in the tool tips

        tts = 12

        # chooser opens that rows color chooser, entry displays the color hex code, button is a lie,
        # they were buttons at one point but now they just display the current color of a color alias,
        # if the color on the color chooser button and the label are differrent, then the user will
        # know the colors haven't been updated to the file yet. This covers the next 105 lines lol

        uc.sel_col_label = Label(uc.color_manager_window, width=10, text="Select Color")
        uc.sel_col_label.grid_configure(row=0, column=0)
        uc.sel_col_tt = tt(uc.sel_col_label, "Opens a color chooser", text_size=tts)

        uc.current_color_label = Label(uc.color_manager_window, width=10, text="Current Color")
        uc.current_color_label.grid_configure(row=0, column=2)
        uc.sel_col_tt = tt(uc.current_color_label, "color currently in the file", text_size=tts)            

        uc.default_color_chooser = Button(uc.color_manager_window, text="default", command=lambda: color_chooser(uc.default_color_entry, uc.default_color_chooser))
        uc.default_color_chooser.grid_configure(row=1, column=0, sticky="NSEW")

        uc.default_color_entry =Entry(uc.color_manager_window, width=10)
        uc.default_color_entry.grid_configure(sticky="NSEW", row=1, column=1)    

        uc.default_color_button = Label(uc.color_manager_window, width=10)
        uc.default_color_button.grid_configure(sticky="NSEW", row=1, column=2)
        
        uc.color0_chooser = Button(uc.color_manager_window, text="color0", command=lambda: color_chooser(uc.color0_entry, uc.color0_chooser))
        uc.color0_chooser.grid_configure(row=2, column=0, sticky="NSEW")

        uc.color0_entry = Entry(uc.color_manager_window, width=10)
        uc.color0_entry.grid_configure(sticky="NSEW", row=2, column=1)

        uc.color0_button = Label(uc.color_manager_window, width=10)
        uc.color0_button.grid_configure(sticky="NSEW", row=2, column=2)
    
        uc.color1_chooser = Button(uc.color_manager_window, text="color1", command=lambda: color_chooser(uc.color1_entry, uc.color1_chooser))
        uc.color1_chooser.grid_configure(row=3, column=0, sticky="NSEW")

        uc.color1_entry = Entry(uc.color_manager_window, width=10)
        uc.color1_entry.grid_configure(sticky="NSEW", row=3, column=1)

        uc.color1_button = Label(uc.color_manager_window, width=10)
        uc.color1_button.grid_configure(sticky="NSEW", row=3, column=2)
    
        uc.color2_chooser = Button(uc.color_manager_window, text="color2", command=lambda: color_chooser(uc.color2_entry, uc.color2_chooser))
        uc.color2_chooser.grid_configure(row=4, column=0, sticky="NSEW")

        uc.color2_entry = Entry(uc.color_manager_window, width=10)
        uc.color2_entry.grid_configure(sticky="NSEW", row=4, column=1)

        uc.color2_button = Label(uc.color_manager_window, width=10)
        uc.color2_button.grid_configure(sticky="NSEW", row=4, column=2)
    
        uc.color3_chooser = Button(uc.color_manager_window, text="color3", command=lambda: color_chooser(uc.color3_entry, uc.color3_chooser))
        uc.color3_chooser.grid_configure(row=5, column=0, sticky="NSEW")

        uc.color3_entry = Entry(uc.color_manager_window, width=10)
        uc.color3_entry.grid_configure(sticky="NSEW", row=5, column=1)

        uc.color3_button = Label(uc.color_manager_window, width=10)
        uc.color3_button.grid_configure(sticky="NSEW", row=5, column=2)
    
        uc.color4_chooser = Button(uc.color_manager_window, text="color4", command=lambda: color_chooser(uc.color4_entry, uc.color4_chooser))
        uc.color4_chooser.grid_configure(row=6, column=0, sticky="NSEW")

        uc.color4_entry = Entry(uc.color_manager_window, width=10)
        uc.color4_entry.grid_configure(sticky="NSEW", row=6, column=1)

        uc.color4_button = Label(uc.color_manager_window, width=10)
        uc.color4_button.grid_configure(sticky="NSEW", row=6, column=2)
        
        uc.color5_chooser = Button(uc.color_manager_window, text="color5", command=lambda: color_chooser(uc.color5_entry, uc.color5_chooser))
        uc.color5_chooser.grid_configure(row=7, column=0, sticky="NSEW")

        uc.color5_entry = Entry(uc.color_manager_window, width=10)
        uc.color5_entry.grid_configure(sticky="NSEW", row=7, column=1)

        uc.color5_button = Label(uc.color_manager_window, width=10)
        uc.color5_button.grid_configure(sticky="NSEW", row=7, column=2)
        
        uc.color6_chooser = Button(uc.color_manager_window, text="color6", command=lambda: color_chooser(uc.color6_entry, uc.color6_chooser))
        uc.color6_chooser.grid_configure(row=8, column=0, sticky="NSEW")

        uc.color6_entry = Entry(uc.color_manager_window, width=10)
        uc.color6_entry.grid_configure(sticky="NSEW", row=8, column=1)

        uc.color6_button = Label(uc.color_manager_window, width=10)
        uc.color6_button.grid_configure(sticky="NSEW", row=8, column=2)
        
        uc.color7_chooser = Button(uc.color_manager_window, text="color7", command=lambda: color_chooser(uc.color7_entry, uc.color7_chooser))
        uc.color7_chooser.grid_configure(row=9, column=0, sticky="NSEW")

        uc.color7_entry = Entry(uc.color_manager_window, width=10)
        uc.color7_entry.grid_configure(sticky="NSEW", row=9, column=1)

        uc.color7_button = Label(uc.color_manager_window, width=10)
        uc.color7_button.grid_configure(sticky="NSEW", row=9, column=2)
        
        uc.color8_chooser = Button(uc.color_manager_window, text="color8", command=lambda: color_chooser(uc.color8_entry, uc.color8_chooser))
        uc.color8_chooser.grid_configure(row=10, column=0, sticky="NSEW")

        uc.color8_entry = Entry(uc.color_manager_window, width=10)
        uc.color8_entry.grid_configure(sticky="NSEW", row=10, column=1)

        uc.color8_button = Label(uc.color_manager_window, width=10)
        uc.color8_button.grid_configure(sticky="NSEW", row=10, column=2)
        
        uc.color9_chooser = Button(uc.color_manager_window, text="color9", command=lambda: color_chooser(uc.color9_entry, uc.color9_chooser))
        uc.color9_chooser.grid_configure(row=11, column=0, sticky="NSEW")

        uc.color9_entry = Entry(uc.color_manager_window, width=10)
        uc.color9_entry.grid_configure(sticky="NSEW", row=11, column=1)

        uc.color9_button = Label(uc.color_manager_window, width=10)
        uc.color9_button.grid_configure(sticky="NSEW", row=11, column=2)

        # after the user chooses their colors, the update_all_button will gather the info from the dialog boxes
        # and add it to the file, and save :).
            
        uc.update_all_button = Button(uc.color_manager_window, text="update-all", command=lambda: update_colors(uc))
        uc.update_all_button.grid_configure(row=12, columnspan=3, sticky="NSEW")
        up_all_tt = tt(uc.update_all_button, "Save new colors to file\nand update 'colors in use'.", text_size=tts)

        # import dialog is a place for the user to add a list of colors in multiple formats and when they push the
        # import_dialog_button, the colors will be loaded into the entry widgets listed above, allowing for quick
        # theme changes

        uc.import_dialog = Text(uc.color_manager_window, width=1, height=10, bg='black', foreground='cyan')
        uc.import_dialog.grid_configure(row=13, column=0, columnspan=3, sticky="NSEW")
        uc.imp_d_tt = tt(uc.import_dialog, "paste list of colors here", text_size=tts)

        uc.import_dialog_button = Button(uc.color_manager_window, text="Import Colors", command=lambda: open_color_dialog(uc))
        uc.import_dialog_button.grid_configure(row=14, column=0, columnspan=3, sticky="NSEW")
        uc.idb_tt = tt(uc.import_dialog_button, "Import from Dialog ^", text_size=tts)

        # does the same thing as above, but instead of pasting a list into a dialog box, they can open it from a file
        # I will be setting this up to automatically add color files to the user directory so they can access it later.

        uc.import_button = Button(uc.color_manager_window, text="Import Color File", command=lambda: open_color_file(uc))
        uc.import_button.grid_configure(row=15, columnspan=3, sticky="NSEW")
        uc.imp_but_tt = tt(uc.import_button, "import list of colors from file", text_size=tts)

        # update_gui changes the gui color to match the file colors

        update_gui(uc, file_colors)

        uc.color_manager_window.mainloop()

    # help_window is being replaced by tool tips.

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

    # image_window_fun is the function to spawn the "add image" dialog

    def image_window_fun(self):
        """create image command window"""

        def open_file():
            """spawns a file dialogue and loads file to image_window_fun"""
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
            """gets the dimensions of the image and
            loads them appropriately"""
            image_dimensions(image_entry, size_x, size_y)
            align_image_x.insert(INSERT, '0')
            align_image_y.insert(INSERT, '0')
        
        ts=12
        uc.image_window = Tk()
        uc.image_window.title(gn.win_image)
        uc.image_window.grid()
        uc.image_window.config(bg="white")
        uc.image_window.attributes("-topmost", True)

        # shows path to image, allows user to add their own path

        image_path_label =Label(uc.image_window, bg=cs.bgc, text="Image Path:")
        image_path_label.grid_configure(row=0, column=0, columnspan=3, sticky="NSEW")
        img_path_tt = tt(image_path_label, "Add image to conky,\nif you need to adjust size\nor place you can\n\
hit enter again. No need\nto delete manually", text_size=ts)

        image_dialogue = Button(uc.image_window, width=15, fg="#ffffff", bg="#000000", command= open_file, text="Select Image")
        image_dialogue.grid_configure(row=1, column=0, columnspan=3, sticky="NSEW")

        empty_label = Label(uc.image_window, bg="black",fg="white")
        empty_label.grid_configure(row=2, column=0, sticky="NSEW")

        x_label = Label(uc.image_window, bg="black", fg="white", text="x")
        x_label.grid_configure(row=2, column=1, sticky="NSEW")
        aix_tt = tt(x_label, "horizontal", text_size=ts)

        y_label = Label(uc.image_window, bg="black", fg="white", text="y")
        y_label.grid_configure(row=2, column=2, sticky="NSEW")
        aiy_tt = tt(y_label, "vertical", text_size=ts)

        size_label =Label(uc.image_window, bg=cs.bgc, text=gn.lbl_size, justify="left", width=20)
        size_label.grid_configure(row=3, column=0, columnspan=1, sticky="NSEW")
        sl_tt = tt(size_label, "Once you load the image\nthe dimensions will\nbe added. If you\nchange the size\n\
of either x or y\nand press enter\nthe value of the\nother will change\nto maintain x:y ratio.")

        size_x =Entry(uc.image_window, width=5)
        size_x.grid_configure(row=3, column=1, sticky='NSE')

        size_y =Entry(uc.image_window, width=5)
        size_y.grid_configure(row=3, column=2, sticky='NSW')


        im_align =Label(uc.image_window, bg=cs.bgc, text=gn.lbl_align, justify="left")
        im_align.grid_configure(row=4, column=0, columnspan=1, sticky="NSEW")
        im_al_tt = tt(im_align, "default value 0 0 will put\nthe top left hand\ncorner of the image\nat the top left\nhand corner of the\nconky window", text_size=ts)

        align_image_x =Entry(uc.image_window, width=5)
        align_image_x.grid_configure(row=4, column=1, sticky='NSE')

        align_image_y =Entry(uc.image_window, width=5)
        align_image_y.grid_configure(row=4, column=2, sticky='NSW')

        image_entry = Entry(uc.image_window)
        image_entry.grid_configure(row=5, columnspan=3, sticky="NSEW")

        enter_button =Button(uc.image_window, text=gn.btn_enter)
        enter_button.grid_configure(row=6, column=0, sticky="W")

        exit_button =Button(uc.image_window, text=gn.btn_exit, command=uc.image_window.destroy)
        exit_button.grid_configure(row=6, column=2, sticky="E")

        enter_button.config(command=lambda: add_image(uc, image_entry, size_x, size_y, align_image_x, align_image_y, uc.file_display, uc.custom_window))

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

    def themes_window(self):
        """create themes properties window"""

        uc.window = Tk()
        uc.window.grid()
        uc.window.title(gn.win_themes)
        uc.window.attributes("-topmost", True)

        theme_name =Label(uc.window, bg=cs.bgc, text=gn.lbl_theme_name)
        theme_name.grid_configure(row=0, column=0, columnspan=1)
        theme_name_tt = tt(theme_name, "load themes here, will be replacing with a standard dialog box soon", waittime=100, wraplength=250, text_size=12)

        theme_display =Entry(uc.window)
        theme_display.grid_configure(row=0, column=1, columnspan=1, sticky="NSEW")

        save_theme_button =Button(uc.window, text=gn.btn_save_theme, command=lambda: theme_prompt(theme_display, uc.file_display))
        save_theme_button.grid_configure(row=0, column=2, columnspan=1, sticky="NSEW")
        save_theme_tt = tt(save_theme_button, "save current config to theme, if you type an existing theme name it will overwrite it")

        open_theme_label =Label(uc.window, text=gn.lbl_open_theme)
        open_theme_label.grid_configure(row=1, column=0, sticky='NSEW')

        theme_list = read_theme_list()
        option_header =StringVar(uc.window)
        option_header.set(theme_list[0])

        themes_list =OptionMenu(uc.window, option_header, *theme_list)
        themes_list.grid_configure(row=1, column=1, columnspan=1, sticky="NSEW")
        themes_list_tt = tt(themes_list, "select name of theme you want to load", text_size=12)

        theme_button =Button(uc.window, text=gn.btn_load_theme)
        theme_button.grid_configure(row=1, column=2, columnspan=1, sticky="NSEW")
        theme_button.config(command=lambda: get_theme(uc, uc.file_display, option_header, uc.custom_window))
        theme_button_tt = tt(theme_button, "load selected theme", text_size=12)
        uc.window.mainloop()

    def run(self):
        self.root.mainloop()

uc = Utilize_Conky(gn.win_main)
com = Utilize_Conky
uc.create_widgets(gn.editor)
load_commands(uc.com_list_box)
syntax_basic(uc.file_display)
fd_syntax_highlighting(uc.file_display)
load_the_colors(uc, "file")
cb_syntax(uc.custom_window)
font_list()
theme_list()

uc.run()