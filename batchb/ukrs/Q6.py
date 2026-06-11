from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel

class NumberConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.create_widgets()
        self.create_grid()
        self.setup_window()
        self.create_link()

    def create_widgets(self):
        self.header_label = QLabel('This is the header label')

    def create_grid(self):
        grid = QGridLayout()
        grid.addWidget(self.header_label,0,0,1,1)
        self.setLayout(grid)

    def setup_window(self):
        self.setWindowTitle('Number Converter')

    def create_link(self):
        pass

app = QApplication([])
window = NumberConverter()
window.show()
app.exec()