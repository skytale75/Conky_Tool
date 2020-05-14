from tkinter import *
import tkinter as tk
from os import listdir, path
from pathlib import Path
from common_stuff import Common_Stuff as cs

# setup dictionary function . . . functions = {"functon_name:" function}
# call dictionary function . . . functions["function_name"]()

class Commands:


    def __init__(self, com_name, com_des, unique_command):
        self.com_name = com_name
        self.com_des = com_des
        self.unique_command = unique_command

    def force_file(self, ww, file_display):
        get_name = ww.get(0.0, END)
        file_name = get_name.split()[0]
        file_open = open(cs.coms_path+file_name+".txt", 'r')
        fo_read = file_open.read()
        fo_sl = fo_read.splitlines()
        cn = str(fo_sl[0])
        file_open.close()
        generic(file_name, cn, fo_read, file_display)

    def command(self, file_display):
        """translate command name to command and insert
        unless command has custom command 'unique_command'"""
        if self.unique_command == "false":
            com_out = "${"+self.com_name+"}"
            file_display.insert(INSERT, com_out)
            active_highlighting(file_display, com_out)
        if self.unique_command == "true":
            file_open = open(cs.coms_path+self.com_name.lower()+".txt", 'r')
            fo_read = file_open.read()
            fo_sl = fo_read.splitlines()
            cn = str(fo_sl[0])
            file_open.close()

            generic(self.com_name, cn, fo_read, file_display)
        if self.unique_command != "true" and self.unique_command != "false":
            eval(self.unique_command)

    def command_out(self, cl_output):
        """puts conky command names in appropriate format"""
        cl_output.insert(INSERT, self.com_name+"\n")

    def definition_out(self, cd_output):
        cd_output.delete(0.0, END)
        cd_output.insert(INSERT, self.com_des)


def def_file(my_input):
    """open definition file and return as a string"""
    open_file = open(cs.coms_path+my_input+".txt")
    read_file = open_file.read()
    open_file.close()
    return str(read_file)

def generic(window_title, command_name, definition_name, file_display):
    window = Tk()
    window.grid()
    window.title(window_title)
    window.config(bg='white')
    window.wait_visibility(window)
    window.attributes("-topmost", True)
    com_label = tk.Label(window, text=command_name)
    com_label.grid_configure(row=0, column=0, sticky="W")

    com_entry = tk.Entry(window, bg="lightblue")
    com_entry.grid_configure(row=1, column=0, columnspan=4, sticky="NESW")
    com_entry.insert(INSERT, command_name)

    def enter_button():
        get_contents = com_entry.get()
        output_to_file = "${"+get_contents+"}"
        file_display.insert(INSERT, output_to_file)

    com_button = tk.Button(window, text="Enter", command=enter_button)
    com_button.grid_configure(row=1, column=4, sticky="NESW")

    def_text = tk.Text(window, width=100, height=20, wrap='word')
    def_text.grid_configure(row=2, column=0, columnspan=5)
    def_text.insert(INSERT, definition_name)


    def save_file(def_text):
        new_file = def_text.get(0.0, "end-1c")
        file_open = open(cs.coms_path+window_title+".txt", 'w')
        file_open.write(new_file)
        file_open.close()

    def_sc = tk.Button(window, text="Save Changes", command=lambda: save_file(def_text))
    def_sc.grid_configure(row=3, column=0, sticky="NESW")

    def_exit = tk.Button(window, text='Exit', command=window.destroy)
    def_exit.grid_configure(row=3, column=4, sticky="NESW")


    window.mainloop()

def active_highlighting(widget_name, tag_command):
    """syntax highlighting for new command"""
    widget_name.tag_config("active", background='purple', foreground='white')
    word_length = len(tag_command)
    pos_start = (f"insert-{word_length}c")
    print(pos_start)
    widget_name.tag_add("active", pos_start, INSERT)
    

cm = Commands
# complete list of conky commands for text section
# definitions are in file in coms folder, def_file() opens and returns them as a string.

acpiacadapter = Commands('acpiacadapter', def_file('acpiacadapter'), 'false')
functions = {"acpiacadapter": acpiacadapter}

Eval = Commands('eval', def_file('eval'), "true")
functions.update({'eval': Eval.command})

Exec = Commands('exec', def_file('exec'), 'true')
functions.update({'exec': Exec.command})

acpifan = Commands('acpifan', def_file('acpifan'), 'false')
functions.update({'acpifan': acpifan.command})

acpitemp = Commands('acpitemp', def_file('acpitemp'), 'false')
functions.update({'acpitemp': acpitemp.command})

addr = Commands('addr', def_file('addr'), 'false')
functions.update({'addr': addr.command})

addrs = Commands('addrs', def_file('addrs'), 'false')
functions.update({'addrs': addrs.command})

adt746xfan = Commands('adt746xfan', def_file('adt746xfan'), 'false')
functions.update({'adt746xfan': adt746xfan.command})

adt746xpcu = Commands('adt746xpcu', def_file('adt746xpcu'), 'false')
functions.update({'adt746xpcu': adt746xpcu.command})

alignc = Commands('alignc', def_file('alignc'), 'false')
functions.update({'alignc': alignc.command})

alignr = Commands('alignr', def_file('alignr'), 'false')
functions.update({'alignr': alignr.command})

apcupsd = Commands('apcupsd', def_file('apcupsd'), 'false')
functions.update({'apcupsd': apcupsd.command})

apcupsd_cable = Commands('apcupsd_cable', def_file('apcupsd_cable'), 'false')
functions.update({'apcupsd_cable': apcupsd_cable.command})

apcupsd_charge = Commands('apcupsd_charge', def_file('apcupsd_charge'), 'false')
functions.update({'apcupsd_charge': apcupsd_charge.command})

apcupsd_lastxfer = Commands('apcupsd_lastxfer', def_file('apcupsd_lastxfer'), 'false')
functions.update({'apcupsd_lastxfer': apcupsd_lastxfer.command})

apcupsd_linev = Commands('apcupsd_linev', def_file('apcupsd_linev'), 'false')
functions.update({'apcupsd_linev': apcupsd_linev.command})

apcupsd_load = Commands('apcupsd_load', def_file('apcupsd_load'), 'false')
functions.update({'apcupsd_load': apcupsd_load.command})

apcupsd_loadbar = Commands('apcupsd_loadbar', def_file('apcupsd_loadbar'), 'false')
functions.update({'apcupsd_loadbar': apcupsd_loadbar.command})

apcupsd_loadgauge = Commands('apcupsd_loadgauge', def_file('apcupsd_loadgauge'), 'false')
functions.update({'apcupsd_loadgauge': apcupsd_loadgauge.command})

apcupsd_loadgraph = Commands('apcupsd_loadgraph', def_file('apcupsd_loadgraph'), 'false')
functions.update({'apcupsd_loadgraph': apcupsd_loadgraph.command})

apcupsd_model = Commands('apcupsd_model', def_file('apcupsd_model'), 'false')
functions.update({'apcupsd_model': apcupsd_model.command})

apcupsd_name = Commands('apcupsd_name', def_file('apcupsd_name'), 'false')
functions.update({'apcupsd_name': apcupsd_name.command})

apcupsd_status = Commands('apcupsd_status', def_file('apcupsd_status'), 'false')
functions.update({'apcupsd_status': apcupsd_status.command})

apcupsd_temp = Commands('apcupsd_temp', def_file('apcupsd_temp'), 'false')
functions.update({'apcupsd_temp': apcupsd_temp.command})

