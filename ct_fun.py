from tkinter import *

class conky_stuff:
    '''variables to carry throughout execution of commands'''
        
    # variables
    x = 0
    y = 0

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
        else:
            print("make a custom command for "+self.com_name)

    def command_out(self, cl_output):
        cl_output.insert(INSERT, self.com_name+"\n")

    def definition_out(self, cd_output):
        cd_output.delete(0.0, END)
        cd_output.insert(INSERT, self.com_des)

    def dummy(self):
        print("make function")

acpiacadapter = Commands("acpiacadapter (adapter)", """\
    ACPI ac adapter state. On linux, the 
    adapter option specifies the subfolder of
    /sys/class/power_supply containing the state
    information (tries "AC" and "ADP1" if there is  
    no argument given). Non-linux systems ignore it.""",
    "false")
functions = {"acpiacadapter (adapter)": acpiacadapter}

acpifan = Commands("acpifan","ACPI fan state", "false")
functions.update({"acpifan": acpifan.command})

acpitemp = Commands("acpitemp", "ACPI temperature in C.", "false")
functions.update({"acpitemp": acpitemp.command})

addr = Commands("addr", """IP address for an interface, or
"No Address" if no address is assigned.""",
Commands.dummy)
functions.update({"addr (interface)": addr.command})

addrs = Commands("addrs", """IP addresses for an interface 
    (if one - works like addr). Linux only.""",
    Commands.dummy)
functions.update({"addrs (interface)": addrs.command})

adt746xcpu = Commands("adt746xpcu", "CPU temperature from therm_adt746x.", "false")
functions.update({"adt746xcpu": adt746xcpu.command})

adt746xfan = Commands("adt746xpcu", "Fan speed therm_adt746x.", "false")
functions.update({"adt746xfan": adt746xfan.command})

alignc = Commands("alignc", "align text to center.", "false")
functions.update({"alignc (number)": alignc.command})

alignr = Commands("alignr", "Right-justify text, with space of N.", "false")
functions.update({"alignr (number)": alignr.command})

apcupsd_host_port = Commands("apcupsd host port",
"Sets up the connection to apcupsd daemon. Prints nothing, defaults to localhost:3551.",
"false")
functions.update({"apcupsd host port": apcupsd_host_port.command})

apcupsd_cable = Commands("apcupsd_cable", "Prints the UPS connection type.", "false")
functions.update({"apcupsd_cable": apcupsd_cable.command})

apcupsd_charge = Commands("apcupsd_charge", "Current battery capacity in percent.", "false")
functions.update({"apcupsd_charge": apcupsd_charge.command})

apcupsd_lastxfer = Commands("apcupsd_lastxfer", "Reason for last transfer from line to battery", "false")
functions.update({"apcupsd_lastxfer": apcupsd_lastxfer.command})

apcupsd_linev = Commands("apcupsd_linev", "Nominal input voltage.", "false")
functions.update({"apcupsd_linev": apcupsd_linev.command})

apcupsd_load = Commands("apcupsd_load", "Current load in percent", "false")
functions.update({"apcupsd_load": apcupsd_load.command})

apcupsd_loadbar = Commands("apcupsd_loadbar", "Bar showing current load", "false")
functions.update({"apcupsd_loadbar": apcupsd_loadbar.command})

apcupsd_load_guage = Commands("apcupsd_load_guage (height),(width)", "Guage that shows current load.", "true")
functions.update({"apcupsd_load_guage (height),(width)": apcupsd_load_guage.command})

apcupsd_loadgraph = Commands("apcupsd_loadgraph", "History graph of current load", "true")
functions.update({"apcupsd_loadgraph": apcupsd_loadgraph.command})

apcupsd_model = Commands("apcupsd_model", "Prints the model of the UPS.", "false")
functions.update({"apcupsd_model": apcupsd_model.command})

apcupsd_name = Commands("apcupsd_name", "Prints the UPS user-defined name.", "false")
functions.update({"apcupsd_name": apcupsd_name.command})

apcupsd_status = Commands("apcupsd_status", "Prints current status (on-line, on-battery).", "false")
functions.update({"apcupsd_status": apcupsd_status.command})

