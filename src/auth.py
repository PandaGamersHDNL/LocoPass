from PyQt5.QtWidgets import QWidget
from UI.build.authentication import Ui_Authentication as authUI
import sys
from crypto import Crypto


class AuthMenu(QWidget, authUI):
    def __init__(self, main, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.confirmBtn.clicked.connect(self.confirm)
        self.cancelBtn.clicked.connect(self.cancel)
        self.show()
        self.main = main

    def confirm(self):
        crypto = Crypto(self.pathInput.text(), f"{self.usernameInput.text() + self.passwordInput.text()}")
        if(self.main.defCrypto(crypto) == True):
            self.close()

    def cancel(self):
        self.close()
        sys.exit()