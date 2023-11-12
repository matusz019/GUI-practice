from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox, QLineEdit, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt

class GymTrackerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gym Progress Tracker")
        self.setGeometry(100, 100, 400, 250)

        # Exercise variables
        self.exercise_var = None  # You can add these as needed
        self.sets_var = None
        self.reps_var = None
        self.weight_var = None

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        def update_entry(index):
            selected_option = exercise_combobox.currentText()
            entry_line_edit.setText(f"Option chosen: {selected_option}")

        # Create a ComboBox with three options
        exercise_combobox = QComboBox(self)
        exercise_combobox.addItems(["Squats", "Deadlifts", "Body Fat"])
        exercise_combobox.setCurrentText("Hello")  # Set the default option
        exercise_combobox.currentIndexChanged.connect(update_entry)
        layout.addWidget(exercise_combobox)

        # Create a LineEdit widget
        entry_line_edit = QLineEdit(self)
        entry_line_edit.setReadOnly(True)
        layout.addWidget(entry_line_edit)

        # Call the update_entry function to initialize the entry text
        update_entry(0)

if __name__ == "__main__":
    app = QApplication([])
    window = GymTrackerApp()
    window.show()
    app.exec()