apcupsd_timeleft = Commands('apcupsd_timeleft', def_file('apcupsd_timeleft'), 'false')
functions.update({'apcupsd_timeleft': apcupsd_timeleft.command})

apcupsd_upsmode = Commands('apcupsd_upsmode', def_file('apcupsd_upsmode'), 'false')
functions.update({'apcupsd_upsmode': apcupsd_upsmode.command})

apm_adapter = Commands('apm_adapter', def_file('apm_adapter'), 'false')
functions.update({'apm_adapter': apm_adapter.command})

apm_battery_life = Commands('apm_battery_life', def_file('apm_battery_life'), 'false')
functions.update({'apm_battery_life': apm_battery_life.command})

apm_battery_time = Commands('apm_battery_time', def_file('apm_battery_time'), 'false')
functions.update({'apm_battery_time': apm_battery_time.command})

audacious_bar = Commands('audacious_bar', def_file('audacious_bar'), 'true')
functions.update({'audacious_bar': audacious_bar.command})

audacious_bitrate = Commands('audacious_bitrate', def_file('audacious_bitrate'), 'false')
functions.update({'audacious_bitrate': audacious_bitrate.command})

audacious_channels = Commands('audacious_channels', def_file('audacious_channels'), 'false')
functions.update({'audacious_channels': audacious_channels.command})

audacious_filename = Commands('audacious_filename', def_file('audacious_filename'), 'false')
functions.update({'audacious_filename': audacious_filename.command})

audacious_frequency = Commands('audacious_frequency', def_file('audacious_frequency'), 'false')
functions.update({'audacious_frequency': audacious_frequency.command})

audacious_length = Commands('audacious_length', def_file('audacious_length'), 'false')
functions.update({'audacious_length': audacious_length.command})

audacious_length_seconds = Commands('audacious_length_seconds', def_file('audacious_length_seconds'), 'false')
functions.update({'audacious_length_seconds': audacious_length_seconds.command})

audacious_main_volume = Commands('audacious_main_volume', def_file('audacious_main_volume'), 'false')
functions.update({'audacious_main_volume': audacious_main_volume.command})

audacious_playlist_length = Commands('audacious_playlist_length', def_file('audacious_playlist_length'), 'false')
functions.update({'audacious_playlist_length': audacious_playlist_length.command})

audacious_playlist_position = Commands('audacious_playlist_position', def_file('audacious_playlist_position'), 'false')
functions.update({'audacious_playlist_position': audacious_playlist_position.command})

audacious_position = Commands('audacious_position', def_file('audacious_position'), 'false')
functions.update({'audacious_position': audacious_position.command})

audacious_position_seconds = Commands('audacious_position_seconds', def_file('audacious_position_seconds'), 'false')
functions.update({'audacious_position_seconds': audacious_position_seconds.command})

audacious_status = Commands('audacious_status', def_file('audacious_status'), 'false')
functions.update({'audacious_status': audacious_status.command})

audacious_title = Commands('audacious_title', def_file('audacious_title'), 'true')
functions.update({'audacious_title': audacious_title.command})

battery = Commands('battery', def_file('battery'), 'true')
functions.update({'battery': battery.command})

battery_bar = Commands('battery_bar', def_file('battery_bar'), 'true')
functions.update({'battery_bar': battery_bar.command})

battery_percent = Commands('battery_percent', def_file('battery_percent'), 'true')
functions.update({'battery_percent': battery_percent.command})

battery_short = Commands('battery_short', def_file('battery_short'), 'true')
functions.update({'battery_short': battery_short.command})

battery_status = Commands('battery_status', def_file('battery_status'), 'true')
functions.update({'battery_status': battery_status.command})

battery_time = Commands('battery_time', def_file('battery_time'), 'true')
functions.update({'battery_time': battery_time.command})

blink = Commands('blink', def_file('blink'), 'true')
functions.update({'blink': blink.command})

buffers = Commands('buffers', def_file('buffers'), 'false')
functions.update({'buffers': buffers.command})

cached = Commands('cached', def_file('cached'), 'false')
functions.update({'cached': cached.command})

cat = Commands('cat', def_file('cat'), 'true')
functions.update({'cat': cat.command})

catp = Commands('catp', def_file('catp'), 'true')
functions.update({'catp': catp.command})

cloud_cover = Commands('cloud_cover', def_file('cloud_cover'), 'false')
functions.update({'cloud_cover': cloud_cover.command})

cmdline_to_pid = Commands('cmdline_to_pid', def_file('cmdline_to_pid'), 'true')
functions.update({'cmdline_to_pid': cmdline_to_pid.command})

cmus_aaa = Commands('cmus_aaa', def_file('cmus_aaa'), 'false')
functions.update({'cmus_aaa': cmus_aaa.command})

cmus_album = Commands('cmus_album', def_file('cmus_album'), 'false')
functions.update({'cmus_album': cmus_album.command})

cmus_artist = Commands('cmus_artist', def_file('cmus_artist'), 'false')
functions.update({'cmus_artist': cmus_artist.command})

cmus_curtime = Commands('cmus_curtime', def_file('cmus_curtime'), 'false')
functions.update({'cmus_curtime': cmus_curtime.command})

cmus_date = Commands('cmus_date', def_file('cmus_date'), 'false')
functions.update({'cmus_date': cmus_date.command})

cmus_file = Commands('cmus_file', def_file('cmus_file'), 'false')
functions.update({'cmus_file': cmus_file.command})

cmus_genre = Commands('cmus_genre', def_file('cmus_genre'), 'false')
functions.update({'cmus_genre': cmus_genre.command})

cmus_percent = Commands('cmus_percent', def_file('cmus_percent'), 'false')
functions.update({'cmus_percent': cmus_percent.command})

cmus_progress = Commands('cmus_progress', def_file('cmus_progress'), 'true')
functions.update({'cmus_progress': cmus_progress.command})

cmus_random = Commands('cmus_random', def_file('cmus_random'), 'false')
functions.update({'cmus_random': cmus_random.command})

cmus_repeat = Commands('cmus_repeat', def_file('cmus_repeat'), 'false')
functions.update({'cmus_repeat': cmus_repeat.command})

cmus_state = Commands('cmus_state', def_file('cmus_state'), 'false')
functions.update({'cmus_state': cmus_state.command})

cmus_timeleft = Commands('cmus_timeleft', def_file('cmus_timeleft'), 'false')
functions.update({'cmus_timeleft': cmus_timeleft.command})

cmus_title = Commands('cmus_title', def_file('cmus_title'), 'false')
functions.update({'cmus_title': cmus_title.command})

cmus_totaltime = Commands('cmus_totaltime', def_file('cmus_totaltime'), 'false')
functions.update({'cmus_totaltime': cmus_totaltime.command})

cmus_track = Commands('cmus_track', def_file('cmus_track'), 'false')
functions.update({'cmus_track': cmus_track.command})

color = Commands('color', def_file('color'), 'true')
functions.update({'color': color.command})

colorN = Commands('colorN', def_file('colorN'), 'false')
functions.update({'colorN': colorN.command})

combine = Commands('combine', def_file('combine'), 'true')
functions.update({'combine': combine.command})

conky_build_arch = Commands('conky_build_arch', def_file('conky_build_arch'), 'false')
functions.update({'conky_build_arch': conky_build_arch.command})

