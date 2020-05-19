from common_stuff import Common_Stuff as cs

class gui_names:
	"""class to tie specific languages widget
	names to the GUI. Look for gui_names.txt to change
	the names of the different elements in language
	folder. If you want to translate the language,
	copy the english, change name to desired language
	and make adjustments from there."""

	open_file = open(cs.gui_names)
	name = open_file.read().splitlines()
	open_file.close()

	# window titles
	win_main = name[0]
	win_colors = name[1]
	win_fonts = name[2]
	win_image = name[3]
	win_themes = name[4]
	# radio buttons, upper left corner
	rb_commands = name[5]
	rb_configs = name[6]
	rb_lua = name[7]
	rb_options = name[8]
	# labels lbl
	lbl_search = name[9]
	lbl_custom = name[10]
	lbl_description = name[11]
	# buttons
	btn_colors = name[12]
	btn_fonts = name[13]
	btn_img = name[14]
	btn_themes = name[15]
	btn_save = name[16]
	btn_quit = name[17]
	# help window titles
	help_editor = name[18]
	help_desription = name[19]
	help_commands = name[20]
	help_custom = name[21]
	help_search = name[22]
	# tab names
	editor = name[23]
	# popup windows
	btn_exit = name[24]
	btn_enter = name[25]
	lbl_size = name[26]
	lbl_align = name[27]
	btn_update = name[28]
	lbl_theme_name = name[29]
	btn_save_theme = name[30]
	lbl_open_theme = name[31]
	btn_load_theme = name[32]
	lbl_font_name = name[33]
	win_ins = name[34]
	how_to = name[35]