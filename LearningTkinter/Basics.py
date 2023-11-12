from tkinter import *

class GymApp(Tk):
    def __init__(self):
        super().__init__()

        #configure main window
        self.title("Mattys Gym App")
        self.configure(bg="skyblue")

        #create frame wiget
        leftFrame= Frame(self)
        leftFrame.config(bg="white")
        leftFrame.grid(row=0,column=0, padx=10, pady=5)

        #create a frame within a frame
        tool_bar = Frame(leftFrame, width=180, height=185, bg="purple")
        tool_bar.grid(row=2, column=0, padx=5, pady=5)

        #label above toolbar
        Label(leftFrame,text="Track your progress").grid(row=1,column=0,padx=5,pady=5)
        


if __name__ == "__main__":
  app = GymApp()
  app.mainloop()
