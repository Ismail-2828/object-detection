import cmath
import sys
import serial
from PyQt5.QtWidgets import *

def dialog():
    global mbox,A
    mbox = QMessageBox()
    A = a.text()
    B = b.text()
    C = c.text()

    D=(B**2)-(4*A*C)
    sol1=(-B-cmath.sqrt(D))/(2*A)
    sol2=(-B+cmath.sqrt(D))/(2*A)
    mbox.setWindowTitle("Answer")
    mbox.setText(f"Solutions: {sol1},{sol2}")
    mbox.exec_()
    

if __name__ =="__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(400,400)
    w.setWindowTitle("CALCULATOR")
    layout = QFormLayout()

    a = QLineEdit()
    b = QLineEdit()
    c = QLineEdit()
    layout.addRow("A:",a)
    layout.addRow("B:",b)
    layout.addRow("C:",c)

    btn = QPushButton("CALCULATE")
    btn.clicked.connect(dialog)
    layout.addRow(btn)

    w.setLayout(layout)
    w.show()
    

