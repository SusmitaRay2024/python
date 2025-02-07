from tkinter import *

def create_window():
    new_window = Tk()
    
    
window = Tk()

Button(window, text="Create new window",
       command = create_window).pack()

window.mainloop()