apcupsd_temp = Commands("apcupsd_temp", "Print current internal temperature.", "false")
functions.update({"apcupsd_temp": apcupsd_temp.command})

apcupsd_timeleft = Commands("apcupsd_timeleft", "Time left to run on battery.", "false")
functions.update({"apcupsd_timeleft": apcupsd_timeleft.command})

apcupsd_upsmode = Commands("apcupsd_upsmode", "Prints the UPS mode (e.g. standalone).", "false")
functions.update({"apcupsd_upsmode": apcupsd_upsmode.command})

apm_adapter = Commands("apm_adapter", "Display APM AC adapter status. FreeBSD, OpenBSD only.", "false")
functions.update({"apm_adapter": apm_adapter.command})

apm_battery_life = Commands("apm_battery_life", "Display APM battery_life in percent. FreeBSD, OpenBSD only.", "false")
functions.update({"apm_battery_life": apm_battery_life.command})

apm_battery_time = Commands("apm_battery_time","""\
    Display remaining APM battery life in hh:mm:ss or
    "unknown" if AC adapterstatus is on-line or charging.
    FreeBSD, OpenBSD only.""",
    "false")
functions.update({"apm_battery_time": apm_battery_time.command})

audacious_bar = Commands("audacious_bar", "audacious music app progress bar", "true")
functions.update({"audacious_bar": audacious_bar.command})

audacious_bitrate = Commands("audacious_bitrate", "Bitrate of current track in audacious music app.", "true")
functions.update({"audacious_bitrate": audacious_bitrate.command})

audacious_channels = Commands("audacious_channels", "Number of audio channels of current track.", "false")
functions.update({"audacious_channels": audacious_channels.command})

audacious_filename = Commands("audacious_filename", "Full path and filename of current track.", "false")
functions.update({"audacious_filename": audacious_filename.command})

audacious_frequency = Commands("audacious_frequency", "Sampling frequency of current track.", "false")
functions.update({"audacious_frequency": audacious_frequency.command})

audacious_length = Commands("audacious_length", "Total length of current track as MM:SS.", "false")
functions.update({"audacious_length": audacious_length.command})

audacious_length_seconds = Commands("audacious_length_seconds", "Total length of current track in seconds.", "false")
functions.update({"audacious_length_seconds": audacious_length_seconds.command})

audacious_main_volume = Commands("audacious_main_volume", "The current volume fetched from Audacious.", "false")
functions.update({"audacious_main_volume": audacious_main_volume.command})

audacious_playlist_length = Commands("audacious_playlist_length", "Number of tracks in playlist.", "false")
functions.update({"audacious_playlist_length": audacious_playlist_length.command})

audacious_playlist_position = Commands("audacious_playlist_position", "Playlist position of current track.", "false")
functions.update({"audacious_playlist_position": audacious_playlist_position.command})

audacious_position = Commands("audacious_position", "Position of current track (MM:SS).", "false")
functions.update({"audacious_position": audacious_position.command})

audacious_position_seconds = Commands("audacious_position_seconds", "Position of current track in seconds.", "false")
functions.update({"audacious_position_seconds": audacious_position_seconds.command})

audacious_status = Commands("audacious_status", "Player status (Playing/Paused/Stopped/Not running).", "false")
functions.update({"audacious_status": audacious_status.command})

audacious_title = Commands("audacious_title", "Title of current track with opitional maximum length specifier.", "true")
functions.update({"audacious_title": audacious_title.command})

battery = Commands("battery", "\
Battery status and remaining percentage capacity of ACPI or APM battery. \
ACPI battery number can be given as argument (default is BAT0).", "true")
functions.update({"battery": battery.command})

battery_bar = Commands("battery_bar", "\
Battery percentage remaining of ACPI battery in a bar. ACPI battery number \
can be given as argument (default is BAT0, use all to get the mean percentage \
remaining for all batteries).", "true")
functions.update({"battery_bar": battery_bar.command})

battery_percent = Commands("battery_percent", "\
Battery percentage remaining for ACPI battery. ACPI battery number can be given \
as argument (default is BAT0, use all to get the mean percentage remaining for \
all batteries).", "true")
functions.update({"battery_percent": battery_percent.command})

