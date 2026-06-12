from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
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
ones_map = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
tens_map = {2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}

class NumberConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.create_widgets()
        self.create_grid()
        self.setup_window()
        self.create_link()

    def create_widgets(self):
        self.header_label = QLabel('Enter the number')
        self.header_label.setStyleSheet('font-size:30px; font-weight:bold;')
        self.input_label = QLabel('Enter the number:')
        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText('Number')
        self.submit_button = QPushButton('Submit')
        self.submit_button.setStyleSheet(green_btn_style)

    def create_grid(self):
        grid = QGridLayout()
        grid.addWidget(self.header_label,0,0,1,3,alignment=Qt.AlignCenter)
        grid.addWidget(self.input_label,1,0,1,1)
        grid.addWidget(self.input_box,1,2,1,1)
        grid.addWidget(self.submit_button,2,0,1,3,alignment=Qt.AlignCenter)
        self.setLayout(grid)

    def setup_window(self):
        self.setWindowTitle('Number Converter')
        self.setStyleSheet(style)
        self.setFixedWidth(422)

    def create_link(self):
        self.submit_button.clicked.connect(self.on_click)

    def on_click(self):
        try:
            num = int(self.input_box.text())
            if not 0 <= num <= 99:
                QMessageBox.warning(self, 'Input Error', 'The number must be 0-99')
                return
            if num <= 20:
                chars = ones_map[num]
            elif num < 100:
                tens = num // 10
                ones = num % 10
                if ones == 0:
                    chars = tens_map[tens]
                else: 
                    chars = f"{tens_map[tens]}-{ones_map[ones]}"
            self.show_result(f'The number is {chars}')
        except ValueError:
            QMessageBox.warning(self,'Input Error', 'Kindly enter valid numbers only.\nNumber and Rows must be integers.\nThe number must be 1-99')

    def show_result(self,text):
        self.header_label.setText(text)
        self.input_box.clear()

app = QApplication([])
window = NumberConverter()
window.show()
app.exec()