from PyQt5.QtWidgets import QMessageBox

class Error(QMessageBox):

    def __init__(self, error, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText(error)
        self.setWindowTitle("Error")
        self.exec()
        #self.show()