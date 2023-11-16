import tkinter as tk

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
        # Create a label for exercise
        exerciseLabel = tk.Label(self.master, text="Exercise")
        exerciseLabel.grid(row=0, column=0, padx=10, pady=10)

        # Create a StringVar to store the selected option
        self.variable = tk.StringVar(self.master)
        self.variable.set("Option")  # Set the default option

        # Create an OptionMenu with multiple options
        option_menu = tk.OptionMenu(self.master, self.variable, "Squats", "Deadlifts", "Body Fat", "Bench Press", "Weight")
        option_menu.grid(row=0, column=1, padx=10, pady=10)

        # Set up a trace on the variable to call the update_entry function when the option changes
        self.variable.trace("w", self.update_entry)

        # Initialize Entry widget
        self.entry_var = tk.StringVar()

        # Initialize kgEntry and kgLabel as class attributes
        self.kgEntry = tk.Entry(self.master, width=20)
        self.kgLabel = tk.Label(self.master, text="kg")
        self.percentEntry = tk.Entry(self.master, width=20)
        self.percentLabel = tk.Label(self.master, text="%")

    def update_entry(self, *args):
        selected_option = self.variable.get()
        self.entry_var.set(f"Option chosen: {selected_option}")

        if selected_option in ("Squats", "Deadlifts", "Bench Press", "Weight"):

            

            self.kgEntry.delete(0, tk.END)
            self.kgEntry.insert(tk.END, "Enter the weight")
            self.kgEntry.grid(row=1, column=0, padx=(10, 0))
            self.kgLabel.grid(row=1, column=1, sticky='W')
        elif selected_option == "Body Fat":
            self.kgEntry.grid_forget()
            self.kgLabel.grid_forget()
            self.percentEntry.insert(tk.END, "Enter body fat")
            self.percentEntry.grid(row=2, column=0, padx=(10, 0))
            self.percentLabel.grid(row=2, column=1, sticky='W')

if __name__ == "__main__":
    root = tk.Tk()
    app = GymTrackerApp(root)
    root.mainloop()

