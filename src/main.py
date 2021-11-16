from UI.build.tablewidget import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu,QTableWidgetItem, QMessageBox
import json
from editMenuCustom import editMenu

print("beep")

#main window (table)
class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        file = open("./LocoPass/data.json", "r")
        self.data = json.load(file)
        self.testButton.clicked.connect(self.addData)
        self.actionadd.triggered.connect(self.openAdd)
        self.actionedit.triggered.connect(self.openEdit)
        self.loadData()
        
    #load data to table TODO en/decrypt data
    def loadData(self):
        self.tableWidget.setRowCount(len(self.data["entries"]))
        for indexEntry, i in enumerate(self.data["entries"]):
            for indexItem,j in enumerate(i):
                item = QTableWidgetItem()
                item.setText(i[j])
                if(j == "password"):
                    item.setText("********")
                self.tableWidget.setItem(indexEntry, indexItem, item)
                #print(i[j])
        #print(self.tableWidget.currentItem().text())
        #print(self.tableWidget.rowCount())
       # 
    def addData(self, data):
        self.data["entries"].append(data)
        self.loadData() #TODO change so we don't loop over all the data?

    def openAdd(self):
        self.add = editMenu(self)
        self.add.show()
    
    def openEdit(self):
        selected = self.tableWidget.currentRow()
        if(selected == -1):
            alert = QMessageBox()
            alert.setText("please select a row to edit")
            alert.setWindowTitle("Error")
            alert.exec()
        else:
            self.edit = editMenu(self, selected)
            self.edit.show()

        print(f"openEdit {selected}")

        
        
#get selected items
#for item in self.tableWidget.selectedItems():
#            print(f"selectedItems {item.text()}")
        
#https://youtu.be/XXPNpdaK9WA


if __name__ == "__main__":

    app = QApplication(sys.argv)
    # create a main window
    main = MainWindow()
    main.show()
    #main.save()
    #main_win.customContextMenuRequested.connect(right_menu)
    #main_win.show(main)
    #main.show()

    sys.exit(app.exec_())
