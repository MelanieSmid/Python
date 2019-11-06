# Tkinter
from tkinter import *

class my_frame(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.my_canvas = Canvas(width = 300, height = 200, bg = "blue")
        self.my_canvas.grid()
        self.my_canvas.create_rectangle(10, 10, 200, 100, fill = "pink")
        self.my_canvas.create_oval(10, 10, 200, 100, fill = "green")
        self.my_canvas.create_line(1, 1, 200, 200, arrow = "first")
        self.my_canvas.create_text(50, 50, text = "Hello World", width = 70, fill = "purple", anchor = "nw", justify = "center", font = ("Times", 16))
# now create a my_frame object and call on mainloop

frame01 = my_frame()
frame01.mainloop()
