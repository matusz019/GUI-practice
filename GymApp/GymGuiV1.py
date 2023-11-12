
import tkinter as tk
from tkinter import ttk, messagebox

class GymTrackerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Gym Progress Tracker")
        self.master.geometry("400x250")

        # Exercise variables
        self.exercise_var = tk.StringVar()
        self.sets_var = tk.IntVar()
        self.reps_var = tk.IntVar()
        self.weight_var = tk.DoubleVar()

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure("TLabel", padding=10, font=('Arial', 12))
        style.configure("TEntry", padding=10, font=('Arial', 12))
        style.configure("TButton", padding=10, font=('Arial', 12))

        # Exercise entry
        exercise_label = ttk.Label(self.master, text="Exercise:")
        exercise_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        variable = tk.StringVar(root)
        variable.set("Option 1")

        exercise = tk.OptionMenu(root, variable, "Option 1", "Option 2", "Option 3")        
        exercise.menu = tk.Menu(exercise, tearoff=0)
        exercise["menu"] = exercise.menu

        # choices in exercise dropdown menu
        exercise.grid(row=0, column=1, padx=10, pady=10)

        # Sets entry
        sets_label = ttk.Label(self.master, text="Sets:")
        sets_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        sets_entry = ttk.Entry(self.master, textvariable=self.sets_var, width=5)
        sets_entry.grid(row=1, column=1, padx=10, pady=10)

        # Reps entry
        reps_label = ttk.Label(self.master, text="Reps:")
        reps_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        reps_entry = ttk.Entry(self.master, textvariable=self.reps_var, width=5)
        reps_entry.grid(row=2, column=1, padx=10, pady=10)

        # Weight entry
        weight_label = ttk.Label(self.master, text="Weight (kg):")
        weight_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

        weight_entry = ttk.Entry(self.master, textvariable=self.weight_var, width=10)
        weight_entry.grid(row=3, column=1, padx=10, pady=10)

        # Log button
        log_button = ttk.Button(self.master, text="Log Exercise", command=self.log_exercise)
        log_button.grid(row=4, column=0, columnspan=2, pady=20)

    def log_exercise(self):
        exercise = self.exercise_var.get()
        sets = self.sets_var.get()
        reps = self.reps_var.get()
        weight = self.weight_var.get()

        if not exercise or sets == 0 or reps == 0 or weight == 0.0:
            messagebox.showwarning("Incomplete Information", "Please fill in all fields.")
        else:
            log_message = f"Exercise: {exercise}\nSets: {sets}\nReps: {reps}\nWeight: {weight} kg"
            messagebox.showinfo("Exercise Logged", log_message)

            # Optionally, you can save the log data to a file or database.

if __name__ == "__main__":
    root = tk.Tk()
    app = GymTrackerApp(root)
    root.mainloop()

