from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QLineEdit, QPushButton, QVBoxLayout, QWidget

class GymTracker(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Gym Progress Tracker")
        self.setGeometry(100, 100, 400, 300)  # x, y, width, height

        # Create a central widget and set the layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a layout for the central widget
        layout = QVBoxLayout(central_widget)

        # Create a label
        label = QLabel("Gym Progress Tracker", self)

        # Create a dropdown menu for exercises
        exercise_label = QLabel("Select Exercise:", self)
        self.exercise_combo = QComboBox(self)
        self.exercise_combo.addItems(["Bench Press", "Squat", "Deadlift", "Shoulder Press", "Other"])
        self.exercise_combo.currentIndexChanged.connect(self.display_info)

        # Create input fields
        sets_label = QLabel("Sets:", self)
        self.sets_input = QLineEdit(self)
        reps_label = QLabel("Repetitions:", self)
        self.reps_input = QLineEdit(self)
        weight_label = QLabel("Weight (kg):", self)
        self.weight_input = QLineEdit(self)

        # Create a button to submit the progress
        submit_button = QPushButton("Submit Progress", self)
        submit_button.clicked.connect(self.submit_progress)

        # Create a label to display exercise details
        self.details_label = QLabel(self)

        # Add widgets to the layout
        layout.addWidget(label)
        layout.addWidget(exercise_label)
        layout.addWidget(self.exercise_combo)
        layout.addWidget(sets_label)
        layout.addWidget(self.sets_input)
        layout.addWidget(reps_label)
        layout.addWidget(self.reps_input)
        layout.addWidget(weight_label)
        layout.addWidget(self.weight_input)
        layout.addWidget(submit_button)
        layout.addWidget(self.details_label)

    def display_info(self):
        selected_exercise = self.exercise_combo.currentText()
        self.details_label.setText(f"Details for {selected_exercise}: Sets, Reps, Weight")

    def submit_progress(self):
        exercise = self.exercise_combo.currentText()
        sets = self.sets_input.text()
        reps = self.reps_input.text()
        weight = self.weight_input.text()

        progress_info = f"Progress submitted for {exercise}: {sets} sets, {reps} reps, {weight} kg"
        self.details_label.setText(progress_info)


if __name__ == "__main__":
    app = QApplication([])  # Create the application instance
    tracker = GymTracker()  # Create an instance of your QMainWindow
    tracker.show()  # Display the window
    app.exec()  # Start the application event loop