battery_short = Commands("battery_short", "\
Battery status and remaining percentage capacity of ACPI or APM battery. ACPI \
battery number can be given as argument (default is BAT0). This mode display a \
short status, which means that C is displayed instead of charging, D for \
discharging, F for full, N for not present, E for empty and U for unknown.", "true")
functions.update({"battery_short": battery_short.command})

battery_status = Commands("battery_status", "\
Battery status for ACPI battery. ACPI battery number can be given as \
argument (default is BAT0).", "true")
functions.update({"battery_status": battery_status.command})
functions.update({"battery_short": battery_short.command})

battery_time = Commands("battery_time", "\
Battery charge/discharge time remaining of ACPI battery. ACPI battery \
number can be given as argument (default is BAT0).", "true")
functions.update({"battery_time": battery_time.command})

blink = Commands("blink", "\
Let 'text_and_other_conky_vars' blink on and off.", "true")
functions.update({"blink": blink.command})

buffers = Commands("buffers", "\
Amount of memory buffered.", "false")
functions.update({"buffers": buffers.command})

cached = Commands("cached", "\
Amount of memory cached.", "false")
functions.update({"cached": cached.command})

cat = Commands("cat", "\
Reads a file and displays the contents in conky. This is useful if you \
have an independent process generating output that you want to include \
in conky.", "true")
functions.update({"cat": cat.command})

catp = Commands("catp", "\
Reads a file and displays the contents in conky. This is useful if you \
have an independent process generating output that you want to include \
in conky. This differs from $cat in that it parses the contents of the \
file, so you can insert things like ${color red}hi!${color} in your \
file and have it correctly parsed by Conky.", "true")
functions.update({"catp": catp.command})

cmdline_to_pid = Commands("cmdline_to_pid", "\
PID of the first process that has string in its commandline.", "true")
functions.update({"cmdline_to_pid": cmdline_to_pid.command})

cmus_aaa = Commands("cmus_aaa", "\
Print aaa status of cmus (all/artist/album).", "false")
functions.update({"cmus_aaa": cmus_aaa.command})

cmus_album = Commands("cmus_album", "\
Prints the album of the current cmus song.", "false")
functions.update({"cmus_album": cmus_album.command})

cmus_artist = Commands("cmus_artist", "\
Prints the artist of the current cmus song.", "false")
functions.update({"cmus_artist": cmus_artist.command})

cmus_curtime = Commands("cmus_curtime", "\
Prints the time of the current cmus song.", "false")
functions.update({"cmus_curtime": cmus_curtime.command})

cmus_file = Commands("cmus_file", "\
Prints the file name of the current cmus song.", "false")
functions.update({"cmus_file": cmus_file.command})

cmus_date = Commands("cmus_date", "\
Prints the date of the current cmus song.", "false")
functions.update({"cmus_date": cmus_date.command})

cmus_genre = Commands("cmus_genre", "\
Prints the genre of the current cmus song.", "false")
functions.update({"cmus_genre": cmus_genre.command})

cmus_percent = Commands("cmus_percent", "\
Prints the percent of the songs progress.", "false")
functions.update({"cmus_percent": cmus_percent.command})

cmus_progress = Commands("cmus_progress", "\
cmus' progress bar.", "true")
functions.update({"cmus_progress": cmus_progress.command})

cmus_random = Commands("cmus_random", "\
Random status of cmus (on/off).", "false")
functions.update({"cmus_random": cmus_random.command})

cmus_repeat = Commands("cmus_repeat", "\
Repeat status of cmus (song/all/off).", "false")
functions.update({"cmus_repeat": cmus_repeat.command})

cmus_state = Commands("cmus_state", "\
Current state of cmus (playing, paused, stopped etc).", "false")
functions.update({"cmus_state": cmus_state.command})

cmus_timeleft = Commands("cmus_timeleft", "\
Time left of the current cmus song.", "false")
functions.update({"cmus_timeleft": cmus_timeleft.command})

cmus_title = Commands("cmus_title", "\
Title of the current cmus song.", "false")
functions.update({"cmus_title": cmus_title.command})

cmus_totaltime = Commands("cmus_totaltime", "\
Print total length of time of the current cmus song.", "false")
functions.update({"cmus_totaltime": cmus_totaltime.command})

