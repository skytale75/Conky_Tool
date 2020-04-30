from tkinter import *
# 593
class conky_stuff:
    '''variables to carry throughout execution of commands'''
        
    # variables
    x = 0
    y = 0
    results = []

# setup dictionary function . . . functions = {"functon_name:" function}
# call dictionary function . . . functions["function_name"]()

class Commands:


    def __init__(self, com_name, com_des, unique_command):
        self.com_name = com_name
        self.com_des = com_des
        self.unique_command = unique_command

    def command(self, file_display):
        """translate command name to command and insert
        unless command has custom command 'unique_command'"""
        print("running command")
        if self.unique_command == "false":
            com_out = "${"+self.com_name+"}"
            file_display.insert(INSERT, com_out)
        if self.unique_command == "true":
            print("make a custom command for "+self.com_name)

    def command_out(self, cl_output):
        """puts conky command names in appropriate format"""
        cl_output.insert(INSERT, self.com_name+"\n")

    def definition_out(self, cd_output):
        cd_output.delete(0.0, END)
        cd_output.insert(INSERT, self.com_des)


    def dummy(self):
        print("make function")


def def_file(my_input):
    """open definition file and return as a string"""
    open_file = open("./coms/"+my_input+".txt")
    read_file = open_file.read()
    open_file.close()
    return str(read_file)

cm = Commands
# complete list of conky commands for text section
# definitions are in file in coms folder, def_file() opens and returns them as a string.

acpiacadapter = Commands("acpiacadapter (adapter)", def_file("acpiacadapter"), "false")
functions = {"acpiacadapter (adapter)": acpiacadapter}

# acpifan = Commands("acpifan", def_file("acpifan"), "false")
# functions.update({"acpifan": acpifan.command})

acpifan = Commands('acpifan', def_file('acpifan'), 'false')
functions.update({'acpifan': acpifan.command})

acpitemp = Commands("acpitemp", def_file("acpitemp"), "false")
functions.update({"acpitemp": acpitemp.command})

addr = Commands("addr", def_file("addr"), "true")
functions.update({"addr (interface)": addr.command})

addrs = Commands("addrs", def_file("addrs"), "true")
functions.update({"addrs (interface)": addrs.command})

adt746xcpu = Commands("adt746xpcu", def_file("adt746xpcu"), "false")
functions.update({"adt746xcpu": adt746xcpu.command})

adt746xfan = Commands("adt746xfan", def_file("adt746xfan"), "false")
functions.update({"adt746xfan": adt746xfan.command})

alignc = Commands("alignc", def_file("alignc"), "false")
functions.update({"alignc (number)": alignc.command})

alignr = Commands("alignr", def_file("alignr"), "false")
functions.update({"alignr (number)": alignr.command})

apcupsd = Commands("apcupsd host port", def_file("apcupsd"), "false")
functions.update({"apcupsd host port": apcupsd.command})

apcupsd_cable = Commands("apcupsd_cable", def_file("apcupsd_cable"), "false")
functions.update({"apcupsd_cable": apcupsd_cable.command})

apcupsd_charge = Commands("apcupsd_charge", def_file("apcupsd_charge"), "false")
functions.update({"apcupsd_charge": apcupsd_charge.command})

apcupsd_lastxfer = Commands("apcupsd_lastxfer", def_file("apcupsd_lastxfer"), "false")
functions.update({"apcupsd_lastxfer": apcupsd_lastxfer.command})

apcupsd_linev = Commands("apcupsd_linev", def_file("apcupsd_linev"), "false")
functions.update({"apcupsd_linev": apcupsd_linev.command})

apcupsd_load = Commands("apcupsd_load", def_file("apcupsd_load"), "false")
functions.update({"apcupsd_load": apcupsd_load.command})

apcupsd_loadbar = Commands("apcupsd_loadbar", def_file("apcupsd_loadbar"), "false")
functions.update({"apcupsd_loadbar": apcupsd_loadbar.command})

apcupsd_loadgauge = Commands("apcupsd_loadgauge (height),(width)", def_file('apcupsd_loadgauge'), "true")
functions.update({"apcupsd_loadgauge (height),(width)": apcupsd_loadgauge.command})

apcupsd_loadgraph = Commands("apcupsd_loadgraph", def_file('apcupsd_loadgraph'), "true")
functions.update({"apcupsd_loadgraph": apcupsd_loadgraph.command})

