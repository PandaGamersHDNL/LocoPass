from logging import exception
from dataStruct import dataHandling
from crypto import Crypto
from PyQt5.QtWidgets import QWidget, QFileDialog, QDialog
from UI.build.newFile import Ui_NewFile as NewFileUI
from error import Error

class NewFile(QWidget, NewFileUI):

    def __init__(self, main, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.browseBtn.clicked.connect(self.browseFolder)
        self.cancelBtn.clicked.connect(self.cancel)
        self.confirmBtn.clicked.connect(self.confirm)
        self.show()
        self.main = main

    def browseFolder(self):
        print("browse")
        dialog = QFileDialog(self, 'Folder')
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        if dialog.exec_() == QDialog.Accepted:
            self.pathInput.setText(dialog.selectedFiles()[0])
            #self._audio_file = dialog.selectedFiles()[0]
        #bring open folder explorerer

    def confirm(self):
        try:
            crypto = Crypto(self.pathInput.text() + "/" + self.filenameInput.text() + ".bin", f"{self.usernameInput.text() + self.passInput.text()}")
            temp = open(crypto.path, "x")
            temp.close()
            self.main.crypto = crypto
            print("confirm")
            self.close()
        except:
            Error("new file failed")

    def cancel(self):
        print("cancel")