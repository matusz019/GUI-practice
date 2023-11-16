import tkinter as tk
from datetime import datetime
import openpyxl
import os

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

        self.options = ["Squats", "Deadlifts", "Bench Press", "Weight", "Body Fat"]

        # Create widgets
        self.create_widgets()
        self.create_database()

    def create_widgets(self):
        # Create a label for exercise
        exerciseLabel = tk.Label(self.master, text="Exercise")
        exerciseLabel.grid(row=0, column=0, padx=10, pady=10)

        # Create a StringVar to store the selected option
        self.variable = tk.StringVar(self.master)
        self.variable.set("Option")  # Set the default option

        # Create an OptionMenu with multiple options
        option_menu = tk.OptionMenu(self.master, self.variable, *self.options )
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
            self.percentEntry.grid_forget()
            self.percentLabel.grid_forget()
            self.kgEntry.delete(0, tk.END)
            self.kgEntry.insert(tk.END, "Enter the weight")
            self.kgEntry.grid(row=1, column=0, padx=(10, 0))
            self.kgLabel.grid(row=1, column=1, sticky='W')
        elif selected_option == "Body Fat":
            self.kgEntry.grid_forget()
            self.kgLabel.grid_forget()
            self.percentEntry.delete(0, tk.END)
            self.percentEntry.insert(tk.END, "Enter body fat")
            self.percentEntry.grid(row=2, column=0, padx=(10, 0))
            self.percentLabel.grid(row=2, column=1, sticky='W')

    def create_database(self):
        # Get the current date
        current_date = datetime.now().strftime("%d-%m-%Y")

        # Define the file name
        file_name = "Gym_Data.xlsx"

        # Check if the file already exists
        if not os.path.exists(file_name):
            # Create a new Excel workbook
            workbook = openpyxl.Workbook()

            # Add a sheet with the current date as the name
            sheet = workbook.active
            sheet.title = current_date

            # Add "Date" in cell A1
            sheet['A1'] = 'Date'

            # Populate rows below A1 with items from the options list
            for idx, option in enumerate(self.options, start=2):
                sheet[f'A{idx}'] = option

            # Save the workbook with the current date as the file name
            workbook.save(file_name)

            # Save the workbook with the current date as the file name
            workbook.save(file_name)

            print(f"Database created: {file_name}")
        else:
            print(f"Database already exists: {file_name}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GymTrackerApp(root)
    root.mainloop()