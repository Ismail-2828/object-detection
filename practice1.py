import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

if __name__ =="__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(400,400)
    
    # Layout=QFormLayout()
    # Layout.addRow("X: ",QLineEdit())
    # w.setLayout(Layout)


    # b2=QPushButton(w)
    # b2.move(100,100)
    # b2.resize(100,20)
    # b2.setText("BUTTON2")
    # b2.show()

    # b1=QPushButton(w)
    # b1.move(200,100)
    # b1.resize(100,20)
    # b1.setText("BUTTON1")
    # b1.show()

    
    # b3=QPushButton("Button3")
    # # b3.move(100,100)
    # b4=QPushButton("Button4")
    # # b4.move(100,100)
    

    # vbox=QVBoxLayout()
    # vbox.addWidget(b3)
    # # vbox.addStretch()
    # vbox.addWidget(b4)
    # vbox.addStretch()

    # hbox=QHBoxLayout()
    # b5=QPushButton("Button5")
    # b6=QPushButton("Button6")
    # hbox.addWidget(b5)
    # hbox.addStretch()
    # hbox.addWidget(b6)
    # # b3.move(300,200)

    
    # vbox.addStretch()
    # vbox.addLayout(hbox)
    # w.setLayout(vbox)
    # #Layout.resize(150,150)

    w.setLayout(Layout)
    w.show()
    sys.exit(app.exec_())