conky_build_date = Commands('conky_build_date', def_file('conky_build_date'), 'false')
functions.update({'conky_build_date': conky_build_date.command})

conky_version = Commands('conky_version', def_file('conky_version'), 'false')
functions.update({'conky_version': conky_version.command})

cpu = Commands('cpu', def_file('cpu'), 'true')
functions.update({'cpu': cpu.command})

cpubar = Commands('cpubar', def_file('cpubar'), 'true')
functions.update({'cpubar': cpubar.command})

cpugauge = Commands('cpugauge', def_file('cpugauge'), 'true')
functions.update({'cpugauge': cpugauge.command})

cpugraph = Commands('cpugraph', def_file('cpugraph'), 'true')
functions.update({'cpugraph': cpugraph.command})

curl = Commands('curl', def_file('curl'), 'true')
functions.update({'curl': curl.command})

desktop = Commands('desktop', def_file('desktop'), 'false')
functions.update({'desktop': desktop.command})

desktop_name = Commands('desktop_name', def_file('desktop_name'), 'false')
functions.update({'desktop_name': desktop_name.command})

desktop_number = Commands('desktop_number', def_file('desktop_number'), 'false')
functions.update({'desktop_number': desktop_number.command})

disk_protect = Commands('disk_protect', def_file('disk_protect'), 'true')
functions.update({'disk_protect': disk_protect.command})

diskio = Commands('diskio', def_file('diskio'), 'true')
functions.update({'diskio': diskio.command})

diskio_read = Commands('diskio_read', def_file('diskio_read'), 'true')
functions.update({'diskio_read': diskio_read.command})

diskio_write = Commands('diskio_write', def_file('diskio_write'), 'true')
functions.update({'diskio_write': diskio_write.command})

diskiograph = Commands('diskiograph', def_file('diskiograph'), 'true')
functions.update({'diskiograph': diskiograph.command})

diskiograph_read = Commands('diskiograph_read', def_file('diskiograph_read'), 'true')
functions.update({'diskiograph_read': diskiograph_read.command})

diskiograph_write = Commands('diskiograph_write', def_file('diskiograph_write'), 'true')
functions.update({'diskiograph_write': diskiograph_write.command})

distribution = Commands('distribution', def_file('distribution'), 'false')
functions.update({'distribution': distribution.command})

downspeed = Commands('downspeed', def_file('downspeed'), 'true')
functions.update({'downspeed': downspeed.command})

downspeedf = Commands('downspeedf', def_file('downspeedf'), 'true')
functions.update({'downspeedf': downspeedf.command})

downspeedgraph = Commands('downspeedgraph', def_file('downspeedgraph'), 'true')
functions.update({'downspeedgraph': downspeedgraph.command})

draft_mails = Commands('draft_mails', def_file('draft_mails'), 'true')
functions.update({'draft_mails': draft_mails.command})

Else = Commands('else', def_file('else'), 'false')
functions.update({'else': Else.command})

endif = Commands('endif', def_file('endif'), 'false')
functions.update({'endif': endif.command})

entropy_avail = Commands('entropy_avail', def_file('entropy_avail'), 'false')
functions.update({'entropy_avail': entropy_avail.command})

entropy_bar = Commands('entropy_bar', def_file('entropy_bar'), 'true')
functions.update({'entropy_bar': entropy_bar.command})

entropy_perc = Commands('entropy_perc', def_file('entropy_perc'), 'false')
functions.update({'entropy_perc': entropy_perc.command})

entropy_poolsize = Commands('entropy_poolsize', def_file('entropy_poolsize'), 'false')
functions.update({'entropy_poolsize': entropy_poolsize.command})

execbar = Commands('execbar', def_file('execbar'), 'true')
functions.update({'execbar': execbar.command})

execgauge = Commands('execgauge', def_file('execgauge'), 'true')
functions.update({'execgauge': execgauge.command})

execgraph = Commands('execgraph', def_file('execgraph'), 'true')
functions.update({'execgraph': execgraph.command})

execi = Commands('execi', def_file('execi'), 'true')
functions.update({'execi': execi.command})

execibar = Commands('execibar', def_file('execibar'), 'true')
functions.update({'execibar': execibar.command})

execigauge = Commands('execigauge', def_file('execigauge'), 'true')
functions.update({'execigauge': execigauge.command})

execigraph = Commands('execigraph', def_file('execigraph'), 'true')
functions.update({'execigraph': execigraph.command})

execp = Commands('execp', def_file('execp'), 'true')
functions.update({'execp': execp.command})

execpi = Commands('execpi', def_file('execpi'), 'true')
functions.update({'execpi': execpi.command})

flagged_mails = Commands('flagged_mails', def_file('flagged_mails'), 'true')
functions.update({'flagged_mails': flagged_mails.command})

font = Commands('font', def_file('font'), 'true')
functions.update({'font': font.command})

fontN = Commands('fontN', def_file('fontN'), 'false')
functions.update({'fontN': fontN.command})

format_time = Commands('format_time', def_file('format_time'), 'true')
functions.update({'format_time': format_time.command})

forwarded_mails = Commands('forwarded_mails', def_file('forwarded_mails'), 'true')
functions.update({'forwarded_mails': forwarded_mails.command})

freq = Commands('freq', def_file('freq'), 'true')
functions.update({'freq': freq.command})

freq2 = Commands('freq2', def_file('freq2'), 'true')
functions.update({'freq2': freq2.command})

freq_g = Commands('freq_g', def_file('freq_g'), 'true')
functions.update({'freq_g': freq_g.command})

fs_bar = Commands('fs_bar', def_file('fs_bar'), 'true')
functions.update({'fs_bar': fs_bar.command})

fs_bar_free = Commands('fs_bar_free', def_file('fs_bar_free'), 'true')
functions.update({'fs_bar_free': fs_bar_free.command})

fs_free = Commands('fs_free', def_file('fs_free'), 'true')
functions.update({'fs_free': fs_free.command})

fs_free_perc = Commands('fs_free_perc', def_file('fs_free_perc'), 'true')
functions.update({'fs_free_perc': fs_free_perc.command})

fs_size = Commands('fs_size', def_file('fs_size'), 'true')
functions.update({'fs_size': fs_size.command})

fs_type = Commands('fs_type', def_file('fs_type'), 'true')
functions.update({'fs_type': fs_type.command})

fs_used = Commands('fs_used', def_file('fs_used'), 'true')
functions.update({'fs_used': fs_used.command})

fs_used_perc = Commands('fs_used_perc', def_file('fs_used_perc'), 'true')
functions.update({'fs_used_perc': fs_used_perc.command})

gid_name = Commands('gid_name', def_file('gid_name'), 'true')
functions.update({'gid_name': gid_name.command})

github_notifications = Commands('github_notifications', def_file('github_notifications'), 'false')
functions.update({'github_notifications': github_notifications.command})

goto = Commands('goto', def_file('goto'), 'true')
functions.update({'goto': goto.command})

gputemp = Commands('gputemp', def_file('gputemp'), 'true')
functions.update({'gputemp': gputemp.command})

gw_iface = Commands('gw_iface', def_file('gw_iface'), 'false')
functions.update({'gw_iface': gw_iface.command})

gw_ip = Commands('gw_ip', def_file('gw_ip'), 'false')
functions.update({'gw_ip': gw_ip.command})

hddtemp = Commands('hddtemp', def_file('hddtemp'), 'true')
functions.update({'hddtemp': hddtemp.command})

