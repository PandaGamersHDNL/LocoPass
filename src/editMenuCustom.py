from UI.build.editMenu import Ui_editMenu as EditMenu
from PyQt5.QtWidgets import QWidget, QLineEdit

class editMenu(QWidget, EditMenu):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.showPassBtn.clicked.connect(self.hideShowPass)
        self.showPass = True

    def hideShowPass(self):
        if self.showPass:
            self.passwordInput.setEchoMode(QLineEdit.Normal)
            self.showPassBtn.setText("Hide")
        else:
            self.passwordInput.setEchoMode(QLineEdit.Password)
            self.showPassBtn.setText("Show")
        self.showPass = not self.showPass
    
    def generatePass(self):
        print("generatePass")

    def getData(self):
        return {"beep": "beep", "boop": "boop"}
#add data to main menu data or file
