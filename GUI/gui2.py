from tkinter import *

#Label = an area widget that holds text and /or an image within a window

window = Tk()

label = Label(window, text="Hi, how are you!", 
              font=('Arial', 40,'bold'),
              fg='green',
              background='black',
              relief=RAISED,
              bd = 10,
              padx=20,
              pady=20)
label.pack()

window.mainloop()