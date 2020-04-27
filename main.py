from ct_gui import Notebook
from ct_fun import conky_stuff
from ct_mod import *


cs = conky_stuff
nb = Notebook('Conky Tool (in progress)')
com = Notebook

nb.create_widgets('Conky Editor')
conky_command()
nb.run()