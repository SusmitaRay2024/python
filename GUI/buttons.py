from tkinter import *

# buttons = you click it, then it does stuff

count = 1
def click():
    global count
    count+=1
    print(count)
    
window = Tk()

button = Button(window, 
                text = "Click me!",
                command=click,
                font = ("Comic Sans", 30),
                fg="red",
                bg="yellow",
                activeforeground="red",
                activebackground="black",
                state= ACTIVE)

button.pack()
window.mainloop()