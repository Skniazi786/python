from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox
from PyQt5.QtCore import Qt
style = """
    QWidget {
        background-color: #2c3e50;
        color: white;
    }

    QLineEdit {
        background-color: #222;
        border: 1px solid #555;
        padding: 10px;
        font-size: 20px;
    }

    QLabel {
        text-align: center;
        font-size: 20px;
    }

    QComboBox {
        background-color: #222;
        border: 1px solid #555;
        font-size: 20px;
        padding: 8px;
        border-radius: 5px;
        min-width: 120px;
        color: white;
    }

    QComboBox:hover {
        border: 1px solid #27ae60;
    }

    QComboBox::drop-down {
        image: none;
        width: 10px;
        height: 10px;
    }

    QComboBox QAbstractItemView {
        background-color: #222;
        border: 1px solid #555;
        selection-background-color: #27ae60;
        selection-color: white;
    }
"""
btn_style = """
QPushButton {background-color: #27ae60;font-size: 25px;border-radius: 8px;padding:10px;}
QPushButton:hover {background-color: #219150;}
"""
red_btn_style = """
QPushButton {background-color: #e74c3c;font-size: 25px;border-radius: 8px;padding:10px;} 
QPushButton:hover { background-color: #c0392b;}
"""

class Converter(QWidget):
    def __init__(self):
        super().__init__()
        self.forward = True
        self.create_widgets()
        self.create_grid()
        self.setup_window()
        self.create_link()
        
    def create_widgets(self):
        self.header_label = QLabel('What would you like to convert?')
        self.header_label.setStyleSheet('font-size:28px; font-weight:bold;')

        self.combo_label = QLabel('Type: ')
        self.combo = QComboBox()
        self.combo.addItems(['Distance','Weight','Temperature'])


        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText('Kilometer (Km) to Miles (M)')

        self.submit_btn = QPushButton('Convert')
        self.submit_btn.setStyleSheet(btn_style)
        self.chg_direction = QPushButton('Change Direction')
        self.chg_direction.setStyleSheet(red_btn_style)

    def create_grid(self):
        grid = QGridLayout()
        grid.addWidget(self.header_label,0,0,1,2,alignment=Qt.AlignCenter)
        grid.addWidget(self.combo_label,1,0)
        grid.addWidget(self.combo,1,1,1,2)
        grid.addWidget(QLabel("Value:"), 2, 0)
        grid.addWidget(self.input_box,2,1)
        grid.addWidget(self.chg_direction,3,0,1,1)
        grid.addWidget(self.submit_btn,3,1,1,3)
        self.setLayout(grid)

    def setup_window(self):
        self.setWindowTitle('Converter')
        self.setStyleSheet(style)
        self.setFixedWidth(550)

    def create_link(self):
        self.combo.currentTextChanged.connect(self.change_unit)
        self.submit_btn.clicked.connect(self.on_click)
        self.chg_direction.clicked.connect(self.change_direction)

    def change_unit(self):
        unit = self.combo.currentText()
        if unit == 'Weight':
            self.input_box.setPlaceholderText('Kilogram(Kg) to Pounds(Lbs)')
        elif unit == 'Temperature':
            self.input_box.setPlaceholderText('Celsius(°C) to Fahrenheit(°F)')
        else:
            self.input_box.setPlaceholderText('Kilometer(KM) to Miles(M)')
        self.forward = True

    def on_click(self):
        unit = self.combo.currentText()
        try:  
            num = float(self.input_box.text())
            if unit == 'Weight':
                self.convert_weight(num)
            elif unit == 'Distance':
                self.convert_distance(num)
            else:
                self.convert_temp(num)
            self.input_box.clear()
        except ValueError: 
            QMessageBox.warning(self,'Input Error', 'Please enter a valid number only.')

    def change_direction(self):
        unit = self.combo.currentText()
        if unit == "Weight":
            if self.forward:
                self.input_box.setPlaceholderText('Pounds(Lbs) to Kilogram (Kg)')
            else: 
                self.input_box.setPlaceholderText('Kilogram(Kg) to Pounds(Lbs)')
        elif unit == "Temperature":
            if self.forward:
                self.input_box.setPlaceholderText('Fahrenheit(°F) to Celsius(°C)')
            else:
                self.input_box.setPlaceholderText('Celsius(°C) to Fahrenheit(°F)')
        else:
            if self.forward:
                self.input_box.setPlaceholderText('Miles(M) to Kilometer(Km)')
            else:
                self.input_box.setPlaceholderText('Kilometer(KM) to Miles(M)')
        self.forward = not self.forward

    def convert_distance(self,num):
        if self.forward:
            result = num / 1.60934
        else:
            result = num * 1.60934
        self.header_label.setText(f'Result: {result:.2f}')

    def convert_weight(self, num):
        if self.forward:
            result = num * 2.20462
        else:
            result = num / 2.20462
        self.header_label.setText(f'Result: {result:.2f}')

    def convert_temp(self,num):
        if self.forward:
            result = (num * (9/5)) + 32
        else:
            result = (num - 32 ) * (5/9)
        self.header_label.setText(f'Result: {result:.2f}')

app = QApplication([])
window = Converter()
window.show()
app.exec()