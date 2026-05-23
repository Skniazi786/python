from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

#Not finished because my mind is not working rn.. gonna give it rest for the day and maybe work on the Q4 for the time being..

style = """
QWidget{ background-color: #2c3e50;color: white; }
QLineEdit {background-color:#222 ;border: 1px solid #555;padding: 10px;}
QLabel { font-size: 17px;  }
QPushButton {background-color: #27ae60;font-size: 15px;border-radius: 8px;padding:10px;}
QPushButton:hover {background-color: #219150;}
"""
red_button = """QPushButton {background-color: #e74c3c;font-size: 15px;border-radius: 8px;padding:10px;}
QPushButton:hover {background-color: #c0392b;}
"""

class CaesarCipher(QWidget):
    def __init__(self):
        super().__init__()
        self.text = ''
        self.num = 0
        self.ciphered = False
        self.create_widgets()
        self.create_grid()
        self.setup_window()
        self.create_link()
    
    def create_widgets(self):
        self.text_label = QLabel('Kindly enter the word/s you want to Caesar Cipher: ')
        self.text_box = QLineEdit()
        self.text_box.setPlaceholderText("Enter the word")

        self.number_label = QLabel('Kindly enter the number you want to Caesar Cipher by: ')
        self.number_box = QLineEdit()
        self.number_box.setPlaceholderText('Enter the number')

        self.result_label = QLabel('PLACEHOLDER')
        self.result_label.setVisible(False)
        self.result_label.setStyleSheet('font-size:35px;')
        self.submit_button = QPushButton('Caesar Cipher')

    def create_grid(self):
        grid = QGridLayout()
        grid.addWidget(self.text_label,0,0,1,2,alignment=Qt.AlignCenter)
        grid.addWidget(self.text_box,0,2)
        grid.addWidget(self.number_label,1,0,1,2,alignment=Qt.AlignCenter)
        grid.addWidget(self.number_box,1,2)
        grid.addWidget(self.result_label,0,1)
        grid.addWidget(self.submit_button,2,0,1,3,alignment=Qt.AlignCenter)
        self.setLayout(grid)
    
    def setup_window(self):
        self.setWindowTitle('Caesar Cipher Program')
        self.setStyleSheet(style)
        self.setFixedWidth(580)
        self.setFixedHeight(150)

    def create_link(self):
        self.submit_button.clicked.connect(self.on_click)
    
    def on_click(self):
        try:
            if self.ciphered:
                self.reset_program()
            else:
                self.text = self.text_box.text().strip()
                self.num = int(self.number_box.text().strip())
                ciphered_charas = []
                for chara in self.text:
                    ascii_num = ord(chara)
                    shifted = ascii_num + self.num
                    if shifted > ord('z'):
                        diff = shifted - ord('z')
                        diff += ord('a')
                        ciphered_charas.append(chr(diff))
                    else:
                        ciphered_charas.append(chr(shifted))
                c_text = "".join(ciphered_charas)
                self.result_label.setText(f'The ciphered text is {c_text}')
                self.successful_input()
        except ValueError:
            QMessageBox.warning(self,'Input Error','Kindly enter valid inputs.')
    
    def successful_input(self):
        self.text_label.setVisible(False)
        self.text_box.setVisible(False)
        self.text_box.clear()
        self.number_label.setVisible(False)
        self.number_box.setVisible(False)
        self.number_box.clear()
        self.result_label.setVisible(True)
        self.submit_button.setText('Reset Program')
        self.submit_button.setStyleSheet(red_button)
        self.ciphered = True

    def reset_program(self):
        self.text_label.setVisible(True)
        self.text_box.setVisible(True)
        self.number_label.setVisible(True)
        self.number_box.setVisible(True)
        self.result_label.setVisible(False)
        self.submit_button.setText('Caesar Cipher')
        self.submit_button.setStyleSheet(style)
        self.ciphered = False

app = QApplication([])
window = CaesarCipher()
window.show()
app.exec()