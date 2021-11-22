from UI.build.editMenu import Ui_editMenu as EditMenu
from PyQt5.QtWidgets import QWidget, QLineEdit

class editMenu(QWidget, EditMenu):

    def __init__(self,mainMenu, edit=-1 ,*args, **kwargs ):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.showPass = True
        self.mainMenu = mainMenu
        self.edit = edit
        if self.edit>-1:
            self.setData()
        self.showPassBtn.clicked.connect(self.hideShowPass)
        self.confirmBtn.clicked.connect(self.confirm)
        self.generatePassBtn.clicked.connect(self.generatePass)
        self.cancelBtn.clicked.connect(self.cancel)

    def hideShowPass(self):
        if self.showPass:
            self.passwordInput.setEchoMode(QLineEdit.Normal)
            self.showPassBtn.setText("Hide")
        else:
            self.passwordInput.setEchoMode(QLineEdit.Password)
            self.showPassBtn.setText("Show")
        self.showPass = not self.showPass
    
    #https://medium.com/analytics-vidhya/create-a-random-password-generator-using-python-2fea485e9da9
    def generatePass(self):
        print("generatePass")

    def setData(self):
        print("setdata")
        self.nameInput.setText(self.mainMenu.tableWidget.item(self.edit, 0).text())
        self.usernameInput.setText(self.mainMenu.tableWidget.item(self.edit, 1).text())
        self.emailInput.setText(self.mainMenu.tableWidget.item(self.edit, 2).text())
        self.passwordInput.setText(self.mainMenu.data["entries"][self.edit]["password"])
        self.urlInput.setText(self.mainMenu.tableWidget.item(self.edit, 4).text())
        self.discInput.setText(self.mainMenu.tableWidget.item(self.edit, 5).text())

    def getData(self):
        return {"name": self.nameInput.text(),
            "username": self.usernameInput.text(), 
            "email": self.emailInput.text(),
            "password": self.passwordInput.text(),
            "url": self.urlInput.text(),
            "description": self.discInput.toPlainText()
        }

    def confirm(self):
        if self.edit>-1:
            self.editEntry()
        else:
            self.mainMenu.addData(self.getData())
        self.close()
    
    def editEntry(self):
        self.mainMenu.changeData(index = self.edit, data = self.getData())
        self.close()

    def cancel(self):
        self.close()
#add data to main menu data or file
#add edit option