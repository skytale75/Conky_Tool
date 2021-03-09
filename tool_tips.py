import tkinter as tk


class CreateToolTip(object):
    '''
    create a tooltip for a given widget
    '''
    def __init__(self, widget, text='widget info', text_size = 14):
        self.widget = widget
        self.text = text
        self.text_size = text_size
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.close)
        self.widget.bind("<F7>", self.close2)

        self.toggle=0

    def enter(self, event=None):
        if self.toggle == 0:
            x = y = 0
            x, y, cx, cy = self.widget.bbox("insert")
            x += self.widget.winfo_rootx() + 25
            y += self.widget.winfo_rooty() + 20
            # creates a toplevel window
            self.tw = tk.Toplevel(self.widget)
            # Leaves only the label and removes the app window
            self.tw.wm_overrideredirect(True)
            self.tw.wm_geometry("+%d+%d" % (x, y))
            label = tk.Label(self.tw, text=self.text, justify='left',
                        background='#FFFFE0', relief='solid', borderwidth=1,
                        font=("times", self.text_size, "normal"))
            label.pack(ipadx=1)
            toggle=1

    def close(self, event=None):
        if self.tw:
            self.tw.destroy()

    def close2(self, event=None):
        self.toggle=0
        if self.tw:
            self.tw.destroy()

# testing ...
if __name__ == '__main__':
    root = tk.Tk()

    # btn1 = tk.Button(root, text="button 1")
    # btn1.pack(padx=10, pady=5)
    # button1_ttp = CreateToolTip(btn1, "mouse is over button 1")

    # btn2 = tk.Button(root, text="button 2")
    # btn2.pack(padx=10, pady=5)
    # button2_ttp = CreateToolTip(btn2, "mouse is over button 2")

    # root.mainloop()