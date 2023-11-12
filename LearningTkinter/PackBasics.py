from tkinter import *
root = Tk()
root.title("using pack")
root.geometry("300x100") #Set starting size of window
root.config(bg="skyblue")

#example of how ot arrange Button using pack

button1 = Button(root, text="Click me!")
button1.pack(side="left",padx=10)

#example how to arrange labels using pack
label1 = Label(root, text="Read me", bg="skyblue")
label1.pack(side="right")
label2 = Label(root, text="Hello", bg="purple")
label2.pack(side="right")

def toggled():
    '''display a message to the terminal every time the check button
    is clicked'''
    print("The check button works.")

# Example of how to arrange Checkbutton widget using pack
var = IntVar()  # Variable to check if checkbox is clicked, or not
check = Checkbutton(root, text="Click me", bg="skyblue", command=toggled, variable=var)
check.pack(side="bottom")

root.mainloop()