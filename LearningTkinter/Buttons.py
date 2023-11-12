from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()

        def volumeUp():
            print("Volume increase +1")

        on = Button(self,text="ON")
        on.pack()

        off = Button(self,text="OFF", command=self.quit)
        off.pack()

        volume = Label(self, text="VOLUME")
        volume.pack()

        vol_up = Button(self, text="+", command=volumeUp)
        vol_up.pack()

        vol_down = Button(self, text="-")
        vol_down.pack()



if __name__ == "__main__":
  app = GUI()
  app.mainloop()