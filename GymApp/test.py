import tkinter as tk

def update_entry(*args):
    selected_option = variable.get()
    entry_var.set(f"Option chosen: {selected_option}")

root = tk.Tk()
root.title("Tkinter OptionMenu Example")

# Create a StringVar to store the selected option
variable = tk.StringVar(root)
variable.set("Option 1")  # Set the default option

# Create an OptionMenu with three options
option_menu = tk.OptionMenu(root, variable, "Option 1", "Option 2", "Option 3")
option_menu.pack(pady=10)

# Create an Entry widget
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, state='readonly', width=30)
entry.pack(pady=10)

# Set up a trace on the variable to call the update_entry function when the option changes
variable.trace("w", update_entry)

# Call the update_entry function to initialize the entry text
update_entry()

root.mainloop()