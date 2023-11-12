import tkinter as tk
from tkinter import ttk, messagebox

class GymTrackerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Gym Progress Tracker")
        self.master.geometry("400x300")

        # Exercise variables
        self.exercise_var = tk.StringVar()
        self.sets_var = tk.IntVar()
        self.reps_var = tk.IntVar()
        self.weight_var = tk.DoubleVar()

        # Create widgets
        self.create_widgets()




    def create_widgets(self):

        def update_entry(*args):
            selected_option = variable.get()
            entry_var.set(f"Option chosen: {selected_option}")

        # Create a label for exercise
        exerciseLabel = tk.Label(root, text="Exercise")
        exerciseLabel.grid(row=0, column=0, padx= 10, pady= 10)

        # Create a StringVar to store the selected option
        variable = tk.StringVar(root)
        variable.set("Option")  # Set the default option

        # Create an OptionMenu with three options
        option_menu = tk.OptionMenu(root, variable, "Squats", "Deadlifts", "Body Fat", "Bench Press", "Weight")
        option_menu.grid(row= 0, column=1,padx=10, pady=10)

        # Create an Entry widget
        entry_var = tk.StringVar()
        entry = tk.Entry(root, textvariable=entry_var, state='readonly', width=30)
        entry.grid(row= 1, column=1,padx=10, pady=150)

        # Set up a trace on the variable to call the update_entry function when the option changes
        variable.trace("w", update_entry)

        # Call the update_entry function to initialize the entry text
        update_entry()



if __name__ == "__main__":
    root = tk.Tk()
    app = GymTrackerApp(root)
    root.mainloop()