head = Commands('head', def_file('head'), 'true')
functions.update({'head': head.command})

hr = Commands('hr', def_file('hr'), 'true')
functions.update({'hr': hr.command})

humidity = Commands('humidity', def_file('humidity'), 'false')
functions.update({'humidity': humidity.command})

hwmon = Commands('hwmon', def_file('hwmon'), 'true')
functions.update({'hwmon': hwmon.command})

i2c = Commands('i2c', def_file('i2c'), 'true')
functions.update({'i2c': i2c.command})

i8k_ac_status = Commands('i8k_ac_status', def_file('i8k_ac_status'), 'false')
functions.update({'i8k_ac_status': i8k_ac_status.command})

i8k_bios = Commands('i8k_bios', def_file('i8k_bios'), 'false')
functions.update({'i8k_bios': i8k_bios.command})

i8k_buttons_status = Commands('i8k_buttons_status', def_file('i8k_buttons_status'), 'false')
functions.update({'i8k_buttons_status': i8k_buttons_status.command})

i8k_cpu_temp = Commands('i8k_cpu_temp', def_file('i8k_cpu_temp'), 'false')
functions.update({'i8k_cpu_temp': i8k_cpu_temp.command})

i8k_left_fan_rpm = Commands('i8k_left_fan_rpm', def_file('i8k_left_fan_rpm'), 'false')
functions.update({'i8k_left_fan_rpm': i8k_left_fan_rpm.command})

i8k_left_fan_status = Commands('i8k_left_fan_status', def_file('i8k_left_fan_status'), 'false')
functions.update({'i8k_left_fan_status': i8k_left_fan_status.command})

i8k_right_fan_rpm = Commands('i8k_right_fan_rpm', def_file('i8k_right_fan_rpm'), 'false')
functions.update({'i8k_right_fan_rpm': i8k_right_fan_rpm.command})

i8k_right_fan_status = Commands('i8k_right_fan_status', def_file('i8k_right_fan_status'), 'false')
functions.update({'i8k_right_fan_status': i8k_right_fan_status.command})

i8k_version = Commands('i8k_version', def_file('i8k_version'), 'false')
functions.update({'i8k_version': i8k_version.command})

ibm_brightness = Commands('ibm_brightness', def_file('ibm_brightness'), 'false')
functions.update({'ibm_brightness': ibm_brightness.command})

ibm_fan = Commands('ibm_fan', def_file('ibm_fan'), 'false')
functions.update({'ibm_fan': ibm_fan.command})

ibm_temps = Commands('ibm_temps', def_file('ibm_temps'), 'true')
functions.update({'ibm_temps': ibm_temps.command})

ibm_thinklight = Commands('ibm_thinklight', def_file('ibm_thinklight'), 'false')
functions.update({'ibm_thinklight': ibm_thinklight.command})

ibm_volume = Commands('ibm_volume', def_file('ibm_volume'), 'false')
functions.update({'ibm_volume': ibm_volume.command})

ical = Commands('ical', def_file('ical'), 'true')
functions.update({'ical': ical.command})

iconv_stop = Commands('iconv_stop', def_file('iconv_stop'), 'false')
functions.update({'iconv_stop': iconv_stop.command})

if_empty = Commands('if_empty', def_file('if_empty'), 'true')
functions.update({'if_empty': if_empty.command})

if_existing = Commands('if_existing', def_file('if_existing'), 'true')
functions.update({'if_existing': if_existing.command})

if_gw = Commands('if_gw', def_file('if_gw'), 'false')
functions.update({'if_gw': if_gw.command})

if_match = Commands('if_match', def_file('if_match'), 'true')
functions.update({'if_match': if_match.command})

if_mixer_mute = Commands('if_mixer_mute', def_file('if_mixer_mute'), 'true')
functions.update({'if_mixer_mute': if_mixer_mute.command})

if_mounted = Commands('if_mounted', def_file('if_mounted'), 'true')
functions.update({'if_mounted': if_mounted.command})

if_mpd_playing = Commands('if_mpd_playing', def_file('if_mpd_playing'), 'false')
functions.update({'if_mpd_playing': if_mpd_playing.command})

if_running = Commands('if_running', def_file('if_running'), 'true')
functions.update({'if_running': if_running.command})

if_smapi_bat_installed = Commands('if_smapi_bat_installed', def_file('if_smapi_bat_installed'), 'true')
functions.update({'if_smapi_bat_installed': if_smapi_bat_installed.command})

if_up = Commands('if_up', def_file('if_up'), 'true')
functions.update({'if_up': if_up.command})

if_updatenr = Commands('if_updatenr', def_file('if_updatenr'), 'true')
functions.update({'if_updatenr': if_updatenr.command})

if_xmms2_connected = Commands('if_xmms2_connected', def_file('if_xmms2_connected'), 'false')
functions.update({'if_xmms2_connected': if_xmms2_connected.command})

iface = Commands('iface', def_file('iface'), 'true')
functions.update({'iface': iface.command})

image = Commands('image', def_file('image'), 'true')
functions.update({'image': image.command})

imap_messages = Commands('imap_messages', def_file('imap_messages'), 'true')
functions.update({'imap_messages': imap_messages.command})

imap_unseen = Commands('imap_unseen', def_file('imap_unseen'), 'true')
functions.update({'imap_unseen': imap_unseen.command})

ioscheduler = Commands('ioscheduler', def_file('ioscheduler'), 'true')
functions.update({'ioscheduler': ioscheduler.command})

irc = Commands('irc', def_file('irc'), 'true')
functions.update({'irc': irc.command})

journal = Commands('journal', def_file('journal'), 'true')
functions.update({'journal': journal.command})

kernel = Commands('kernel', def_file('kernel'), 'false')
functions.update({'kernel': kernel.command})

key_caps_lock = Commands('key_caps_lock', def_file('key_caps_lock'), 'false')
functions.update({'key_caps_lock': key_caps_lock.command})

key_num_lock = Commands('key_num_lock', def_file('key_num_lock'), 'false')
functions.update({'key_num_lock': key_num_lock.command})

key_scroll_lock = Commands('key_scroll_lock', def_file('key_scroll_lock'), 'false')
functions.update({'key_scroll_lock': key_scroll_lock.command})

keyboard_layout = Commands('keyboard_layout', def_file('keyboard_layout'), 'false')
functions.update({'keyboard_layout': keyboard_layout.command})

laptop_mode = Commands('laptop_mode', def_file('laptop_mode'), 'false')
functions.update({'laptop_mode': laptop_mode.command})

lines = Commands('lines', def_file('lines'), 'true')
functions.update({'lines': lines.command})

loadavg = Commands('loadavg', def_file('loadavg'), 'true')
functions.update({'loadavg': loadavg.command})

loadgraph = Commands('loadgraph', def_file('loadgraph'), 'true')
functions.update({'loadgraph': loadgraph.command})

lua = Commands('lua', def_file('lua'), 'true')
functions.update({'lua': lua.command})

lua_bar = Commands('lua_bar', def_file('lua_bar'), 'true')
functions.update({'lua_bar': lua_bar.command})

lua_gauge = Commands('lua_gauge', def_file('lua_gauge'), 'true')
functions.update({'lua_gauge': lua_gauge.command})

lua_graph = Commands('lua_graph', def_file('lua_graph'), 'true')
functions.update({'lua_graph': lua_graph.command})

lua_parse = Commands('lua_parse', def_file('lua_parse'), 'true')
functions.update({'lua_parse': lua_parse.command})

