from PyQt5.QtWidgets import (
QApplication,QWidget, QVBoxLayout, QLineEdit, QPushButton, QTableWidget,
QTableWidgetItem, QHBoxLayout, QLabel
)
app=QApplication([])
window=QWidget()
window.setWindowTitle("Table Generator")

layout= QVBoxLayout()
input_layout = QHBoxLayout()
label = QLabel("Enter Number for Table")
input_box= QLineEdit()
input_box.setPlaceholderText("Number")
input_layout.addWidget(label)
input_layout.addWidget(input_box)

table = QTableWidget()
table.setColumnCount(3)
table.setHorizontalHeaderLabels(["Number","Times","Result"])
table.hide()

def show_table():
	try:
		num = int(input_box.text())
		table.setRowCount(0)
		for i in range(1,11):
			row = table.rowCount()
			table.insertRow(row)
			table.setItem(row,0,QTableWidgetItem(f"{num}"))
			table.setItem(row,1,QTableWidgetItem(f"{i}"))
			table.setItem(row,2,QTableWidgetItem(f"{num*i}"))
			table.show()
	except ValueError:
		label.setText("Enter a valid number")
button = QPushButton("Show Table")
button.clicked.connect(show_table)

layout.addLayout(input_layout)
layout.addWidget(button)
layout.addWidget(table)

window.setLayout(layout)
window.show()
app.exec_()
