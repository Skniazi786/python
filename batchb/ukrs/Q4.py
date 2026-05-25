from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt

style = """
    QWidget {background-color: #2c3e50;color: white;}
    QPushButton {background-color: #27ae60;font-size: 15px;border-radius: 8px;padding:10px;}
    QPushButton:hover {background-color: #219150;}
    QLineEdit {background-color:#222 ;border: 1px solid #555;padding: 10px;}
    QLabel { text-align: center; font-size:20px;}
"""
green_btn_style = """QPushButton {background-color: #27ae60;font-size: 15px;border-radius: 8px;padding:10px;}QPushButton:hover {background-color: #219150;}"""
red_btn_style = """QPushButton {background-color: #e74c3c; color: white;font-size: 20px; border-radius: 8px; padding: 8px; padding-top: 28px; padding-bottom: 28px;} QPushButton:hover { background-color: #c0392b;}"""

class AnagramChecker(QWidget):
    def __init__(self):
        super().__init__()
        self.has_result = False
        self.create_widgets()
        self.create_grid()
        self.setup_window()
        self.create_link()
        
    def create_widgets(self):
        self.header_label = QLabel('Check if the two words are Anagram!')
        self.header_label.setStyleSheet('font-size:28px; font-weight:bold')

        self.first_txt_label = QLabel('Kindly enter the first word:')
        self.first_txt_box = QLineEdit()
        self.first_txt_box.setPlaceholderText('First word')

        self.second_txt_label = QLabel('Kindly enter the second word:')
        self.second_txt_box = QLineEdit()
        self.second_txt_box.setPlaceholderText('Second word')

        self.check_button = QPushButton('Check Anagram')
        self.check_button.setStyleSheet(green_btn_style)

    def create_grid(self):
        grid = QGridLayout()
        grid.addWidget(self.header_label,0,0,1,3,alignment=Qt.AlignCenter)
        grid.addWidget(self.first_txt_label,1,0,1,2,alignment=Qt.AlignRight)
        grid.addWidget(self.first_txt_box,1,2,1,1)
        grid.addWidget(self.second_txt_label,2,0,1,2,alignment=Qt.AlignRight)
        grid.addWidget(self.second_txt_box,2,2,1,1)
        grid.addWidget(self.check_button,3,0,1,3,alignment=Qt.AlignCenter)
        grid.setContentsMargins(50, 20, 50, 20)
        grid.setVerticalSpacing(10)
        grid.setHorizontalSpacing(10)
        self.setLayout(grid)

    def setup_window(self):
        self.setWindowTitle('Anagram Checker')
        self.setStyleSheet(style)
        self.setFixedWidth(580)

    def create_link(self):
        self.check_button.clicked.connect(self.on_click)

    def on_click(self):
        if self.has_result:
            self.reset_program()
        else:
            self.text1 = self.first_txt_box.text().lower().strip()
            self.text2 = self.second_txt_box.text().lower().strip()
            if self.text1.isalpha() and self.text2.isalpha():
                if sorted(self.text1) == sorted(self.text2):
                    self.result_anagram(True)
                else:
                    self.result_anagram(False)
            else:
                QMessageBox.warning(self,'Input Error','Kindly enter valid inputs.')
        
    def result_anagram(self,status):
        self.header_label.setText(f"{self.text1} & {self.text2} {'are' if status else 'are not'} anagrams")
        self.first_txt_label.setVisible(False)
        self.first_txt_box.setVisible(False)
        self.second_txt_label.setVisible(False)
        self.second_txt_box.setVisible(False)
        self.check_button.setText('Reset Program')
        self.check_button.setStyleSheet(red_btn_style)
        self.has_result = True

    def reset_program(self):
        self.header_label.setText('Check if the two words are Anagram!')
        self.first_txt_label.setVisible(True)
        self.first_txt_box.setVisible(True)
        self.first_txt_box.clear()
        self.second_txt_label.setVisible(True)
        self.second_txt_box.setVisible(True)
        self.second_txt_box.clear()
        self.check_button.setText('Check Anagram')
        self.check_button.setStyleSheet(green_btn_style)
        self.has_result = False

app = QApplication([])
window = AnagramChecker()
window.show()
app.exec()