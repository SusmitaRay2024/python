from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pymysql

def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmEntry.delete(0,END)
    check.set(0)
    

def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmEntry.get()=='':
        messagebox.showerror('Error', 'All Fields are Required')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error', 'Password Mismatch')
    elif check.get()==0:
        messagebox.showerror('Error', 'Please Accept Terms and Conditions')
    else:
        try:
            con= pymysql.connect(host='localhost', user='root', password='Hello5@123' )
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue, Please Try Again')
            return
        try:
            query='create database userdata'
            mycursor.execute(query)
            query='use userdata'
            mycursor.execute(query)
            query='create table data(id int auto_increment primary key not null, email varchar(50), username varchar(100), password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')
        
        query='select * from data where username=%s'
        mycursor.execute(query,(usernameEntry.get()))
        
        row=mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error', 'Username Already Exists')
        else:
            query ='insert into data(email,username,password) values(%s,%s,%s)'
            mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
            con.commit()
            con.close()  
            messagebox.showinfo('Success', 'Registration is successful')
            clear()
            signupWindow.destroy()
            import signin
            
def login_page():
    signupWindow.destroy()
    import signin

signupWindow = Tk()
signupWindow.title('Signup Page')
signupWindow.resizable(False, False)
background = (ImageTk.PhotoImage(file="C:/Handson/python/gitcodeforpython/GUI/loginsignup/bg.png"))

bgLabel = Label(signupWindow, image=background)
bgLabel.grid()

frame = Frame(signupWindow, bg='white')
frame.place(x=556, y=97)

heading= Label(frame,text='CREATE AN ACCOUNT', font=('Microsoft Yahei UI Light',18,'bold')
               ,bg='white', fg='grey')
heading.grid(row=0, column=0, padx=40, pady=10)



emailLabel= Label(frame, text='Email', font=('Microsoft Yahei UI Light',10,'bold')
               ,bg='white', fg='grey')
emailLabel.grid(row=1, column=0, sticky='w', padx=55, pady=(10,0))

emailEntry=Entry(frame, width=30, font=('Microsoft Yahei UI Light',10,'bold'),
                 fg='white', bg='grey' )
emailEntry.grid(row=2, column=0, sticky='w', padx=55)


usernameLabel= Label(frame, text='Username', font=('Microsoft Yahei UI Light',10,'bold')
               ,bg='white', fg='grey')
usernameLabel.grid(row=3, column=0, sticky='w', padx=55, pady=(10,0))

usernameEntry=Entry(frame, width=30, font=('Microsoft Yahei UI Light',10,'bold'),
                 fg='white', bg='grey' )
usernameEntry.grid(row=4, column=0, sticky='w', padx=55)


passwordLabel= Label(frame, text='Password', font=('Microsoft Yahei UI Light',10,'bold')
               ,bg='white', fg='grey')
passwordLabel.grid(row=5, column=0, sticky='w', padx=55, pady=(10,0))

passwordEntry=Entry(frame, width=30, font=('Microsoft Yahei UI Light',10,'bold'),
                 fg='white', bg='grey' )
passwordEntry.grid(row=6, column=0, sticky='w', padx=55)


confirmLabel= Label(frame, text='Confirm Password', font=('Microsoft Yahei UI Light',10,'bold')
               ,bg='white', fg='grey')
confirmLabel.grid(row=7, column=0, sticky='w', padx=55, pady=(10,0))

confirmEntry=Entry(frame, width=30, font=('Microsoft Yahei UI Light',10,'bold'),
                 fg='white', bg='grey' )
confirmEntry.grid(row=8, column=0, sticky='w', padx=55)

check = IntVar()
termsandconditions = Checkbutton(frame, 
                                 text='I agree to the Terms & Conditions',  # Add `text=`
                                 font=('Microsoft YaHei UI Light', 9, 'bold'), 
                                 fg='grey', bg='white', activebackground='white', activeforeground='grey', 
                                 cursor='hand2', variable=check)
termsandconditions.grid(row=9,column=0, pady=10, padx=15)


signupButton=Button(frame,text='Signup', 
                   font=('Open Sans',16,'bold'),
                   fg='white', bg='grey',
                   activebackground='grey',
                   activeforeground='white',
                   cursor='hand2', bd=0, width=17, command=connect_database)
signupButton.grid(row=10, column=0, pady=10)


alreadyaccount=Label(frame, text="Don't have an account?", 
              font=('Open Sans',9,'bold'), bg='white', fg='grey')
alreadyaccount.grid(row=11, column=0, sticky='w', padx=65, pady=10)

loginButton=Button(frame,text='Log in', 
                   font=('OpenSans',9,'bold underline'),
                   fg='blue', bg='white',
                   activebackground='grey',
                   activeforeground='blue',
                   cursor='hand2', bd=0, command=login_page)
loginButton.place(x=200, y=403)



signupWindow.mainloop()