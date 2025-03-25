from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pymysql

#Functionality Part

def forget_pass():
    def change_password():
        if user_entry.get()=='' or newpass_entry.get()=='' or confirmpass_entry.get()=='':
            messagebox.showerror('Error', 'All Fields Are Required!', parent=window)
        elif newpass_entry.get()!=confirmpass_entry.get():
            messagebox.showerror('Error', 'Password and Confirm Password are not Matching!', parent=window)
        else: 
            con= pymysql.connect(host='localhost', user='root', password='Hello5@123', database='userdata' )
            mycursor=con.cursor()
            query = 'select * from data where username=%s'
            mycursor.execute(query,(user_entry.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error', 'Incorrect Username', parent=window)
            else:
                query='update data set password=%s where username=%s'
                mycursor.execute(query,(newpass_entry.get(), user_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Password is reset, please login with new password', parent=window)
                window.destroy()
            
    window= Toplevel()
    window.title('Change Password')
    
    bgPic = ImageTk.PhotoImage(file='bg.png')
    bglabel = Label(window, image=bgPic)
    bglabel.grid()
    
    heading_label = Label(window, text='RESET PASSWORD', font=('arial', 18, 'bold'),
                          bg='white', fg='SlateBlue3')
    heading_label.place(x=635, y=120)
    
    userLabel = Label(window, text='Username', font=('arial', 12, 'bold'),
                          bg='white', fg='SlateBlue1')
    userLabel.place(x=620, y=200)
    
    user_entry = Entry(window, width=25, fg='SlateBlue3', font=('arial', 11, 'bold'), bd=0)
    user_entry.place(x=620, y=230)
    
    Frame(window, width=250, height=2, bg='SlateBlue1').place(x=620, y=250)
    
    passwordLabel = Label(window, text='New Password', font=('arial', 12, 'bold'),
                          bg='white', fg='SlateBlue1')
    passwordLabel.place(x=620, y=280)
    
    newpass_entry = Entry(window, width=25, fg='SlateBlue3', font=('arial', 11, 'bold'), bd=0)
    newpass_entry.place(x=620, y=310)
    
    Frame(window, width=250, height=2, bg='SlateBlue1').place(x=620, y=330)
    
    confirmpassLabel = Label(window, text='Confirm Password', font=('arial', 12, 'bold'),
                          bg='white', fg='SlateBlue1')
    confirmpassLabel.place(x=620, y=360)
    
    confirmpass_entry = Entry(window, width=25, fg='SlateBlue3', font=('arial', 11, 'bold'), bd=0)
    confirmpass_entry.place(x=620, y=390)
    
    Frame(window, width=250, height=2, bg='SlateBlue1').place(x=620, y=410)
    
    submitButton = Button(window, text='Submit', bd=0, bg='SlateBlue3', fg= 'White', font=('Open Sans', '16', 'bold'), 
                          width=19, cursor='hand2', activebackground='SlateBlue1', activeforeground='white',
                          command=change_password)
    submitButton.place(x=620, y=460)
    
    window.mainloop()

def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error', 'All Fields Are Required')
    else:
        try:
            con= pymysql.connect(host='localhost', user='root', password='Hello5@123')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection is not established try again')
            return
        query='use userdata'
        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error', 'Invalid username or password')
        else:
            messagebox.showinfo('Welcome','Login is successful')
        
        
def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)

def hide():
    openeye.config(file='closeeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)
    
def show():
    openeye.config(file='C:/Handson/python/gitcodeforpython/GUI/loginsignup/openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)
    
def signup_page():
    loginWindow.destroy()
    import signup

#GUI Part
loginWindow=Tk()
loginWindow.geometry('998x660+50+50')
loginWindow.resizable(0,0)
loginWindow.title('Login Page')
photo = (ImageTk.PhotoImage(file="C:/Handson/python/gitcodeforpython/GUI/loginsignup/bg.png"))


bgLabel = Label(loginWindow, image=photo)
bgLabel.place(x=0,y=0)


heading= Label(loginWindow,text='USER LOGIN', font=('Microsoft Yahei UI Light',23,'bold')
               ,bg='white', fg='grey')
heading.place(x=635, y=120)

usernameEntry=Entry(loginWindow, width=25, font=('Microsoft Yahei UI Light',11,'bold'), bd=0, fg='grey')
usernameEntry.place(x=620, y=200)
usernameEntry.insert(0, 'Username')

usernameEntry.bind('<FocusIn>',user_enter)

Frame(loginWindow,width=230,height=2, bg='grey').place(x=620, y=222)

passwordEntry=Entry(loginWindow, width=25, font=('Microsoft Yahei UI Light',11,'bold'), bd=0, fg='grey')
passwordEntry.place(x=620, y=260)
passwordEntry.insert(0, 'Password')

passwordEntry.bind('<FocusIn>',password_enter)

Frame(loginWindow,width=230,height=2, bg='grey').place(x=620, y=282)

openeye=PhotoImage(file="C:/Handson/python/gitcodeforpython/GUI/loginsignup/openeye.png")
eyeButton=Button(loginWindow, image=openeye, 
                 width=20, height=17, 
                 bd=0, bg='white', 
                 activebackground='white', 
                 cursor='hand2', command=hide)
eyeButton.place(x=822, y=263)

forgetButton=Button(loginWindow, text='Forgot Password?',  
                 bd=0, bg='white', 
                 activebackground='white', 
                 cursor='hand2', font=('Microsoft Yahei UI Light',9,'bold'), 
                 fg='grey',
                 activeforeground='grey', command=forget_pass )
forgetButton.place(x=725, y=290)

loginButton=Button(loginWindow,text='Login', 
                   font=('OpenSans',16,'bold'),
                   fg='white', bg='grey',
                   activebackground='grey',
                   activeforeground='white',
                   cursor='hand2', bd=0, width=17, command=login_user)
loginButton.place(x=620, y=350)

orLabel=Label(loginWindow, text='--------------OR-------------', 
              font=('Open Sans',16), fg='grey', bg='white')
orLabel.place(x=620, y=400)

facebook_logo=PhotoImage(file="C:/Handson/python/gitcodeforpython/GUI/loginsignup/facebook.png")
fbLabel=Label(loginWindow, image=facebook_logo, bg='white' )
fbLabel.place(x=665, y=440)

google_logo=PhotoImage(file="C:/Handson/python/gitcodeforpython/GUI/loginsignup/google.png")
googleLabel=Label(loginWindow, image=google_logo, bg='white' )
googleLabel.place(x=715, y=440)

twitter_logo=PhotoImage(file="C:/Handson/python/gitcodeforpython/GUI/loginsignup/twitter.png")
twitterLabel=Label(loginWindow, image=twitter_logo, bg='white' )
twitterLabel.place(x=765, y=440)

signupLabel=Label(loginWindow, text='Dont have an account?', 
              font=('Open Sans',9,'bold'), bg='white', fg='grey')
signupLabel.place(x=610, y=500)

newaccountButton=Button(loginWindow,text='Create new one', 
                   font=('OpenSans',9,'bold underline'),
                   fg='blue', bg='white',
                   activebackground='grey',
                   activeforeground='blue',
                   cursor='hand2', bd=0, command=signup_page)
newaccountButton.place(x=750, y=500)






loginWindow.mainloop()
