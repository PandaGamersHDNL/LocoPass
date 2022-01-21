from logging import exception
from dataStruct import dataHandling
from crypto import Crypto
from PyQt5.QtWidgets import QDialogButtonBox, QFileDialog, QDialog, QLineEdit, QMessageBox
from UI.build.newFile import Ui_newFile as NewFileUI
from error import Error

class NewFile(QDialog, NewFileUI):

    def __init__(self, main, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        #self.buttonBox.rejected.connect(self.reject)
        #self.buttonBox.accepted.connect(self.accept)
        self.browseBtn.clicked.connect(self.browseFolder)
        self.showPassBtn.clicked.connect(self.hideShowPass)
        self.showPass = True
        self.show()
        self.main = main

    def browseFolder(self):
        print("browse")
        dialog = QFileDialog(self, 'Folder')
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        if dialog.exec_() == QDialog.Accepted:
            self.pathInput.setText(dialog.selectedFiles()[0])

    def accept(self):
        try:
            if(self.passInput.text() != ''):
                crypto = Crypto(self.pathInput.text() + "/" + self.filenameInput.text() + ".bin", f"{self.usernameInput.text() + self.passInput.text()}")
                temp = open(crypto.path, "x")
                temp.close()
                self.main.crypto = crypto
                print("confirm")
                self.close()
            else:
                QMessageBox.critical(self, "Error!", "Please enter a password.")
        except:
            QMessageBox.critical(self, "Error!", "Path already exists or isn\'t valid")


    def reject(self):
        print("cancel")
        self.done(QDialogButtonBox.Cancel)

    def hideShowPass(self):
        if self.showPass:
            self.passInput.setEchoMode(QLineEdit.Normal)
            self.showPassBtn.setText("Hide")
        else:
            self.passInput.setEchoMode(QLineEdit.Password)
            self.showPassBtn.setText("Show")
        self.showPass = not self.showPass