mails = Commands('mails', def_file('mails'), 'true')
functions.update({'mails': mails.command})

mboxscan = Commands('mboxscan', def_file('mboxscan'), 'true')
functions.update({'mboxscan': mboxscan.command})

mem = Commands('mem', def_file('mem'), 'false')
functions.update({'mem': mem.command})

membar = Commands('membar', def_file('membar'), 'true')
functions.update({'membar': membar.command})

memdirty = Commands('memdirty', def_file('memdirty'), 'false')
functions.update({'memdirty': memdirty.command})

memeasyfree = Commands('memeasyfree', def_file('memeasyfree'), 'false')
functions.update({'memeasyfree': memeasyfree.command})

memfree = Commands('memfree', def_file('memfree'), 'false')
functions.update({'memfree': memfree.command})

memgauge = Commands('memgauge', def_file('memgauge'), 'true')
functions.update({'memgauge': memgauge.command})

memgraph = Commands('memgraph', def_file('memgraph'), 'true')
functions.update({'memgraph': memgraph.command})

memmax = Commands('memmax', def_file('memmax'), 'false')
functions.update({'memmax': memmax.command})

memperc = Commands('memperc', def_file('memperc'), 'false')
functions.update({'memperc': memperc.command})

memwithbuffers = Commands('memwithbuffers', def_file('memwithbuffers'), 'false')
functions.update({'memwithbuffers': memwithbuffers.command})

memwithbuffersbar = Commands('memwithbuffersbar', def_file('memwithbuffersbar'), 'true')
functions.update({'memwithbuffersbar': memwithbuffersbar.command})

memwithbuffersgraph = Commands('memwithbuffersgraph', def_file('memwithbuffersgraph'), 'true')
functions.update({'memwithbuffersgraph': memwithbuffersgraph.command})

mixer = Commands('mixer', def_file('mixer'), 'true')
functions.update({'mixer': mixer.command})

mixerbar = Commands('mixerbar', def_file('mixerbar'), 'true')
functions.update({'mixerbar': mixerbar.command})

mixerl = Commands('mixerl', def_file('mixerl'), 'true')
functions.update({'mixerl': mixerl.command})

mixerlbar = Commands('mixerlbar', def_file('mixerlbar'), 'true')
functions.update({'mixerlbar': mixerlbar.command})

mixerr = Commands('mixerr', def_file('mixerr'), 'true')
functions.update({'mixerr': mixerr.command})

mixerrbar = Commands('mixerrbar', def_file('mixerrbar'), 'true')
functions.update({'mixerrbar': mixerrbar.command})

moc_album = Commands('moc_album', def_file('moc_album'), 'false')
functions.update({'moc_album': moc_album.command})

moc_artist = Commands('moc_artist', def_file('moc_artist'), 'false')
functions.update({'moc_artist': moc_artist.command})

moc_bitrate = Commands('moc_bitrate', def_file('moc_bitrate'), 'false')
functions.update({'moc_bitrate': moc_bitrate.command})

moc_curtime = Commands('moc_curtime', def_file('moc_curtime'), 'false')
functions.update({'moc_curtime': moc_curtime.command})

moc_file = Commands('moc_file', def_file('moc_file'), 'false')
functions.update({'moc_file': moc_file.command})

moc_rate = Commands('moc_rate', def_file('moc_rate'), 'false')
functions.update({'moc_rate': moc_rate.command})

moc_song = Commands('moc_song', def_file('moc_song'), 'false')
functions.update({'moc_song': moc_song.command})

moc_state = Commands('moc_state', def_file('moc_state'), 'false')
functions.update({'moc_state': moc_state.command})

moc_timeleft = Commands('moc_timeleft', def_file('moc_timeleft'), 'false')
functions.update({'moc_timeleft': moc_timeleft.command})

moc_title = Commands('moc_title', def_file('moc_title'), 'false')
functions.update({'moc_title': moc_title.command})

moc_totaltime = Commands('moc_totaltime', def_file('moc_totaltime'), 'false')
functions.update({'moc_totaltime': moc_totaltime.command})

monitor = Commands('monitor', def_file('monitor'), 'false')
functions.update({'monitor': monitor.command})

monitor_number = Commands('monitor_number', def_file('monitor_number'), 'false')
functions.update({'monitor_number': monitor_number.command})

mouse_speed = Commands('mouse_speed', def_file('mouse_speed'), 'false')
functions.update({'mouse_speed': mouse_speed.command})

mpd_album = Commands('mpd_album', def_file('mpd_album'), 'false')
functions.update({'mpd_album': mpd_album.command})

mpd_albumartist = Commands('mpd_albumartist', def_file('mpd_albumartist'), 'false')
functions.update({'mpd_albumartist': mpd_albumartist.command})

mpd_artist = Commands('mpd_artist', def_file('mpd_artist'), 'false')
functions.update({'mpd_artist': mpd_artist.command})

mpd_bar = Commands('mpd_bar', def_file('mpd_bar'), 'true')
functions.update({'mpd_bar': mpd_bar.command})

mpd_bitrate = Commands('mpd_bitrate', def_file('mpd_bitrate'), 'false')
functions.update({'mpd_bitrate': mpd_bitrate.command})

mpd_date = Commands('mpd_date', def_file('mpd_date'), 'false')
functions.update({'mpd_date': mpd_date.command})

mpd_elapsed = Commands('mpd_elapsed', def_file('mpd_elapsed'), 'false')
functions.update({'mpd_elapsed': mpd_elapsed.command})

mpd_file = Commands('mpd_file', def_file('mpd_file'), 'false')
functions.update({'mpd_file': mpd_file.command})

mpd_length = Commands('mpd_length', def_file('mpd_length'), 'false')
functions.update({'mpd_length': mpd_length.command})

mpd_name = Commands('mpd_name', def_file('mpd_name'), 'false')
functions.update({'mpd_name': mpd_name.command})

mpd_percent = Commands('mpd_percent', def_file('mpd_percent'), 'false')
functions.update({'mpd_percent': mpd_percent.command})

mpd_random = Commands('mpd_random', def_file('mpd_random'), 'false')
functions.update({'mpd_random': mpd_random.command})

mpd_repeat = Commands('mpd_repeat', def_file('mpd_repeat'), 'false')
functions.update({'mpd_repeat': mpd_repeat.command})

mpd_smart = Commands('mpd_smart', def_file('mpd_smart'), 'true')
functions.update({'mpd_smart': mpd_smart.command})

mpd_status = Commands('mpd_status', def_file('mpd_status'), 'false')
functions.update({'mpd_status': mpd_status.command})

mpd_title = Commands('mpd_title', def_file('mpd_title'), 'true')
functions.update({'mpd_title': mpd_title.command})

mpd_track = Commands('mpd_track', def_file('mpd_track'), 'false')
functions.update({'mpd_track': mpd_track.command})

mpd_vol = Commands('mpd_vol', def_file('mpd_vol'), 'false')
functions.update({'mpd_vol': mpd_vol.command})

mysql = Commands('mysql', def_file('mysql'), 'true')
functions.update({'mysql': mysql.command})

nameserver = Commands('nameserver', def_file('nameserver'), 'true')
functions.update({'nameserver': nameserver.command})

new_mails = Commands('new_mails', def_file('new_mails'), 'true')
functions.update({'new_mails': new_mails.command})

no_update = Commands('no_update', def_file('no_update'), 'true')
functions.update({'no_update': no_update.command})

