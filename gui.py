import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout
from PyQt5.QtCore import QThread, pyqtSignal


class ProcessingThread(QThread):
    task_completed = pyqtSignal(str)

    def run(self):
        # Simulating a time-consuming task
        import time
        time.sleep(5)

        # Emitting a signal to indicate task completion
        self.task_completed.emit("Processing completed!")


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Set window properties
        self.setWindowTitle("Charger")
        self.setGeometry(100, 100, 300, 200)

        # Create a vertical layout for the window
        layout = QHBoxLayout()

        # Create the left panel with buttons
        left_panel = QVBoxLayout()
        self.button1 = QPushButton("Start Charging", self)
        self.button1.clicked.connect(self.start_processing)
        self.button1.setFixedHeight(200)

        left_panel.addWidget(self.button1)

        # Create the right panel with labels
        right_panel = QVBoxLayout()
        self.userLabel = QLabel("Label 1", self)
        self.BalanceLabel = QLabel("Label 2", self)
        right_panel.addWidget(self.userLabel)
        right_panel.addWidget(self.BalanceLabel)

        # Add the left and right panels to the main layout
        layout.addLayout(left_panel)
        layout.addLayout(right_panel)

        # Set the main layout for the window
        self.setLayout(layout)

    def start_processing(self):
        # Create and start the processing thread
        self.processing_thread = ProcessingThread()
        self.processing_thread.task_completed.connect(self.on_processing_completed)
        self.processing_thread.start()

        # Disable the button while processing

        self.button1.setEnabled(False)

    def on_processing_completed(self, message):
        # Update the label with the task completion message
        self.BalanceLabel.setText(message)

        # Re-enable the button
        self.button1.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())