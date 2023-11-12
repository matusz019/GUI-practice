from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()

        #configure main window
        self.title("Basic GUI Layout")
        self.maxsize(900, 600)
        
        left_frame = Frame(self, width=200, height=400, bg='grey')
        left_frame.grid(row=0, column=0, padx=10, pady=5)

        right_frame = Frame(self, width=650, height=400, bg='grey')
        right_frame.grid(row=0, column=1, padx=10, pady=5)

        # Create frames and labels in left_frame
        Label(left_frame, text="Original Image").grid(row=0, column=0, padx=5, pady=5)

        # Create tool bar frame
        tool_bar = Frame(left_frame, width=180, height=185)
        tool_bar.grid(row=2, column=0, padx=5, pady=5)

        # Example labels that serve as placeholders for other widgets
        Label(tool_bar, text="Tools", relief=RAISED).grid(row=0, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
        Label(tool_bar, text="Filters", relief=RAISED).grid(row=0, column=1, padx=5, pady=3, ipadx=10)

        # Example labels that could be displayed under the "Tool" menu
        Label(tool_bar, text="Select").grid(row=1, column=0, padx=5, pady=5)
        Label(tool_bar, text="Crop").grid(row=2, column=0, padx=5, pady=5)
        Label(tool_bar, text="Rotate & Flip").grid(row=3, column=0, padx=5, pady=5)
        Label(tool_bar, text="Resize").grid(row=4, column=0, padx=5, pady=5)
        Label(tool_bar, text="Exposure").grid(row=5, column=0, padx=5, pady=5)


if __name__ == "__main__":
  app = GUI()
  app.mainloop()