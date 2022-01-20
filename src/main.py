from error import Error
from auth import AuthMenu
#from crypto import Crypto
from UI.build.tablewidget import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu,QTableWidgetItem, QMessageBox, QDialogButtonBox
import json
from editMenuCustom import editMenu
from dataStruct import dataHandling
from newFileCustom import NewFile

#main window (table)
class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.actionadd.triggered.connect(self.openAdd)
        self.actionedit.triggered.connect(self.openEdit)
        self.actionsave.triggered.connect(self.saveData)
        self.actionsaveAs.triggered.connect(self.saveAs)
        self.actionopen.triggered.connect(self.open)
        self.actiondelete.triggered.connect(self.deleteSelected)
        self.actionnew.triggered.connect(self.newFile)
        self.actionexit.triggered.connect(self.exit)
        #TODO remove example in UI file
        self.show()    
        
    def loadData(self):
        self.tableWidget.setRowCount(len(self.data["entries"]))
        for indexEntry, i in enumerate(self.data["entries"]):
            for indexItem,j in enumerate(i):
                item = QTableWidgetItem()
                item.setText(i[j])
                if(j == "password"):
                    item.setText("********")
                self.tableWidget.setItem(indexEntry, indexItem, item)
    
    def saveData(self):
        try:
            self.crypto.encryptData(self.data)
            QMessageBox.information(self, "success", "saved successfully")
            return True
        except:
            Error("save error, opening new file")
            self.saveAs()
            return False

    def addData(self, data):
        self.data["entries"].append(data)
        self.loadData()

    def changeData(self, index, data):
        self.data["entries"][index] = data
        self.loadData()

    def openAdd(self):
        self.add = editMenu(self)
        self.add.show()
    
    def openEdit(self):
        selected = self.tableWidget.currentRow()
        if(selected == -1):
            Error("please select a row to edit")
        else:
            self.edit = editMenu(self, selected)
            self.edit.show()
        print(f"openEdit {selected}")

    def deleteSelected(self):
        selected = self.tableWidget.currentRow()
        if(selected >= 0):
            reply = QMessageBox().question(self,  "Delete?", f'Are you sure you want to delete {selected +1}', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if(reply == QMessageBox.Yes):
                self.data["entries"].pop(selected)
                self.loadData()

    def defCrypto(self, crypto):
        self.crypto = crypto
        self.data = self.crypto.decryptData()
        if(self.data == False):
            self.crypto = False
            return False
        self.loadData()
        self.show()
        return True
    
    def newFile(self):
        self.new = NewFile(self)
        if (self.new.exec_() == QDialogButtonBox.Ok):
            self.data = dataHandling.createEmpty()
            self.saveData()
            self.loadData()
            if(self.saveData() == True):
                QMessageBox.information(self, "success!", "new file successfully created")

    def saveAs(self):
        self.new = NewFile(self)
        if (self.new.exec_() == QDialogButtonBox.Ok):
            self.saveData()

    def open(self):
        self.auth = AuthMenu(main)
        
    def exit(self):
        reply = QMessageBox().question(self,  "exit", f'save before exiting?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if(reply == QMessageBox.Yes):
            if(self.saveData() == True):
                sys.exit()
        else:
            sys.exit()


#https://youtu.be/XXPNpdaK9WA

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # create a main window
    main = MainWindow()
    main.auth = AuthMenu(main)
    
    sys.exit(app.exec_())
