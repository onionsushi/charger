import sys
import typing
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from firestoreSnippet import *
import time

class ProcessingThread(QThread):
    deviceID = "GUIdevice-ProtoType"
    active : bool = False

    def __init__(self,userId = ""):
        super().__init__()
        self.userId = userId
        AddDevice("GUIdevice-ProtoType", "guiIPAddress")


    ClientLoaded = pyqtSignal(str)
    ClientEmptied = pyqtSignal(str)
    OnBalanceChange = pyqtSignal(str)
    active = False
      
    
    def run(self):
        self.userId = FindDevice(self.deviceID)[0]["CurrentUser"]
        print(self.userId)
        StartCharge("deviceId", self.userId)
        # Simulating a time-consuming task
            

        # Emitting a signal to indicate task completion
        self.ClientLoaded.emit("Processing completed!")
        self._run_task()
    
    def _run_task(self):
        while (self.active):
            print("charging!")
            time.sleep(2)
            res = BalanceChange(self.userId, 500)
            if not res:
                self.stop()
                self.active = res

    def stop(self):
        if (self.active):
            print("stop function worked!")
            finishCharge(self.deviceID)
            self.active = False
        self.ClientEmptied.emit("Charging halted!")
        
class MyWindow(QWidget):
    userId = ""
    processing_thread = None
    
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.processing_thread = ProcessingThread() 

        setConfigure("GUIdevice-ProtoType", "newipaddress") 
        userId = "cf51c330-6a3e-4c1b-9c59-98185712ce86"

        ModifyUserData(userId, {"Balance": 2000})
        StartCharge("GUIdevice-ProtoType", userId)
        self.processing_thread.ClientLoaded.connect(self.postLoadClient)
        self.processing_thread.ClientEmptied.connect(self.postEmptyClient)
        self.processing_thread.OnBalanceChange.connect(self.ChangeStatus)

    def init_ui(self):
        # Set window properties
        self.setWindowTitle("Charger")
        self.setGeometry(100, 100, 300, 200)

        # Create a vertical layout for the window
        layout = QHBoxLayout()

        # Create the left panel with buttons
        left_panel = QVBoxLayout()
        self.button1 = QPushButton("Start Charging", self)
        self.button1.clicked.connect(self.startLoadClient)
        self.button1.setFixedHeight(200)

        self.button2 = QPushButton("Stop Charging", self)
        self.button2.clicked.connect(self.startEmptyClient)
        self.button2.setFixedHeight(200)
        self.button2.setEnabled(False)

        left_panel.addWidget(self.button1)
        left_panel.addWidget(self.button2)


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

    def ChangeStatus(self, message):
        self.BalanceLabel.setText(message)

    def startLoadClient(self):
        # Create and start the processing thread
        self.processing_thread.active = True
        
        self.processing_thread.start()

        # Disable the button while processing

        self.button1.setEnabled(False)

    def postLoadClient(self, message):
        # Update the label with the task completion message
        self.BalanceLabel.setText(message)


        # Re-enable the button
        self.button1.setEnabled(False)
        self.button2.setEnabled(True)
        

    def startEmptyClient(self):
        print("shutting down")

        self.button2.setEnabled(False)
        self.processing_thread.active = False
        self.processing_thread.stop()
        

    
    def postEmptyClient(self, message):
        print("PostEmpty triggered!")
        
        self.button1.setEnabled(True)
        self.button2.setEnabled(False)
        self.BalanceLabel.setText(message)

    

if __name__ == '__main__':
    ''' Make MyWindow full screen with pyqt5'''
    app = QApplication(sys.argv)
    screen_resolution = app.desktop().screenGeometry()
    width, height = screen_resolution.width(), screen_resolution.height()
    window = MyWindow()
    '''set window size'''
    window.resize(width, height)
    window.show()
    sys.exit(app.exec_())

    # app = QApplication(sys.argv)
    # window = MyWindow()
    # window.show()
    # sys.exit(app.exec_())