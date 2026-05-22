from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
import random

style = """
    QWidget {background-color: #2c3e50;color: white;}
    QPushButton {background-color: #27ae60;font-size: 15px;border-radius: 8px;padding:10px;}
    QPushButton:hover {background-color: #219150;}
    QLineEdit {background-color:#222 ;border: 1px solid #555;padding: 10px;}
    QLabel { text-align: center;}
"""
red_button = """QPushButton {background-color: #e74c3c;font-size: 15px;border-radius: 8px;padding:10px;}
QPushButton:hover {background-color: #c0392b;}
"""

class NumberGuessingGame(QWidget):
    def __init__(self):
        super().__init__()
        self.random_number = random.randint(1,100)
        self.tries = 0
        self.has_won = False
        self.create_widgets()
        self.create_grid()
        self.setup_window()
        self.create_link()
    
    def reset_game(self):
        self.random_number = random.randint(1,100)
        self.tries = 0
        self.has_won = False
        self.header_label.setVisible(True)
        self.number_box.setVisible(True)
        self.number_box.clear()
        self.mystery_label.setText('???')
        self.mystery_label.setStyleSheet("font-size: 26px;")
        self.tries_label.setText('Total Tries: 0')
        self.check_button.setText('Check the guess')
        self.check_button.setStyleSheet(style)

    def create_widgets(self):
        self.header_label = QLabel('Guess the number')
        self.header_label.setStyleSheet("font-size: 35px; font-weight: bold;")
        self.mystery_label = QLabel('???')
        self.mystery_label.setStyleSheet("font-size: 26px;")
        self.number_box = QLineEdit()
        self.number_box.setPlaceholderText("Make a guess")
        self.check_button = QPushButton("Check the guess")
        self.tries_label = QLabel('Total Tries: 0')
        self.tries_label.setStyleSheet("font-size: 25px;")
        self.tries_label.setAlignment(Qt.AlignCenter)
    
    def create_grid(self):
        grid = QGridLayout()
        grid.addWidget(self.header_label,0,0,1,3,alignment=Qt.AlignCenter)
        grid.addWidget(self.mystery_label,1,0,1,3,alignment=Qt.AlignCenter)
        grid.addWidget(self.number_box,2,0,1,3)
        grid.addWidget(self.check_button,3,0,1,3,alignment=Qt.AlignCenter)
        grid.addWidget(self.tries_label,4,0,1,3,alignment=Qt.AlignCenter)
        grid.setContentsMargins(50, 20, 50, 20)
        grid.setVerticalSpacing(10)
        grid.setHorizontalSpacing(10)
        self.setLayout(grid)

    def setup_window(self):
        self.setWindowTitle('Number Guessing Game')
        self.setFixedHeight(270)
        self.setFixedWidth(420)
        self.setStyleSheet(style)

    def create_link(self):
        self.check_button.clicked.connect(self.on_click)

    def on_click(self):
        try:
            if self.has_won:
                self.reset_game()
            else:
                num = int(self.number_box.text())
                if num > self.random_number: self.input_update('Too high!')
                elif num < self.random_number: self.input_update('Too Low!')
                else:
                    self.successful_guess()
        except ValueError:
            QMessageBox.warning(self,'Input Error', 'Kindly enter valid numbers only.')    

    def input_update(self,text):
        self.mystery_label.setText(text)
        self.number_box.clear()
        self.tries += 1
        self.tries_label.setText(f'Total Tries: {self.tries}')

    def successful_guess(self):
        self.has_won = True
        self.number_box.setVisible(False)
        self.header_label.setVisible(False)
        self.mystery_label.setStyleSheet("font-size: 36px;")
        self.mystery_label.setText(f'The number is {self.random_number}')
        self.tries_label.setText(f'Congratulations!\nYou got the guess in {self.tries} tries.')
        self.check_button.setText('Restart Game')
        self.check_button.setStyleSheet(red_button)


app = QApplication([])
window = NumberGuessingGame()
window.show()
app.exec()