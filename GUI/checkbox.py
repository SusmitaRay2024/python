from tkinter import *

def display():
    if(x.get()==1):
        print("You Agree!")
    else:
        print("You Don't Agree!")

window = Tk()

x = IntVar()

check_button = Checkbutton(window,
                           text = "I agree to something!",
                           variable = x,
                           onvalue=1,
                           offvalue=0,
                           command= display,
                           font=('Arial', 20),
                           fg="green",
                           bg="black",
                           activeforeground='green',
                           activebackground='blue')

check_button.pack()

window.mainloop()