apcupsd_model = Commands("apcupsd_model", def_file("apcupsd_model"), "false")
functions.update({"apcupsd_model": apcupsd_model.command})

apcupsd_name = Commands("apcupsd_name", def_file("apcupsd_name"), "false")
functions.update({"apcupsd_name": apcupsd_name.command})

apcupsd_status = Commands("apcupsd_status", def_file("apcupsd_status"), "false")
functions.update({"apcupsd_status": apcupsd_status.command})

apcupsd_temp = Commands("apcupsd_temp", def_file("apcupsd_temp"), "false")
functions.update({"apcupsd_temp": apcupsd_temp.command})

apcupsd_timeleft = Commands("apcupsd_timeleft", def_file("apcupsd_timeleft"), "false")
functions.update({"apcupsd_timeleft": apcupsd_timeleft.command})

apcupsd_upsmode = Commands("apcupsd_upsmode", def_file("apcupsd_upsmode"), "false")
functions.update({"apcupsd_upsmode": apcupsd_upsmode.command})

apm_adapter = Commands("apm_adapter", def_file("apm_adapter"), "false")
functions.update({"apm_adapter": apm_adapter.command})

apm_battery_life = Commands("apm_battery_life", def_file("apm_battery_life"), "false")
functions.update({"apm_battery_life": apm_battery_life.command})

apm_battery_time = Commands("apm_battery_time", def_file("apm_battery_time"), "false")
functions.update({"apm_battery_time": apm_battery_time.command})

audacious_bar = Commands("audacious_bar", def_file("audacious_bar"), "true")
functions.update({"audacious_bar": audacious_bar.command})

audacious_bitrate = Commands("audacious_bitrate", def_file("audacious_bitrate"), "true")
functions.update({"audacious_bitrate": audacious_bitrate.command})

audacious_channels = Commands("audacious_channels", def_file("audacious_channels"), "false")
functions.update({"audacious_channels": audacious_channels.command})

audacious_filename = Commands("audacious_filename", def_file("audacious_filename"), "false")
functions.update({"audacious_filename": audacious_filename.command})

audacious_frequency = Commands("audacious_frequency", def_file("audacious_frequency"), "false")
functions.update({"audacious_frequency": audacious_frequency.command})

audacious_length = Commands("audacious_length", def_file("audacious_length"), "false")
functions.update({"audacious_length": audacious_length.command})

audacious_length_seconds = Commands("audacious_length_seconds", def_file("audacious_length_seconds"), "false")
functions.update({"audacious_length_seconds": audacious_length_seconds.command})

audacious_main_volume = Commands("audacious_main_volume", def_file("audacious_main_volume"), "false")
functions.update({"audacious_main_volume": audacious_main_volume.command})

audacious_playlist_length = Commands("audacious_playlist_length", def_file("audacious_playlist_length"), "false")
functions.update({"audacious_playlist_length": audacious_playlist_length.command})

audacious_playlist_position = Commands("audacious_playlist_position", def_file("audacious_playlist_position"), "false")
functions.update({"audacious_playlist_position": audacious_playlist_position.command})

audacious_position = Commands("audacious_position", def_file("audacious_position"), "false")
functions.update({"audacious_position": audacious_position.command})

audacious_position_seconds = Commands("audacious_position_seconds", def_file("audacious_position_seconds"), "false")
functions.update({"audacious_position_seconds": audacious_position_seconds.command})

audacious_status = Commands("audacious_status", def_file("audacious_status"), "false")
functions.update({"audacious_status": audacious_status.command})

audacious_title = Commands("audacious_title", def_file("audacious_title"), "true")
functions.update({"audacious_title": audacious_title.command})

battery = Commands("battery", def_file("battery"), "true")
functions.update({"battery": battery.command})

battery_bar = Commands("battery_bar", def_file("battery_bar"), "true")
functions.update({"battery_bar": battery_bar.command})

battery_percent = Commands("battery_percent", def_file("battery_percent"), "true")
functions.update({"battery_percent": battery_percent.command})

battery_short = Commands("battery_short", def_file("battery_short"), "true")
functions.update({"battery_short": battery_short.command})

battery_status = Commands("battery_status", def_file("battery_status"), "true")
functions.update({"battery_status": battery_status.command})

battery_time = Commands("battery_time", def_file("battery_time"), "true")
functions.update({"battery_time": battery_time.command})

blink = Commands("blink", def_file("blink"), "true")
functions.update({"blink": blink.command})

