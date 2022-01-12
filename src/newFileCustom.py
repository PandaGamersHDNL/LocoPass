from PyQt5.QtWidgets import QWidget, QFileDialog, QDialog
from UI.build.newFile import Ui_NewFile as NewFileUI

class NewFile(QWidget, NewFileUI):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.browseBtn.clicked.connect(self.browseFolder)
        self.cancelBtn.clicked.connect(self.cancel)
        self.confirmBtn.clicked.connect(self.confirm)
        self.show()

    def browseFolder(self):
        print("browse")
        dialog = QFileDialog(self, 'Folder')
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        if dialog.exec_() == QDialog.Accepted:
            self.pathInput.setText(dialog.selectedFiles()[0])
            #self._audio_file = dialog.selectedFiles()[0]
        #bring open folder explorerer

    def confirm(self):
        print("confirm")

    def cancel(self):
        print("cancel")