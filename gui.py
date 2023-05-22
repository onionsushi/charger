import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout


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
        button1 = QPushButton("Start Charging", self)
        button1.clicked.connect(lambda: self.button_click(1))
        button1.setFixedHeight(200)
        button2 = QPushButton("Button 2", self)
        button2.clicked.connect(lambda: self.button_click(2))
        button2.setFixedHeight(200)
        button3 = QPushButton("Button 3", self)
        button3.setFixedHeight(200)
        button3.clicked.connect(lambda: self.button_click(3))
        left_panel.addWidget(button1)
        left_panel.addWidget(button2)
        left_panel.addWidget(button3)

        # Create the right panel with labels
        right_panel = QVBoxLayout()
        self.label1 = QLabel("Label 1", self)
        self.label2 = QLabel("Label 2", self)
        self.label3 = QLabel("Label 3", self)
        right_panel.addWidget(self.label1)
        right_panel.addWidget(self.label2)
        right_panel.addWidget(self.label3)

        # Add the left and right panels to the main layout
        layout.addLayout(left_panel)
        layout.addLayout(right_panel)

        # Set the main layout for the window
        self.setLayout(layout)

    def button_click(self, button_num):
        label_text = f"Button {button_num} clicked!"
        if button_num == 1:
            self.label1.setText(label_text)
        elif button_num == 2:
            self.label2.setText(label_text)
        elif button_num == 3:
            self.label3.setText(label_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())