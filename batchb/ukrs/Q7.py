from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
style = """
    QWidget {background-color: #2c3e50;color: white;}
    QPushButton {background-color: #27ae60;font-size: 15px;border-radius: 8px;padding:10px;}
    QPushButton:hover {background-color: #219150;}
    QLineEdit {background-color:#222 ;border: 1px solid #555;padding: 10px;}
    QLabel { text-align: center; font-size:20px;}
"""
btn_style = """
QPushButton {background-color: #27ae60;font-size: 25px;border-radius: 8px;padding:10px;}QPushButton:hover {background-color: #219150;}
"""

class Converter(QWidget):
    def __init__(self):
        super().__init__()
        self.create_widgets()
        self.create_grid()
        self.setup_window()
        self.create_link()
        
    def create_widgets(self):
        self.header_label = QLabel('This is the header label')
        self.header_label.setStyleSheet('font-size:30px; font-weight:bold;')

    def create_grid(self):
        grid = QGridLayout()
        grid.addWidget(self.header_label,0,0,1,1,alignment=Qt.AlignCenter)
        self.setLayout(grid)

    def setup_window(self):
        self.setWindowTitle('Converter')
        self.setStyleSheet(style)
        self.setFixedWidth(422)

    def create_link(self):
        pass

app = QApplication([])
window = Converter()
window.show()
app.exec()