from UI.build.tablewidget import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu,QTableWidgetItem
import json

print("beep")

#main window (table)
class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.load()
        #self.testButton.clicked.connect()
        
    def load(self):
        file = open("./LocoPass/data.json", "r")
        data = json.load(file)
        self.tableWidget.setRowCount(len(data["entries"]))
        for indexEntry, i in enumerate(data["entries"]):
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
