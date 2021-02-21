from tkinter import Button, Tk
from PIL import ImageTk ,Image

base = Tk()
base.title('Start Button')

img=ImageTk.PhotoImage(Image.open ("/home/mike/Conky_Tool/button.png"))
lab=Button(image=img, text="fuck")
lab.pack()

button=Button(base,text='exit',command=base.quit)
button.pack()
base.mainloop()