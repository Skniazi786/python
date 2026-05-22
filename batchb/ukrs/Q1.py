from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel,QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt

#Finally switched to Class based app after what? 27 days.. sheesh.. talk about days wasted..

btn_style_green, btn_style_red = """
    QPushButton {
        background-color: #27ae60;
        color: white;
        font-size: 20px;
        border-radius: 8px;
        padding: 8px;
        padding-top: 28px;
        padding-bottom: 28px;                
    }
    QPushButton:hover {
        background-color: #219150;
    }
""", """
    QPushButton {
        background-color: #e74c3c;
        color: white;
        font-size: 20px;
        border-radius: 8px;
        padding: 8px;
        padding-top: 28px;
        padding-bottom: 28px;                
    }
    QPushButton:hover {
        background-color: #c0392b;
    }
"""

#The reason why i use QWidget is gonna be honest cuz of chatgpt, it's better to use QWidget as a the base class since i will be using it as a well.. a base huehue..
class TableGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.table_status = False
        self.original_height = 100
        self.create_widgets()
        self.create_grid()
        self.create_link()

    def create_widgets(self):
        #Prepare The Labels
        self.number_label = QLabel("Enter the number:")
        self.number_box = QLineEdit()
        self.number_box.setPlaceholderText('Number')

        self.row_label = QLabel("Enter the rows:")
        self.row_box = QLineEdit()
        self.row_box.setPlaceholderText("Rows")
        
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Number","Times","Result"])
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setVisible(False)
        self.toggle_table = QPushButton("Show Table")
        self.toggle_table.setStyleSheet(btn_style_green)
    
    def setup_window(self):
        self.setWindowTitle('Table Generator')
        self.setFixedWidth(422)
        self.setFixedHeight(self.original_height)
 
    def create_grid(self):
        grid = QGridLayout()
        grid.addWidget(self.number_label,0,0)
        grid.addWidget(self.number_box,0,1)
        grid.addWidget(self.row_label,1,0)
        grid.addWidget(self.row_box,1,1)
        # the 0 is row, 2 is column, 2 is rowspan and 1 is coumn span..
        grid.addWidget(self.toggle_table,0,2,2,1)
        grid.addWidget(self.table,2,0,1,3)
        self.setLayout(grid)

#a whole new function just for this looked cooler in my head..
    def create_link(self):
        self.toggle_table.clicked.connect(self.on_click)
        
    def on_click(self):
        try:
            num = int(self.number_box.text())
            rows = int(self.row_box.text())
            # really wanted to add that dynamic open/close button so resorted to this.. 
            if not self.table_status:
                self.table.setRowCount(rows)
                for i in range(rows):
                    # in my looking up table items.. i surprisingly didn't found the table.insertrow.. so decided to skip it.. and it worked! yea that i+1 is a bit ugly to look at.. too tired right now to think of a better solution.
                    item1,item2,item3 = QTableWidgetItem(f"{num}"), QTableWidgetItem(f"{i+1}"), QTableWidgetItem(f"{num*(i+1)}")
                    item1.setTextAlignment(Qt.AlignCenter)
                    item2.setTextAlignment(Qt.AlignCenter)
                    item3.setTextAlignment(Qt.AlignCenter)
                    self.table.setItem(i,0,item1)
                    self.table.setItem(i,1,item2)
                    self.table.setItem(i,2,item3)
                self.toggle_table.setStyleSheet(btn_style_red)
                self.toggle_table.setText("Close Table")
                self.table_status = True
                self.setFixedHeight(500)
                self.table.setVisible(True)
                self.number_box.setVisible(False)
                self.row_box.setVisible(False)

            else:
                # took this setvisible straight from chatgpt.. not gonna lie or deny it.. *supposedly* it's supposed to work with all the other widgets as well.. maybe even the whole window..
                self.table.setVisible(False)
                self.number_box.setVisible(True)
                self.row_box.setVisible(True)
                self.number_box.clear()
                self.row_box.clear()
                self.toggle_table.setStyleSheet(btn_style_green)
                self.toggle_table.setText("Show Table")
                self.table_status = False

                self.setFixedHeight(self.original_height)
            

        except ValueError:
            # really wanted to do this.. in tkinter there was a small popup on bottom right for errors.. gonna change that with this as well if i live till then..
            QMessageBox.warning(self,'Input Error', 'Kindly enter valid numbers only.\nNumber and Rows must be integers.')

#instead of adding the Application in my class, it's better to just make it in while running the function.. supposedly i/we should be able to add more windows in future (InshAllah)
app = QApplication([])
window = TableGenerator()
window.show()
#works fine, do let me know if you see any issue on yer end..
app.exec()