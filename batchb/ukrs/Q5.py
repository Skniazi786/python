from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
import string
style = """
    QWidget {background-color: #2c3e50;color: white;}
    QPushButton {background-color: #27ae60;font-size: 15px;border-radius: 8px;padding:10px;}
    QPushButton:hover {background-color: #219150;}
    QLineEdit {background-color:#222 ;border: 1px solid #555;padding: 10px;}
    QLabel { text-align: center; font-size:20px;}
"""
green_btn_style = """
QPushButton {background-color: #27ae60;font-size: 25px;border-radius: 8px;padding:10px;}QPushButton:hover {background-color: #219150;}
"""
red_btn_style = """
PushButton {background-color: #e74c3c; color: white;font-size: 30px; border-radius: 8px; padding: 8px; padding-top: 28px; padding-bottom: 28px;} 
QPushButton:hover { background-color: #c0392b;}
"""
STRENGTH_MAP = [
    (3,'Weak'), (4,'Medium'), (5,'Strong')
]
class PasswordChecker(QWidget):
    def __init__(self):
        super().__init__()
        self.create_widgets()
        self.create_grid()
        self.setup_window()
        self.create_link()
    
    def create_widgets(self):
        self.header_label = QLabel('Check your Password Protection')
        self.header_label.setStyleSheet('font-size:30px; font-weight:bold;')

        self.pwsd_label = QLabel('Enter the password: ')
        self.pwsd_box = QLineEdit()
        self.pwsd_box.setPlaceholderText('Password here')

        self.submit_button = QPushButton('Submit')
        self.submit_button.setStyleSheet(green_btn_style)

    def create_grid(self):
        grid = QGridLayout()
        grid.addWidget(self.header_label,0,0,1,3,alignment=Qt.AlignCenter)
        grid.addWidget(self.pwsd_label,1,0,1,1)
        grid.addWidget(self.pwsd_box,1,1,1,2)
        grid.addWidget(self.submit_button,2,0,1,3,alignment=Qt.AlignCenter)
        self.setLayout(grid)
     
    def setup_window(self):
        self.setWindowTitle('Password Checker')
        self.setStyleSheet(style)

    def create_link(self):
        self.submit_button.clicked.connect(self.on_click)

    def on_click(self):
        pswd = self.pwsd_box.text()
        pswd_level = self.pswd_chckr(pswd)
        self.header_label.setText(f'Your password strength is {pswd_level}')
        self.pwsd_box.clear()
    
    def pswd_chckr(self,pswd):
        score = 0
        if len(pswd) >= 8: score += 1
        if any(c.islower() for c in pswd): score += 1
        if any(c.isupper() for c in pswd): score += 1
        if any(c.isdigit() for c in pswd): score += 1
        if any(c in string.punctuation for c in pswd): score += 1
        strength = self.pswd_strength(score)
        return strength

    def pswd_strength(self,score):
        for scr,label in STRENGTH_MAP:
            if score <= scr:
                return label

app = QApplication([])
window = PasswordChecker()
window.show()
app.exec()