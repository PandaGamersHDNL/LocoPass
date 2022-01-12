from error import error
from auth import AuthMenu
#from crypto import Crypto
from UI.build.tablewidget import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu,QTableWidgetItem, QMessageBox
import json
from editMenuCustom import editMenu
from dataStruct import dataHandling
from newFileCustom import NewFile



print("beep")
#TODO rename safe to save
#TODO login system

#main window (table)
class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        #TODO create option to pick which file (in auth?)
        self.actionadd.triggered.connect(self.openAdd)
        self.actionedit.triggered.connect(self.openEdit)
        self.actionsafe.triggered.connect(self.saveData)
        self.actiondelete.triggered.connect(self.deleteSelected)
        self.actionnew.triggered.connect(self.newFile)
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
        except:
            error("save error, opening new file")
            self.new = NewFile()
            return False

    def addData(self, data):
        self.data["entries"].append(data)
        self.loadData() #TODO change so we don't loop over all the data?

    def changeData(self, index, data):
        self.data["entries"][index] = data
        self.loadData()

    def openAdd(self):
        self.add = editMenu(self)
        self.add.show()
    
    def openEdit(self):
        selected = self.tableWidget.currentRow()
        if(selected == -1):
            error("please select a row to edit")
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
        #self.testButton.clicked.connect(self.crypto.decryptData)
        self.data = self.crypto.decryptData()
        if(self.data == False):
            #TODO change so we can make a new one if we can't log in?
            return False
        self.loadData()
        self.show()
        return True
    
    def newFile(self):
        self.new = NewFile()
        
#get selected items
#for item in self.tableWidget.selectedItems():
#            print(f"selectedItems {item.text()}")
        
#https://youtu.be/XXPNpdaK9WA


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # create a main window
    main = MainWindow()
    auth = AuthMenu(main)
    
    #main.save()
    #main_win.customContextMenuRequested.connect(right_menu)
    #main_win.show(main)
    #main.show()
    sys.exit(app.exec_())