buffers = Commands("buffers", def_file("buffers"), "false")
functions.update({"buffers": buffers.command})

cached = Commands("cached", def_file("cached"), "false")
functions.update({"cached": cached.command})

cat = Commands("cat", def_file("cat"), "true")
functions.update({"cat": cat.command})

catp = Commands("catp", def_file("catp"), "true")
functions.update({"catp": catp.command})

cmdline_to_pid = Commands("cmdline_to_pid", def_file("cmdline_to_pid"), "true")
functions.update({"cmdline_to_pid": cmdline_to_pid.command})

cmus_aaa = Commands("cmus_aaa", def_file("cmus_aaa"), "false")
functions.update({"cmus_aaa": cmus_aaa.command})

cmus_album = Commands("cmus_album", def_file("cmus_album"), "false")
functions.update({"cmus_album": cmus_album.command})

cmus_artist = Commands("cmus_artist", def_file("cmus_artist"), "false")
functions.update({"cmus_artist": cmus_artist.command})

cmus_curtime = Commands("cmus_curtime", def_file("cmus_curtime"), "false")
functions.update({"cmus_curtime": cmus_curtime.command})

cmus_file = Commands("cmus_file", def_file("cmus_file"), "false")
functions.update({"cmus_file": cmus_file.command})

cmus_date = Commands("cmus_date", def_file("cmus_date"), "false")
functions.update({"cmus_date": cmus_date.command})

cmus_genre = Commands("cmus_genre", def_file("cmus_genre"), "false")
functions.update({"cmus_genre": cmus_genre.command})

cmus_percent = Commands("cmus_percent", def_file("cmus_percent"), "false")
functions.update({"cmus_percent": cmus_percent.command})

cmus_progress = Commands("cmus_progress", def_file("cmus_progress"), "true")
functions.update({"cmus_progress": cmus_progress.command})

cmus_random = Commands("cmus_random", def_file("cmus_random"), "false")
functions.update({"cmus_random": cmus_random.command})

cmus_repeat = Commands("cmus_repeat", def_file("cmus_repeat"), "false")
functions.update({"cmus_repeat": cmus_repeat.command})

cmus_state = Commands("cmus_state", def_file("cmus_repeat"), "false")
functions.update({"cmus_state": cmus_state.command})

cmus_timeleft = Commands("cmus_timeleft", def_file("cmus_timeleft"), "false")
functions.update({"cmus_timeleft": cmus_timeleft.command})

cmus_title = Commands("cmus_title", def_file("cmus_title"), "false")
functions.update({"cmus_title": cmus_title.command})

cmus_totaltime = Commands("cmus_totaltime", def_file("cmus_totaltime"), "false")
functions.update({"cmus_totaltime": cmus_totaltime.command})

cmus_track = Commands("cmus_track", def_file("cmus_track"), "false")
functions.update({"cmus_track": cmus_track.command})

combine = Commands("combine", def_file("combine"), "true")
functions.update({"combine": combine.command})

conky_build_arch = Commands("conky_build_arch", def_file("conky_build_arch"), "false")
functions.update({"conky_build_arch": conky_build_arch.command})

conky_build_date = Commands("conky_build_date", def_file("conky_build_date"), "false")
functions.update({"conky_build_date": conky_build_date.command})

conky_version = Commands("conky_version", def_file("conky_version"), "false")
functions.update({"conky_version": conky_version.command})

cpu = Commands("cpu", def_file("cpu"), "true")
functions.update({"cpu": cpu.command})

cpubar = Commands("cpubar", def_file("cpubar"), "true")
functions.update({"cpubar": cpubar.command})

cpugauge = Commands("cpugauge", def_file("cpugauge"), "true")
functions.update({"cpugauge": cpugauge.command})

cpugraph = Commands("cpugraph", def_file("cpugraph"), "true")
functions.update({"cpugraph": cpugraph.command})

curl = Commands("curl", def_file("curl"), "true")
functions.update({"curl": curl.command})

desktop = Commands("desktop", def_file("desktop"), "false")
functions.update({"desktop": desktop.command})

desktop_name = Commands("desktop_name", def_file("desktop_name"), "false")
functions.update({"desktop_name": desktop_name.command})

disk_protect = Commands("disk_protect", def_file("disk_protect"), "true")
functions.update({"disk_protect": disk_protect.command})

diskio = Commands("diskio", def_file("diskio"), "true")
functions.update({"diskio": diskio.command})

