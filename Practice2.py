import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

def submit():
    global mbox,NAME,ADDRESS
    mbox=QMessageBox()
    NAME = add1.text()
    ADDRESS = add2.text()

    if NAME and ADDRESS:
       mbox.setText("Application Successful!")
       mbox.setWindowTitle("submission")
       mbox.exec_()

    else:
       
       mbox.setText("Spaces should not be empty")
       mbox.exec_()
    #  QMessageBox.warning(win,"Error","Space shouldnt be empty")
       


if __name__=="__main__":
    app=QApplication(sys.argv)
    win=QWidget()
    win.resize(400,200)
    
    add1 = QLineEdit()
    add2 = QLineEdit()
    add3 = QLineEdit()
    add4 = QLineEdit()

    l1 = QLabel("NAME")
    font=QFont()
    font.setFamily("Arial")
    font.setPointSize(12)
    l1.setFont(font)
    nm = QLineEdit()
    l2= QLabel("ADDRESS")
    l2.setFont(font)
    fbox = QFormLayout()
    vbox = QVBoxLayout()
    vbox.addWidget(add3)
    vbox.addWidget(add4)
    fbox.addRow(l1,vbox)
    vbox = QVBoxLayout()
    vbox.addWidget(add1)
    vbox.addWidget(add2)
    fbox.addRow(l2,vbox)

    hbox = QHBoxLayout()
    r1 = QRadioButton("Male")
    r2 = QRadioButton("Female")
    hbox.addWidget(r1)
    hbox.addWidget(r2)
    # hbox.addStretch()
    b1=QPushButton("Submit")
    b2=QPushButton("Cancel")
    fbox.addRow(QLabel("sex"),hbox)
    fbox.addRow(b1,b2)
    b1.clicked.connect(submit)

    win.setLayout(fbox)

    win.show()
    sys.exit(app.exec_())

