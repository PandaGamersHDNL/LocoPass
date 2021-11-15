from UI.build.tablewidget import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu,QTableWidgetItem
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
        self.actionadd.triggered.connect(self.openEdit)
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
    def addData(self):
        self.data["entries"].append({"name": "example", "username": "user", "email": "example@example.com", "password": "beepboop", "url": "example.com", "description": 'this is an example entry'})
        self.loadData() #TODO change so we don't loop over all the data?

    def openEdit(self):
        self.edit = editMenu()
        self.edit.show()
        temp = self.edit.getData()
        print(temp)
        
        
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