diskio_read = Commands("diskio_read", def_file("diskio_read"), "true")
functions.update({"diskio_read": diskio_read.command})

diskio_write = Commands("diskio_write", def_file("diskio_write"), "true")
functions.update({"diskio_write": diskio_write.command})

diskiograph = Commands("diskiograph", def_file("diskiograph"), "true")
functions.update({"diskiograph": diskiograph.command})

diskiograph_read = Commands("diskiograph_read", def_file("diskiograph_read"), "true")
functions.update({"diskiograph_read": diskiograph_read.command})

diskiograph_write = Commands("diskiograph_write", def_file("diskiograph_write"), "true")
functions.update({"diskiograph_write": diskiograph_write.command})

distribution = Commands("distribution", def_file("distribution"), "false")
functions.update({"distribution": distribution.command})

downspeed = Commands("downspeed", def_file("downspeed"), "true")
functions.update({"downspeed": downspeed.command})

downspeedf = Commands("downspeedf", def_file("downspeedf"), "false")
functions.update({"downspeedf": downspeedf.command})

downspeedgraph = Commands("downspeedgraph", def_file("downspeedgraph"), "true")
functions.update({"downspeedgraph": downspeedgraph.command})

draft_mails = Commands("draft_mails", def_file("draft_mails"), "true")
functions.update({"draft_mails": draft_mails.command})

entropy_avail = Commands("entropy_avail", def_file("entropy_avail"), "false")
functions.update({"entropy_avail": entropy_avail.command})

entropy_bar = Commands("entropy_bar", def_file("entropy_bar"), "false")
functions.update({"entropy_bar": entropy_bar.command})

entropy_perc = Commands("entropy_perc", def_file("entropy_perc"), "false")
functions.update({"entropy_perc": entropy_perc.command})

entropy_poolsize = Commands("entropy_poolsize", def_file("entropy_poolsize"), "false")
functions.update({"entropy_poolsize": entropy_poolsize.command})
# eval = python function so made capital to distinguish the two
Eval = Commands("Eval", def_file("Eval"), 'true')
functions.update({"Eval": Eval.command})
# Exec can't be exec because it is a python function. . . so make special function to compensate
Exec = Commands("Exec", def_file("Exec"), 'true')
functions.update({"Exec": Exec.command})

execbar = Commands("execbar", def_file("execbar"), 'true')
functions.update({"execbar": execbar.command})

execgauge = Commands("execgauge", def_file("execgauge"), 'true')
functions.update({"execgauge": execgauge.command})

execgraph = Commands("execgraph", def_file("execgraph"), 'true')
functions.update({"execgraph": execgraph.command})

execi = Commands("execi", def_file("execi"), 'true')
functions.update({"execi": execi.command})

execibar = Commands("execibar", def_file("execibar"), 'true')
functions.update({"execibar": execibar.command})

execigauge = Commands("execigauge", def_file("execigauge"), 'true')
functions.update({"execigauge": execigauge.command})

execigraph = Commands("execigraph", def_file("execigraph"), 'true')
functions.update({"execigraph": execigraph.command})

execp = Commands("execp", def_file("execp"), 'true')
functions.update({"execp": execp.command})

execpi = Commands("execpi", def_file("execpi"), 'true')
functions.update({"execpi": execpi.command})

flagged_mails = Commands("flagged_mails", def_file("flagged_mails"), 'true')
functions.update({"flagged_mails": flagged_mails.command})

format_time = Commands("format_time", def_file('format_time'), 'true')
functions.update({"format_time": format_time.command})

forwarded_mails = Commands("forwarded_mails", def_file('forwarded_mails'), 'true')
functions.update({"forwarded_mails": forwarded_mails.command})

freq = Commands("freq", def_file("freq"), 'true')
functions.update({"freq": freq.command})

freq_g = Commands("freq_g", def_file("freq_g"), 'true')
functions.update({"freq_g": freq_g.command})

freq2 = Commands("freq2", def_file("freq2"), 'true')
functions.update({"freq2": freq2.command})

fs_bar = Commands("fs_bar", def_file("fs_bar"), 'true')
functions.update({"fs_bar": fs_bar.command})

fs_bar_free = Commands("fs_bar_free", def_file("fs_bar_free"), 'true')
functions.update({"fs_bar_free": fs_bar_free.command})

fs_free = Commands("fs_free", def_file("fs_free"), 'true')
functions.update({"fs_free": fs_free.command})
