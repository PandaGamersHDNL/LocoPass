from PyQt5.QtWidgets import QWidget
from UI.build.newFile import Ui_NewFile as NewFileUI

class NewFile(QWidget, NewFileUI):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()