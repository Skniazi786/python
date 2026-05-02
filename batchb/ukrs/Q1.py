from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel,QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt

#Use these because why not.. Was planning to stich these to the window but nah.. 
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
app = QApplication([])

window = QWidget()
window.setWindowTitle("Table Generator")
#after testing with multiple widths.. this one seemed perfeclty matchin with the table most right line..
window.setFixedWidth(422)
window.table_status, window.original_height = False, 100
window.setFixedHeight(window.original_height)
grid = QGridLayout()

number_label = QLabel("Enter the number:")
number_box = QLineEdit()
number_box.setPlaceholderText('Number')

row_label = QLabel("Enter the rows:")
row_box = QLineEdit()
row_box.setPlaceholderText("Rows")

# copied your design for table word by word.. because why not..
table = QTableWidget()
table.setColumnCount(3)
table.setHorizontalHeaderLabels(["Number","Times","Result"])
table.verticalHeader().setVisible(False)
table.horizontalHeader().setStretchLastSection(True)
table.setVisible(False)

toggle_table = QPushButton("Show Table")
toggle_table.setStyleSheet(btn_style_green)
def on_click():
    try:
        num = int(number_box.text())
        rows = int(row_box.text())
        # really wanted to add that dynamic open/close button so resorted to this.. 
        if not window.table_status:
            table.setRowCount(rows)
            for i in range(rows):
                # in my looking up table items.. i surprisingly didn't found the table.insertrow.. so decided to skip it.. and it worked! yea that i+1 is a bit ugly to look at.. too tired right now to think of a better solution.
                item1,item2,item3 = QTableWidgetItem(f"{num}"), QTableWidgetItem(f"{i+1}"), QTableWidgetItem(f"{num*(i+1)}")
                item1.setTextAlignment(Qt.AlignCenter)
                item2.setTextAlignment(Qt.AlignCenter)
                item3.setTextAlignment(Qt.AlignCenter)
                table.setItem(i,0,item1)
                table.setItem(i,1,item2)
                table.setItem(i,2,item3)
            toggle_table.setStyleSheet(btn_style_red)
            toggle_table.setText("Close Table")
            window.table_status = True
            window.setFixedHeight(500)
            table.setVisible(True)
            number_box.setVisible(False)
            row_box.setVisible(False)

        else:
            # took this setvisible straight from chatgpt.. not gonna lie or deny it.. *supposedly* it's supposed to work with all the other widgets as well.. maybe even the whole window..
            table.setVisible(False)
            number_box.setVisible(True)
            row_box.setVisible(True)
            number_box.clear()
            row_box.clear()
            toggle_table.setStyleSheet(btn_style_green)
            toggle_table.setText("Show Table")
            window.table_status = False
            window.setFixedHeight(window.original_height)
            

    except ValueError:
        # really wanted to do this.. in tkinter there was a small popup on bottom right for errors.. gonna change that with this as well if i live till then..
        QMessageBox.warning(window,'Input Error', 'Kindly enter valid numbers only.\nNumber and Rows must be integers.')

toggle_table.clicked.connect(on_click)

grid.addWidget(number_label,0,0)
grid.addWidget(number_box,0,1)
grid.addWidget(row_label,1,0)
grid.addWidget(row_box,1,1)
# the 0 is row, 2 is column, 2 is rowspan and 1 is column span..
grid.addWidget(toggle_table,0,2,2,1)
grid.addWidget(table,2,0,1,3)
window.setLayout(grid)
window.show()
# supposedly even the chatgpt wanted me to use _exec() but exec() is working fine so meh..
app.exec()

# gonna make this class based tomorrow.. it's 4 am now.. i am too tired.. we need to switch to class based right now..