nodename = Commands('nodename', def_file('nodename'), 'false')
functions.update({'nodename': nodename.command})

nodename_short = Commands('nodename_short', def_file('nodename_short'), 'false')
functions.update({'nodename_short': nodename_short.command})

nvidia = Commands('nvidia', def_file('nvidia'), 'true')
functions.update({'nvidia': nvidia.command})

nvidiabar = Commands('nvidiabar', def_file('nvidiabar'), 'true')
functions.update({'nvidiabar': nvidiabar.command})

nvidiagauge = Commands('nvidiagauge', def_file('nvidiagauge'), 'true')
functions.update({'nvidiagauge': nvidiagauge.command})

nvidiagraph = Commands('nvidiagraph', def_file('nvidiagraph'), 'true')
functions.update({'nvidiagraph': nvidiagraph.command})

offset = Commands('offset', def_file('offset'), 'true')
functions.update({'offset': offset.command})

outlinecolor = Commands('outlinecolor', def_file('outlinecolor'), 'true')
functions.update({'outlinecolor': outlinecolor.command})

pa_card_active_profile = Commands('pa_card_active_profile', def_file('pa_card_active_profile'), 'false')
functions.update({'pa_card_active_profile': pa_card_active_profile.command})

pa_card_name = Commands('pa_card_name', def_file('pa_card_name'), 'false')
functions.update({'pa_card_name': pa_card_name.command})

pa_sink_active_port_name = Commands('pa_sink_active_port_name', def_file('pa_sink_active_port_name'), 'false')
functions.update({'pa_sink_active_port_name': pa_sink_active_port_name.command})

pa_sink_description = Commands('pa_sink_description', def_file('pa_sink_description'), 'false')
functions.update({'pa_sink_description': pa_sink_description.command})

pa_sink_volume = Commands('pa_sink_volume', def_file('pa_sink_volume'), 'false')
functions.update({'pa_sink_volume': pa_sink_volume.command})

pa_sink_volumebar = Commands('pa_sink_volumebar', def_file('pa_sink_volumebar'), 'false')
functions.update({'pa_sink_volumebar': pa_sink_volumebar.command})

password = Commands('password', def_file('password'), 'true')
functions.update({'password': password.command})

pb_battery = Commands('pb_battery', def_file('pb_battery'), 'true')
functions.update({'pb_battery': pb_battery.command})

pid_chroot = Commands('pid_chroot', def_file('pid_chroot'), 'true')
functions.update({'pid_chroot': pid_chroot.command})

pid_cmdline = Commands('pid_cmdline', def_file('pid_cmdline'), 'true')
functions.update({'pid_cmdline': pid_cmdline.command})

pid_cwd = Commands('pid_cwd', def_file('pid_cwd'), 'true')
functions.update({'pid_cwd': pid_cwd.command})

pid_egid = Commands('pid_egid', def_file('pid_egid'), 'true')
functions.update({'pid_egid': pid_egid.command})

pid_environ = Commands('pid_environ', def_file('pid_environ'), 'true')
functions.update({'pid_environ': pid_environ.command})

pid_environ_list = Commands('pid_environ_list', def_file('pid_environ_list'), 'true')
functions.update({'pid_environ_list': pid_environ_list.command})

pid_euid = Commands('pid_euid', def_file('pid_euid'), 'true')
functions.update({'pid_euid': pid_euid.command})

pid_exe = Commands('pid_exe', def_file('pid_exe'), 'true')
functions.update({'pid_exe': pid_exe.command})

pid_fsgid = Commands('pid_fsgid', def_file('pid_fsgid'), 'true')
functions.update({'pid_fsgid': pid_fsgid.command})

pid_fsuid = Commands('pid_fsuid', def_file('pid_fsuid'), 'true')
functions.update({'pid_fsuid': pid_fsuid.command})

pid_gid = Commands('pid_gid', def_file('pid_gid'), 'true')
functions.update({'pid_gid': pid_gid.command})

pid_nice = Commands('pid_nice', def_file('pid_nice'), 'true')
functions.update({'pid_nice': pid_nice.command})

pid_openfiles = Commands('pid_openfiles', def_file('pid_openfiles'), 'true')
functions.update({'pid_openfiles': pid_openfiles.command})

pid_parent = Commands('pid_parent', def_file('pid_parent'), 'true')
functions.update({'pid_parent': pid_parent.command})

pid_priority = Commands('pid_priority', def_file('pid_priority'), 'true')
functions.update({'pid_priority': pid_priority.command})

pid_read = Commands('pid_read', def_file('pid_read'), 'true')
functions.update({'pid_read': pid_read.command})

pid_sgid = Commands('pid_sgid', def_file('pid_sgid'), 'true')
functions.update({'pid_sgid': pid_sgid.command})

pid_state = Commands('pid_state', def_file('pid_state'), 'true')
functions.update({'pid_state': pid_state.command})

pid_state_short = Commands('pid_state_short', def_file('pid_state_short'), 'true')
functions.update({'pid_state_short': pid_state_short.command})

pid_stderr = Commands('pid_stderr', def_file('pid_stderr'), 'true')
functions.update({'pid_stderr': pid_stderr.command})

pid_stdin = Commands('pid_stdin', def_file('pid_stdin'), 'true')
functions.update({'pid_stdin': pid_stdin.command})

pid_stdout = Commands('pid_stdout', def_file('pid_stdout'), 'true')
functions.update({'pid_stdout': pid_stdout.command})

pid_suid = Commands('pid_suid', def_file('pid_suid'), 'true')
functions.update({'pid_suid': pid_suid.command})

pid_thread_list = Commands('pid_thread_list', def_file('pid_thread_list'), 'true')
functions.update({'pid_thread_list': pid_thread_list.command})

pid_threads = Commands('pid_threads', def_file('pid_threads'), 'true')
functions.update({'pid_threads': pid_threads.command})

pid_time = Commands('pid_time', def_file('pid_time'), 'true')
functions.update({'pid_time': pid_time.command})

pid_time_kernelmode = Commands('pid_time_kernelmode', def_file('pid_time_kernelmode'), 'true')
functions.update({'pid_time_kernelmode': pid_time_kernelmode.command})

pid_time_usermode = Commands('pid_time_usermode', def_file('pid_time_usermode'), 'true')
functions.update({'pid_time_usermode': pid_time_usermode.command})

pid_uid = Commands('pid_uid', def_file('pid_uid'), 'true')
functions.update({'pid_uid': pid_uid.command})

pid_vmdata = Commands('pid_vmdata', def_file('pid_vmdata'), 'true')
functions.update({'pid_vmdata': pid_vmdata.command})

pid_vmexe = Commands('pid_vmexe', def_file('pid_vmexe'), 'true')
functions.update({'pid_vmexe': pid_vmexe.command})

pid_vmhwm = Commands('pid_vmhwm', def_file('pid_vmhwm'), 'true')
functions.update({'pid_vmhwm': pid_vmhwm.command})

pid_vmlck = Commands('pid_vmlck', def_file('pid_vmlck'), 'true')
functions.update({'pid_vmlck': pid_vmlck.command})

pid_vmlib = Commands('pid_vmlib', def_file('pid_vmlib'), 'true')
functions.update({'pid_vmlib': pid_vmlib.command})

pid_vmpeak = Commands('pid_vmpeak', def_file('pid_vmpeak'), 'true')
functions.update({'pid_vmpeak': pid_vmpeak.command})

