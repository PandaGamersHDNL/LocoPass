from PyQt5.QtWidgets import QWidget, QFileDialog
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
        self.show()
        self.main = main

    def confirm(self):
        crypto = Crypto(self.pathInput.text(), f"{self.usernameInput.text() + self.passwordInput.text()}")
        if(self.main.defCrypto(crypto) == True):
            self.close()

    def cancel(self):
        self.close()
        sys.exit()

    def browse(self):
        filePath = QFileDialog.getOpenFileName(self, "Pick your .bin file", os.getcwd(), 'binairy files (*.bin)')
        self.pathInput.setText(filePath[0])