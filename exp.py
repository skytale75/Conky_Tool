import tkinter as tk
import tkinter.ttk as ttk
from tkcolorpicker import askcolor

root = tk.Tk()
style = ttk.Style(root)
style.theme_use('clam')

print(askcolor(('#FF0000'), root))
root.mainloop()