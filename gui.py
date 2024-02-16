import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton, QLineEdit, QTextEdit
from PyQt5.QtGui import QIcon
import commands

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Palworld Manager")
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setGeometry(300, 300, 400, 350)  # Increased height
        self.setStyleSheet('background-color: #e6f5e6; color: #333; border-radius: 10px;')

        # Layout
        layout = QVBoxLayout()
        layout.setSpacing(10)  # Adjusting spacing between widgets

        # Labels
        lbl_ip_ports = QLabel("IP:")
        lbl_ip_ports.setStyleSheet("color: #005580;")  # Darker blue text color
        lbl_admin_password = QLabel("Admin Password:")
        lbl_admin_password.setStyleSheet("color: #005580;")  # Darker blue text color
        self.lbl_additional_input = QLabel("Additional Input:")
        self.lbl_additional_input.setStyleSheet("color: #005580;")  # Darker blue text color

        # Input Fields
        self.input_ip_ports = QLineEdit()
        self.input_ip_ports.setStyleSheet("background-color: white; border-radius: 5px;")
        self.input_ip_ports.setPlaceholderText("0:0:0:0")  # Placeholder text for IP and Ports
        self.input_admin_password = QLineEdit()
        self.input_admin_password.setStyleSheet("background-color: white; border-radius: 5px;")
        self.input_admin_password.setPlaceholderText("Enter admin password")  # Placeholder text for Admin Password

        # Dropdown Menu
        self.dropdown_menu = QComboBox()
        self.dropdown_menu.setStyleSheet(
            """
            QComboBox {
                background-color: white; 
                border-radius: 5px; 
                padding: 3px;
                border: 1px solid #005580; /* Darker blue border */
            }
            """
        )  # Set background color of the dropdown menu
        
        self.dropdown_menu.addItem("Info")
        self.dropdown_menu.addItem("Broadcast") #needs aditional
        self.dropdown_menu.addItem("Shutdown") #needs add
        self.dropdown_menu.addItem("Exit") 

        self.dropdown_menu.addItem("Kick player") #needs add
        self.dropdown_menu.addItem("Show Players")
        self.dropdown_menu.addItem("Save")

        self.dropdown_menu.currentIndexChanged.connect(self.toggle_additional_input)  # Connect dropdown signal to function

        # Additional Input Field
        self.input_additional = QLineEdit()
        self.input_additional.setStyleSheet("background-color: white; border-radius: 5px;")
        self.input_additional.setPlaceholderText("Additional input goes here...")  # Placeholder text for Additional Input
        self.input_additional.hide()  # Initially hide additional input field
        self.lbl_additional_input.hide()  # Hide label for additional input

        # Send Button
        self.send_button = QPushButton("Send")
        self.send_button.setStyleSheet(
            """
            QPushButton {
                background-color: #4caf50; 
                color: white; 
                border-radius: 5px;
            }
            QPushButton:pressed {
                background-color: #357a38; /* darker green */
                border-style: inset;
            }
            """
        )
        self.send_button.setFixedHeight(40)  # Setting the fixed height of the send button
        self.send_button.clicked.connect(self.on_send_clicked)  # Connect send button signal to function

        # Console Output
        self.console_output = QTextEdit()
        self.console_output.setStyleSheet("background-color: black; color: white; border-radius: 10px;")
        self.console_output.setReadOnly(True)  # Make it read-only

        # Adding Widgets to Layout
        layout.addWidget(lbl_ip_ports)
        layout.addWidget(self.input_ip_ports)
        layout.addWidget(lbl_admin_password)
        layout.addWidget(self.input_admin_password)
        layout.addWidget(self.dropdown_menu)
        layout.addWidget(self.lbl_additional_input)
        layout.addWidget(self.input_additional)
        layout.addWidget(self.send_button)
        layout.addWidget(self.console_output)

        # Set Layout
        self.setLayout(layout)

    def toggle_additional_input(self, index):
        """Toggle visibility of additional input field based on selected option"""
        if (index == 1 or index == 2 or index == 4):  # Option 1 selected
            self.input_additional.show()
            self.lbl_additional_input
            if (index == 1): #Broadcast Message
                self.lbl_additional_input.setText("Message to send")
                self.input_additional.setPlaceholderText("Message goes here")
            if (index == 2):
                self.lbl_additional_input.setText("Shutdown time and message to send")
                self.input_additional.setPlaceholderText("Add a space between time and message")
            if (index == 3):
                self.lbl_additional_input.setText("Player to be Kicked")
                self.input_additional.setPlaceholderText("Player SteamID")

            self.lbl_additional_input.show()
        else:
            self.input_additional.hide()
            self.lbl_additional_input.hide()

    def on_send_clicked(self):
        
        """Function to be executed when the Send button is clicked"""
        ip = self.input_ip_ports.text()
        password = self.input_admin_password.text()
        addit = self.input_additional.text()
        print(self.dropdown_menu.itemText)
        cmnd = self.dropdown_menu.currentIndex()

        newCommand = commands.commands(ip, password, addit, cmnd)
        
        newCommand.commandSwitch()

        # Do something with the inputs, e.g., print them to the console output
        self.console_output.append(f"IP and Ports: {ip}")
        #self.console_output.append(f"Admin Password: {password}")
        self.console_output.append(f"Returned Response: {newCommand.response}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