pid_vmpte = Commands('pid_vmpte', def_file('pid_vmpte'), 'true')
functions.update({'pid_vmpte': pid_vmpte.command})

pid_vmrss = Commands('pid_vmrss', def_file('pid_vmrss'), 'true')
functions.update({'pid_vmrss': pid_vmrss.command})

pid_vmsize = Commands('pid_vmsize', def_file('pid_vmsize'), 'true')
functions.update({'pid_vmsize': pid_vmsize.command})

pid_vmstk = Commands('pid_vmstk', def_file('pid_vmstk'), 'true')
functions.update({'pid_vmstk': pid_vmstk.command})

pid_write = Commands('pid_write', def_file('pid_write'), 'true')
functions.update({'pid_write': pid_write.command})

platform = Commands('platform', def_file('platform'), 'true')
functions.update({'platform': platform.command})

pop3_unseen = Commands('pop3_unseen', def_file('pop3_unseen'), 'true')
functions.update({'pop3_unseen': pop3_unseen.command})

pop3_used = Commands('pop3_used', def_file('pop3_used'), 'true')
functions.update({'pop3_used': pop3_used.command})

pressure = Commands('pressure', def_file('pressure'), 'false')
functions.update({'pressure': pressure.command})

processes = Commands('processes', def_file('processes'), 'false')
functions.update({'processes': processes.command})

read_tcp = Commands('read_tcp', def_file('read_tcp'), 'true')
functions.update({'read_tcp': read_tcp.command})

read_udp = Commands('read_udp', def_file('read_udp'), 'true')
functions.update({'read_udp': read_udp.command})

replied_mails = Commands('replied_mails', def_file('replied_mails'), 'true')
functions.update({'replied_mails': replied_mails.command})

rss = Commands('rss', def_file('rss'), 'true')
functions.update({'rss': rss.command})

running_processes = Commands('running_processes', def_file('running_processes'), 'false')
functions.update({'running_processes': running_processes.command})

running_threads = Commands('running_threads', def_file('running_threads'), 'false')
functions.update({'running_threads': running_threads.command})

scroll = Commands('scroll', def_file('scroll'), 'true')
functions.update({'scroll': scroll.command})

seen_mails = Commands('seen_mails', def_file('seen_mails'), 'true')
functions.update({'seen_mails': seen_mails.command})

shadecolor = Commands('shadecolor', def_file('shadecolor'), 'true')
functions.update({'shadecolor': shadecolor.command})

sip_status = Commands('sip_status', def_file('sip_status'), 'true')
functions.update({'sip_status': sip_status.command})

smapi = Commands('smapi', def_file('smapi'), 'true')
functions.update({'smapi': smapi.command})

smapi_bat_bar = Commands('smapi_bat_bar', def_file('smapi_bat_bar'), 'true')
functions.update({'smapi_bat_bar': smapi_bat_bar.command})

smapi_bat_perc = Commands('smapi_bat_perc', def_file('smapi_bat_perc'), 'true')
functions.update({'smapi_bat_perc': smapi_bat_perc.command})

smapi_bat_power = Commands('smapi_bat_power', def_file('smapi_bat_power'), 'true')
functions.update({'smapi_bat_power': smapi_bat_power.command})

smapi_bat_temp = Commands('smapi_bat_temp', def_file('smapi_bat_temp'), 'true')
functions.update({'smapi_bat_temp': smapi_bat_temp.command})

sony_fanspeed = Commands('sony_fanspeed', def_file('sony_fanspeed'), 'false')
functions.update({'sony_fanspeed': sony_fanspeed.command})

start_case = Commands('start_case', def_file('start_case'), 'true')
functions.update({'start_case': start_case.command})

stippled_hr = Commands('stippled_hr', def_file('stippled_hr'), 'true')
functions.update({'stippled_hr': stippled_hr.command})

stock = Commands('stock', def_file('stock'), 'true')
functions.update({'stock': stock.command})

swap = Commands('swap', def_file('swap'), 'false')
functions.update({'swap': swap.command})

swapbar = Commands('swapbar', def_file('swapbar'), 'true')
functions.update({'swapbar': swapbar.command})

swapfree = Commands('swapfree', def_file('swapfree'), 'false')
functions.update({'swapfree': swapfree.command})

swapmax = Commands('swapmax', def_file('swapmax'), 'false')
functions.update({'swapmax': swapmax.command})

swapperc = Commands('swapperc', def_file('swapperc'), 'false')
functions.update({'swapperc': swapperc.command})

sysctlbyname = Commands('sysctlbyname', def_file('sysctlbyname'), 'true')
functions.update({'sysctlbyname': sysctlbyname.command})

sysname = Commands('sysname', def_file('sysname'), 'false')
functions.update({'sysname': sysname.command})

tab = Commands('tab', def_file('tab'), 'true')
functions.update({'tab': tab.command})

tail = Commands('tail', def_file('tail'), 'true')
functions.update({'tail': tail.command})

tcp_ping = Commands('tcp_ping', def_file('tcp_ping'), 'true')
functions.update({'tcp_ping': tcp_ping.command})

tcp_portmon = Commands('tcp_portmon', def_file('tcp_portmon'), 'true')
functions.update({'tcp_portmon': tcp_portmon.command})

templateN = Commands('templateN', def_file('templateN'), 'true')
functions.update({'templateN': templateN.command})

texeci = Commands('texeci', def_file('texeci'), 'true')
functions.update({'texeci': texeci.command})

texecpi = Commands('texecpi', def_file('texecpi'), 'true')
functions.update({'texecpi': texecpi.command})

threads = Commands('threads', def_file('threads'), 'false')
functions.update({'threads': threads.command})

time = Commands('time', def_file('time'), 'true')
functions.update({'time': time.command})

to_bytes = Commands('to_bytes', def_file('to_bytes'), 'true')
functions.update({'to_bytes': to_bytes.command})

top = Commands('top', def_file('top'), 'true')
functions.update({'top': top.command})

top_io = Commands('top_io', def_file('top_io'), 'true')
functions.update({'top_io': top_io.command})

top_mem = Commands('top_mem', def_file('top_mem'), 'true')
functions.update({'top_mem': top_mem.command})

top_time = Commands('top_time', def_file('top_time'), 'true')
functions.update({'top_time': top_time.command})

totaldown = Commands('totaldown', def_file('totaldown'), 'true')
functions.update({'totaldown': totaldown.command})

totalup = Commands('totalup', def_file('totalup'), 'true')
functions.update({'totalup': totalup.command})

trashed_mails = Commands('trashed_mails', def_file('trashed_mails'), 'true')
functions.update({'trashed_mails': trashed_mails.command})

tztime = Commands('tztime', def_file('tztime'), 'true')
functions.update({'tztime': tztime.command})

uid_name = Commands('uid_name', def_file('uid_name'), 'true')
functions.update({'uid_name': uid_name.command})

unflagged_mails = Commands('unflagged_mails', def_file('unflagged_mails'), 'true')
functions.update({'unflagged_mails': unflagged_mails.command})

unforwarded_mails = Commands('unforwarded_mails', def_file('unforwarded_mails'), 'true')
functions.update({'unforwarded_mails': unforwarded_mails.command})

unreplied_mails = Commands('unreplied_mails', def_file('unreplied_mails'), 'true')
functions.update({'unreplied_mails': unreplied_mails.command})

unseen_mails = Commands('unseen_mails', def_file('unseen_mails'), 'true')
functions.update({'unseen_mails': unseen_mails.command})

