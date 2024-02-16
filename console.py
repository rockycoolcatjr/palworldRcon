import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLabel, QLineEdit, QTextEdit, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class StyledGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Create widgets
        ip_label = QLabel('IP:')
        self.ip_entry = QLineEdit()
        self.stylize_entry(self.ip_entry)

        port_label = QLabel('Port:')
        self.port_entry = QLineEdit()
        self.stylize_entry(self.port_entry)

        password_label = QLabel('Password:')
        self.password_entry = QLineEdit()
        self.stylize_entry(self.password_entry)

        command_label = QLabel('Command:')
        self.command_entry = QLineEdit()
        self.stylize_entry(self.command_entry)

        console_output_label = QLabel('Console Output:')
        self.console_output = QTextEdit()
        self.console_output.setReadOnly(True)
        self.console_output.setStyleSheet(
            'QTextEdit {border: 2px solid #4CAF50; border-radius: 4px; padding: 2px; background: #101010; color: white;}'  # Close to black
            'QScrollBar:vertical {border: 2px solid #4CAF50; background: transparent; width: 16px; margin: 0px 4px 0px 4px;}'
            'QScrollBar::handle:vertical {background: #FF0000; border-radius: 8px; min-height: 30px;}'
            'QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {background: white;}'
            'QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {background: transparent;}'
        )

        send_button = QPushButton('Send')
        send_button.clicked.connect(self.send_command)
        send_button.setStyleSheet('QPushButton {background-color: #4CAF50; color: white; border: 2px solid #4CAF50; border-radius: 4px;}')

        # Layout
        layout = QFormLayout()
        layout.addRow(ip_label, self.ip_entry)
        layout.addRow(port_label, self.port_entry)
        layout.addRow(password_label, self.password_entry)
        layout.addRow(command_label, self.command_entry)
        layout.addRow(console_output_label, self.console_output)
        layout.addRow(send_button)

        self.setLayout(layout)

        # Set up the main window
        self.setWindowTitle('Palworld Manager')
        self.setWindowIcon(QIcon("icon.jpg"));
        self.setGeometry(300, 300, 400, 350)  # Increased height
        self.setStyleSheet('background-color: #3198c4; color: white;')

    def send_command(self):
        # This function will be called when the Send button is clicked
        ip = self.ip_entry.text()
        port = self.port_entry.text()
        password = self.password_entry.text()
        command = self.command_entry.text()

        # Simulate sending command and displaying output in the console area
        output_text = f'Sending command: {command}\nOutput: Dummy output\n'
        self.console_output.append(output_text)

    def stylize_entry(self, entry):
        entry.setStyleSheet(
            'QLineEdit {border: 2px solid #4CAF50; border-radius: 4px; padding: 2px; background: #F0F0F0; color: black;}'  # Lighter grey
            'QLineEdit:focus {border: 2px solid #4CAF50;}'
        )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StyledGUI()
    window.show()
    sys.exit(app.exec_())