cmus_track = Commands("cmus_track", "\
Print track number of current cmus song.", "false")
functions.update({"cmus_track": cmus_track.command})

combine = Commands("combine", "\
Places the lines of var2 to the right of the lines of var1 separated \
by the chars that are put between var1 and var2. For example: \
${combine ${head /proc/cpuinfo 2} - ${head /proc/meminfo 1}} gives \
as output 'cpuinfo_line1 - meminfo_line1' on line 1 and \
'cpuinfo_line2 -' on line 2. $combine vars can also be nested \
to place more vars next to each other.", "true")
functions.update({"combine": combine.command})

conky_build_arch = Commands("conky_build_arch", "\
CPU architecture Conky was built for.", "false")
functions.update({"conky_build_arch": conky_build_arch.command})

conky_build_date = Commands("conky_build_date", "\
Date Conky was built.", "false")
functions.update({"conky_build_date": conky_build_date.command})

conky_version = Commands("conky_version", "\
Conky version.", "false")
functions.update({"conky_version": conky_version.command})

cpu = Commands("cpu", "\
CPU usage in percents. For SMP machines, the CPU number can be \
provided as an argument. ${cpu cpu0} is the total usage, and \
${cpu cpuX} (X >= 1) are individual CPUs.", "true")
functions.update({"cpu": cpu.command})

cpu_bar = Commands("cpu_bar", "\
Bar that shows CPU usage, height is bar's height in pixels. See \
$cpu for more info on SMP.", "true")
functions.update({"cpu_bar": cpu_bar.command})

cpu_gauge = Commands("cpu_gauge", "\
Elliptical gauge that shows CPU usage, height and width are gauge's \
vertical and horizontal axis respectively. See $cpu for more info \
on SMP.", "true")
functions.update({"cpu_gauge": cpu_gauge.command})

cpugraph = Commands("cpugraph", "\
CPU usage graph, with optional colours in hex, minus the #. See $cpu \
for more info on SMP. Uses a logarithmic scale (to see small numbers) \
when you use the -l switch. Takes the switch '-t' to use a temperature \
gradient, which makes the gradient values change depending on the \
amplitude of a particular graph value (try it and see).", "true")
functions.update({"cpugraph": cpugraph.command})

curl = Commands("curl", "\
Download data from URI using Curl at the specified interval. The interval \
may be a positive floating point value (0 is allowed), otherwise defaults \
to 15 minutes. Most useful when used in conjunction with Lua and the Lua \
API. This object is threaded, and once a thread is created it can't be \
explicitly destroyed. One thread will run for each URI specified. You can \
use any protocol that Curl supports.", "true")
functions.update({"curl": curl.command})

desktop = Commands("desktop", "\
Number of the desktop on which conky is running or the message 'Not running \
in X' if this is the case.", "false")
functions.update({"desktop": desktop.command})

desktop_name = Commands("desktop_name", "\
Name of the desktop on which conky is running or the message 'Not running \
in X' if this is the case.", "false")
functions.update({"desktop_name": desktop_name.command})

disk_protect = Commands("disk_protect", "\
Disk protection status, if supported (needs kernel-patch). Prints either \
'frozen' or 'free ' (note the padding).", "true")
functions.update({"disk_protect": disk_protect.command})

diskio = Commands("diskio", "\
Displays current disk IO. Device is optional, and takes the form of sda for \
/dev/sda. A block device label can be specified with label:foo and a block \
device partuuid can be specified with partuuid:40000000-01.", "true")
functions.update({"diskio": diskio.command})

diskio_read = Commands("diskio_read", "\
Displays current disk IO for reads. Device as in diskio.", "true")
functions.update({"diskio_read": diskio_read.command})

diskio_write = Commands("diskio_write", "\
Displays current disk IO for writes. Device as in diskio.", "true")
functions.update({"diskio_write": diskio_write.command})

diskiograph = Commands("diskiograph", "\
Disk IO graph, colours defined in hex, minus the #. If scale is non-zero, it \
becomes the scale for the graph. Uses a logarithmic scale (to see small numbers) \
when you use -l switch. Takes the switch '-t' to use a temperature gradient, \
which makes the gradient values change depending on the amplitude of a particular \
graph value (try it and see).", "true")
functions.update({"diskiograph": diskiograph.command})

