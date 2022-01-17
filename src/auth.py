from PyQt5.QtWidgets import QWidget, QFileDialog, QLineEdit
from UI.build.authentication import Ui_Authentication as authUI
import sys
from crypto import Crypto
from dataStruct import dataHandling
import os

class AuthMenu(QWidget, authUI):
    def __init__(self, main, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.confirmBtn.clicked.connect(self.confirm)
        self.cancelBtn.clicked.connect(self.cancel)
        self.browseBtn.clicked.connect(self.browse)
        self.showPassBtn.clicked.connect(self.hideShowPass)
        self.show()
        self.showPass = True
        self.main = main

    def confirm(self):
        crypto = Crypto(self.pathInput.text(), f"{self.usernameInput.text() + self.passwordInput.text()}")
        if(self.main.defCrypto(crypto) == True):
            self.close()

    def cancel(self):
        self.main.data = dataHandling.createEmpty()
        self.main.crypto = False
        self.main.loadData()
        self.close()
        #sys.exit()

    def browse(self):
        filePath = QFileDialog.getOpenFileName(self, "Pick your .bin file", os.getcwd(), 'binairy files (*.bin)')
        self.pathInput.setText(filePath[0])

    def hideShowPass(self):
        if self.showPass:
            self.passwordInput.setEchoMode(QLineEdit.Normal)
            self.showPassBtn.setText("Hide")
        else:
            self.passwordInput.setEchoMode(QLineEdit.Password)
            self.showPassBtn.setText("Show")
        self.showPass = not self.showPass