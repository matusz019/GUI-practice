from tkinter import *

root = Tk()

#setting up the root window
root.title("Login UI using Pack")
root.geometry("400x320")
root.maxsize(400, 320)
root.minsize(400,320)
root.config(bg="skyblue")

login = Label(root, text="Login", bg="#2176C1", fg='white', relief=RAISED)
login.pack(ipady=5, fill='x')
login.config(font=("Font", 30))  # change font and size of label


def checkInput():
    '''check that the username and password match'''
    usernm = "Username301"
    pswrd = "Passw0rd"
    entered_usernm = username_entry.get()  # get username from Entry widget
    entered_pswrd = password_entry.get()  # get password from Entry widget

    if (usernm == entered_usernm) and (pswrd == entered_pswrd):
        print("Hello!")
        root.destroy()  

    else:
        print("Login failed: Invalid username or password.")

def toggled():
    '''display a message to the terminal every time the check button
    is clicked'''
    print("The check button works.")

# Username Entry
username_frame = Frame(root, bg="#6FAFE7")
username_frame.pack()

Label(username_frame, text="Username", bg="#6FAFE7").pack(side='left', padx=5)

username_entry = Entry(username_frame, bd=3)
username_entry.pack(side='right')

# Password entry
password_frame = Frame(root, bg="#6FAFE7")
password_frame.pack()

Label(password_frame, text="Password", bg="#6FAFE7").pack(side='left', padx=7)

password_entry = Entry(password_frame, bd=3)
password_entry.pack(side='right')

# Create Go! Button

go_button = Button(root, text="GO!", command=checkInput, bg="#6FAFE7", width=15)

go_button.pack(pady=5)

# Remember me and forgot password
bottom_frame = Frame(root, bg="#6FAFE7")
bottom_frame.pack()

var = IntVar()

remember_me = Checkbutton(bottom_frame, text="Remember me", bg="#6FAFE7", command=toggled, variable=var)
remember_me.pack(side='left', padx=19)

# The forgot password Label is just a placeholder, has no function currently
forgot_pswrd = Label(bottom_frame, text="Forgot password?", bg="#6FAFE7")
forgot_pswrd.pack(side="right", padx=19)


root.mainloop()