diskiograph_read = Commands("diskiograph_read", "\
Disk IO graph for reads, colours defined in hex, minus the #. If scale is non-zero, \
it becomes the scale for the graph. Device as in diskio. Uses a logarithmic scale \
(to see small numbers) when you use -l switch. Takes the switch '-t' to use a \
temperature gradient, which makes the gradient values change depending on the \
amplitude of a particular graph value (try it and see).", "true")
functions.update({"diskiograph_read": diskiograph_read.command})

diskiograph_write = Commands("diskiograph_write", "\
Disk IO graph for writes, colours defined in hex, minus the #. If scale is non-zero, \
it becomes the scale for the graph. Device as in diskio. Uses a logarithmic scale (to \
see small numbers) when you use -l switch. Takes the switch '-t' to use a temperature \
gradient, which makes the gradient values change depending on the amplitude of a \
particular graph value (try it and see).", "true")
functions.update({"diskiograph_write": diskiograph_write.command})

distribution = Commands("distribution", "\
The name of the distribution. It could be that some of the untested distributions \
will show up wrong or as 'unknown', if that's the case post a bug on sourceforge, \
make sure it contains the name of your distribution, the contents of /proc/version \
and if there is a file that only exists on your distribution, also add the path of \
that file in the bug. If there is no such file, please add another way which we can\
 use to identify your distribution.", "false")
functions.update({"distribution": distribution.command})

downspeed = Commands("downspeed", "\
Download speed in suitable IEC units.", "true")
functions.update({"downspeed": downspeed.command})

downspeedf = Commands("downspeedf", "\
Download speed in KiB with one decimal.", "false")
functions.update({"downspeedf": downspeedf.command})

downspeedgraph = Commands("downspeedgraph", "\
Download speed graph, colours defined in hex, minus the #. If scale is non-zero, it \
becomes the scale for the graph. Uses a logarithmic scale (to see small numbers) \
when you use -l switch. Takes the switch '-t' to use a temperature gradient, which \
makes the gradient values change depending on the amplitude of a particular graph \
value (try it and see).", "true")
functions.update({"downspeedgraph": downspeedgraph.command})

draft_mails = Commands("draft_mails", """\
Number of mails marked as draft in the specified mailbox or mail spool if not. \
Only maildir type mailboxes are supported, mbox type will return -1.
else
Text to show if any of the above are not true.
endif
Ends an $if block.""", "true")
functions.update({"draft_mails": draft_mails.command})

entropy_avail = Commands("entropy_avail", "\
Current entropy available for crypto freaks.", "false")
functions.update({"entropy_avail": entropy_avail.command})

entropy_bar = Commands("entropy_bar", "\
Normalized bar of available entropy for crypto freaks.", "false")
functions.update({"entropy_bar": entropy_bar.command})

entropy_perc = Commands("entropy_perc", "\
Percentage of entropy available in comparison to the poolsize.", "false")
functions.update({"entropy_perc": entropy_perc.command})

entropy_poolsize = Commands("entropy_poolsize", "\
Total size of system entropy pool for crypto freaks.", "false")
functions.update({"entropy_poolsize": entropy_poolsize.command})

eval = Commands("eval", "\
Evaluates given string according to the rules of conky.text interpretation, i.e. \
parsing any contained text object specifications into their output, any occuring \
'$$' into a single '$' and so on. The output is then being parsed again.", 'true')
functions.update({"eval": eval.command})
# Exec can't be exec because it is a python function. . . so make special function to compensate
Exec = Commands("Exec", "\
Executes a shell command and displays the output in conky. Warning: this takes a \
lot more resources than other variables. I'd recommend coding wanted behaviour \
in C/C++ and posting a patch.", 'true')
functions.update({"Exec": Exec.command})

execbar = Commands("execbar", "\
Same as exec, except if the first value returned is a value between 0-100, it \
will use that number to draw a horizontal bar. The height and width parameters \
are optional, and default to the default_bar_height and default_bar_width \
config settings, respectively.", 'true')
functions.update({"execbar": execbar.command})
# leave off 8.3.102.0