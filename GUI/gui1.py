from tkinter import *

#window = server as a container to hold or contain these widgets
#widgets = GUI elements - buttons, textboxes, lables, images

window = Tk() #instantiate an instance of a window
window.geometry("420x420")
window.title("Python")
window.config(background="#feffb5")

icon = PhotoImage(file='image.png')
window.iconphoto(True, icon)

window.mainloop() #place window on computer screen, listen for the events