updates = Commands('updates', def_file('updates'), 'true')
functions.update({'updates': updates.command})

upspeed = Commands('upspeed', def_file('upspeed'), 'true')
functions.update({'upspeed': upspeed.command})

upspeedf = Commands('upspeedf', def_file('upspeedf'), 'true')
functions.update({'upspeedf': upspeedf.command})

upspeedgraph = Commands('upspeedgraph', def_file('upspeedgraph'), 'true')
functions.update({'upspeedgraph': upspeedgraph.command})

uptime = Commands('uptime', def_file('uptime'), 'false')
functions.update({'uptime': uptime.command})

uptime_short = Commands('uptime_short', def_file('uptime_short'), 'false')
functions.update({'uptime_short': uptime_short.command})

user_names = Commands('user_names', def_file('user_names'), 'false')
functions.update({'user_names': user_names.command})

user_number = Commands('user_number', def_file('user_number'), 'false')
functions.update({'user_number': user_number.command})

user_terms = Commands('user_terms', def_file('user_terms'), 'false')
functions.update({'user_terms': user_terms.command})

user_time = Commands('user_time', def_file('user_time'), 'true')
functions.update({'user_time': user_time.command})

user_times = Commands('user_times', def_file('user_times'), 'false')
functions.update({'user_times': user_times.command})

utime = Commands('utime', def_file('utime'), 'true')
functions.update({'utime': utime.command})

v6addrs = Commands('v6addrs', def_file('v6addrs'), 'true')
functions.update({'v6addrs': v6addrs.command})

version = Commands('version', def_file('version'), 'false')
functions.update({'version': version.command})

voffset = Commands('voffset', def_file('voffset'), 'true')
functions.update({'voffset': voffset.command})

voltage_mv = Commands('voltage_mv', def_file('voltage_mv'), 'true')
functions.update({'voltage_mv': voltage_mv.command})

voltage_v = Commands('voltage_v', def_file('voltage_v'), 'true')
functions.update({'voltage_v': voltage_v.command})

weather = Commands('weather', def_file('weather'), 'true')
functions.update({'weather': weather.command})

weather_forecast = Commands('weather_forecast', def_file('weather_forecast'), 'true')
functions.update({'weather_forecast': weather_forecast.command})

wind_dir = Commands('wind_dir', def_file('wind_dir'), 'false')
functions.update({'wind_dir': wind_dir.command})

wind_dir_DEG = Commands('wind_dir_DEG', def_file('wind_dir_DEG'), 'false')
functions.update({'wind_dir_DEG': wind_dir_DEG.command})

wind_speed = Commands('wind_speed', def_file('wind_speed'), 'false')
functions.update({'wind_speed': wind_speed.command})

wireless_ap = Commands('wireless_ap', def_file('wireless_ap'), 'true')
functions.update({'wireless_ap': wireless_ap.command})

wireless_bitrate = Commands('wireless_bitrate', def_file('wireless_bitrate'), 'true')
functions.update({'wireless_bitrate': wireless_bitrate.command})

wireless_channel = Commands('wireless_channel', def_file('wireless_channel'), 'true')
functions.update({'wireless_channel': wireless_channel.command})

wireless_essid = Commands('wireless_essid', def_file('wireless_essid'), 'true')
functions.update({'wireless_essid': wireless_essid.command})

wireless_freq = Commands('wireless_freq', def_file('wireless_freq'), 'true')
functions.update({'wireless_freq': wireless_freq.command})

wireless_link_bar = Commands('wireless_link_bar', def_file('wireless_link_bar'), 'true')
functions.update({'wireless_link_bar': wireless_link_bar.command})

wireless_link_qual = Commands('wireless_link_qual', def_file('wireless_link_qual'), 'true')
functions.update({'wireless_link_qual': wireless_link_qual.command})

wireless_link_qual_max = Commands('wireless_link_qual_max', def_file('wireless_link_qual_max'), 'true')
functions.update({'wireless_link_qual_max': wireless_link_qual_max.command})

wireless_link_qual_perc = Commands('wireless_link_qual_perc', def_file('wireless_link_qual_perc'), 'true')
functions.update({'wireless_link_qual_perc': wireless_link_qual_perc.command})

wireless_mode = Commands('wireless_mode', def_file('wireless_mode'), 'true')
functions.update({'wireless_mode': wireless_mode.command})

words = Commands('words', def_file('words'), 'true')
functions.update({'words': words.command})

xmms2_album = Commands('xmms2_album', def_file('xmms2_album'), 'false')
functions.update({'xmms2_album': xmms2_album.command})

xmms2_artist = Commands('xmms2_artist', def_file('xmms2_artist'), 'false')
functions.update({'xmms2_artist': xmms2_artist.command})

xmms2_bar = Commands('xmms2_bar', def_file('xmms2_bar'), 'true')
functions.update({'xmms2_bar': xmms2_bar.command})

xmms2_bitrate = Commands('xmms2_bitrate', def_file('xmms2_bitrate'), 'false')
functions.update({'xmms2_bitrate': xmms2_bitrate.command})

xmms2_comment = Commands('xmms2_comment', def_file('xmms2_comment'), 'false')
functions.update({'xmms2_comment': xmms2_comment.command})

xmms2_date = Commands('xmms2_date', def_file('xmms2_date'), 'false')
functions.update({'xmms2_date': xmms2_date.command})

xmms2_duration = Commands('xmms2_duration', def_file('xmms2_duration'), 'false')
functions.update({'xmms2_duration': xmms2_duration.command})

xmms2_elapsed = Commands('xmms2_elapsed', def_file('xmms2_elapsed'), 'false')
functions.update({'xmms2_elapsed': xmms2_elapsed.command})

xmms2_genre = Commands('xmms2_genre', def_file('xmms2_genre'), 'false')
functions.update({'xmms2_genre': xmms2_genre.command})

xmms2_id = Commands('xmms2_id', def_file('xmms2_id'), 'false')
functions.update({'xmms2_id': xmms2_id.command})

xmms2_percent = Commands('xmms2_percent', def_file('xmms2_percent'), 'false')
functions.update({'xmms2_percent': xmms2_percent.command})

xmms2_playlist = Commands('xmms2_playlist', def_file('xmms2_playlist'), 'false')
functions.update({'xmms2_playlist': xmms2_playlist.command})

xmms2_size = Commands('xmms2_size', def_file('xmms2_size'), 'false')
functions.update({'xmms2_size': xmms2_size.command})

xmms2_smart = Commands('xmms2_smart', def_file('xmms2_smart'), 'false')
functions.update({'xmms2_smart': xmms2_smart.command})

xmms2_status = Commands('xmms2_status', def_file('xmms2_status'), 'false')
functions.update({'xmms2_status': xmms2_status.command})

xmms2_timesplayed = Commands('xmms2_timesplayed', def_file('xmms2_timesplayed'), 'false')
functions.update({'xmms2_timesplayed': xmms2_timesplayed.command})

xmms2_title = Commands('xmms2_title', def_file('xmms2_title'), 'false')
functions.update({'xmms2_title': xmms2_title.command})

xmms2_tracknr = Commands('xmms2_tracknr', def_file('xmms2_tracknr'), 'false')
functions.update({'xmms2_tracknr': xmms2_tracknr.command})

xmms2_url = Commands('xmms2_url', def_file('xmms2_url'), 'false')
functions.update({'xmms2_url': xmms2_url.command})

