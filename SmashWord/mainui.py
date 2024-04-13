from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from sorting import Sorting
import csv
from newest import main 
import sys
from tkinter import messagebox
from time import sleep
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread
import datetime
import time
from Search import Searching
import traceback
import tkinter as tk
class MainWindow(QMainWindow):
    def __init__(self):
        self.root = tk.Tk()
        super().__init__()
        self.DataTable = QTableWidget()
        loadUi('untitled.ui', self)
        try:
         self.DataTable = self.tableWidget
         self.load_DataFromFile(r'C:\Users\hp\OneDrive\Desktop\Book1.csv')
        except Exception as e:
            print(f"An error occurred: {e}") 
        self.pushButton_3.setObjectName("pushbutton")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.pushButton_2.clicked.connect(self.pushButton2_clicked)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.start_scraping)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.stop_scraping)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.close)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.pause)
        self.pushButton_2.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.search)

       #  convert specific columns in data to integers
    def convert_columns_to_int(self, data):
        for row in data[1:]:
            for i in [2, 3, 5]:
                row[i] = float(row[i].replace(',', ''))
        return data
    
    #  read data from a CSV file
    def readdata(self):
        file_path = r'C:\Users\hp\OneDrive\Desktop\Book1.csv'
        with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
            datais = list(csv.reader(file)) 
        return datais  
 
         # load data from file to table    
    def load_DataFromFile(self,filename):
     try:
        with open(filename, 'r', encoding='iso-8859-1') as fileInput:
            
            tableRows = 0
            self.data = list(csv.reader(fileInput))
            self.DataTable.setRowCount(len(self.data))
            
            
            for row in self.data:
                
                self.DataTable.setItem(tableRows, 0, QtWidgets.QTableWidgetItem((row[0])))
                self.DataTable.setItem(tableRows, 1, QtWidgets.QTableWidgetItem((row[1])))
                self.DataTable.setItem(tableRows, 2, QtWidgets.QTableWidgetItem((row[2])))
                self.DataTable.setItem(tableRows, 3, QtWidgets.QTableWidgetItem((row[3])))
                self.DataTable.setItem(tableRows, 4, QtWidgets.QTableWidgetItem((row[4])))

                self.DataTable.setItem(tableRows, 5, QtWidgets.QTableWidgetItem((row[5])))
                self.DataTable.setItem(tableRows, 6, QtWidgets.QTableWidgetItem((row[6])))
                self.DataTable.setItem(tableRows, 7, QtWidgets.QTableWidgetItem((row[7])))
                #self.DataTable.setItem(tableRows, 8, QtWidgets.QTableWidgetItem((row[8])))
                tableRows += 1
     except Exception as e:
            print(f"An error occurred: {e}")
            traceback.print_exc()
 # delcare  table
    def load_Data(self):
        tableRows = 0
        self.DataTable.setRowCount(len(self.data))
        for row in self.data:
            self.DataTable.setItem(tableRows, 0, QtWidgets.QTableWidgetItem((row[0])))
            self.DataTable.setItem(tableRows, 1, QtWidgets.QTableWidgetItem((row[1])))
            self.DataTable.setItem(tableRows, 2, QtWidgets.QTableWidgetItem((row[2])))
            self.DataTable.setItem(tableRows, 3, QtWidgets.QTableWidgetItem((row[3])))
            self.DataTable.setItem(tableRows, 4, QtWidgets.QTableWidgetItem((row[4])))
            if int(row[5].split(":")[0]) >= int(24):
                row[5] = row[5][0:len(row[5]) - 1]
            self.DataTable.setItem(tableRows, 5, QtWidgets.QTableWidgetItem((row[5])))
            self.DataTable.setItem(tableRows, 6, QtWidgets.QTableWidgetItem((row[6])))
            self.DataTable.setItem(tableRows, 7, QtWidgets.QTableWidgetItem((row[7])))
            #self.DataTable.setItem(tableRows, 8, QtWidgets.QTableWidgetItem((row[8])))
            tableRows += 1


    
   #again init 
    def pushButton2_clicked(self):
        self.__init__()   
    
    #triger_searc
    def search_thread(self,datais, indextosort, value, column_to_search):
        data = self.searching_instance.LinearSearch(datais, indextosort, value, column_to_search)
        if len(data)>0:
            print('me')
            import unicodedata

            def remove_non_ascii(text):
                return ''.join(char for char in text if unicodedata.category(char)[0] != 'C')

            cleaned_data = [[remove_non_ascii(item) for item in row] for row in data]

            with open(r'C:\Users\hp\OneDrive\Desktop\resources\smashwordsorted.csv', mode='w', encoding='utf-8', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows(cleaned_data)
            self.load_DataFromFile(r'C:\Users\hp\OneDrive\Desktop\resources\smashwordsorted.csv')
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Please choose valid values ")
            msg.setWindowTitle("Invalid Input")
            msg.exec_()
            
    def trigger_searching(self, algorithm, column_to_search, value):
     try:
        
        datais=self.readdata()
        header=datais[0]
        indextosort=header.index(algorithm)
        
        
        thread = Thread(target=self.search_thread, args=(datais, indextosort, value, column_to_search))
        thread.start()

     except Exception as e:
            print(f"An error occurred: {e}")
            traceback.print_exc() 
    # multi search
    def multi(self,col1,col2,val1,val2):
        datais=self.readdata()
        header=datais[0]
        indextosort1=header.index(col1)
        indextosort2=header.index(col2)
        listofsearc=[(indextosort1,val1),(indextosort2,val2)]
        data=self.searching_instance.multi_level_search_2d(datais,listofsearc)
        
        if len(data)>0:
            print(data)
            with open(r'C:\Users\hp\OneDrive\Desktop\resources\smashwordsorted.csv', 'w', newline='', encoding='utf-8') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(data)
            self.load_DataFromFile('smashwordsorted.csv')
        
               
  #search ui
    def search(self):
     try:
        second_page=loadUi('a.ui')
        self.setCentralWidget(second_page)
        push_button = second_page.findChild(QPushButton, "pushButton")
        self.DataTable = second_page.tableWidget
        self.load_DataFromFile(r'C:\Users\hp\OneDrive\Desktop\Book1.csv')
        push_button.clicked.connect(
            lambda: self.trigger_searching(
                second_page.findChild(QWidget, "widget").findChild(QComboBox, "comboBox_2").currentText(),
                second_page.findChild(QWidget, "widget").findChild(QComboBox, "comboBox_3").currentText(),
                second_page.findChild(QWidget, "widget").findChild(QLineEdit, "lineEdit").text()
            ))
        push_button1=second_page.findChild(QWidget, "widget_5").findChild(QPushButton, "pushButton_5")
        push_button1.clicked.connect(
            lambda:self.multi(
                second_page.findChild(QWidget, "widget_5").findChild(QComboBox, "comboBox_4").currentText(),
                second_page.findChild(QWidget, "widget_5").findChild(QComboBox, "comboBox_5").currentText(),
                second_page.findChild(QWidget, "widget_5").findChild(QLineEdit, "lineEdit_2").text(),
                second_page.findChild(QWidget, "widget_5").findChild(QLineEdit, "lineEdit_3").text()
                
            )
        )
        self.searching_instance = Searching()

        push=second_page.findChild(QWidget, "widget_3").findChild(QPushButton, "pushButton_2")
        push.clicked.connect(self.pushButton2_clicked)
        push1=second_page.findChild(QWidget, "widget_3").findChild(QPushButton, "pushButton_3")
        push1.clicked.connect(self.pushButton_clicked)
        push2=second_page.findChild(QWidget, "widget_3").findChild(QPushButton, "pushButton_8")
        push2.clicked.connect(self.close)
        
     except Exception as e:
            print(f"An error occurred: {e}")
    #time display
    def time_display(self, lcd,time, result):
        if result:
           
            lcd.display(time)

    def sorting_thread(self, sorting_algorithm, datais, indextosort, ascending, callback):
        start_time = time.time()
        data = self.sorting_instance.callingfunction(sorting_algorithm, datais, indextosort, ascending)
        end_time = time.time()

        diff = end_time - start_time
        result = True
        callback(diff, result)
        with open(r'C:\Users\hp\OneDrive\Desktop\resources\smashwordsorted.csv', 'w', newline='', encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(data)

        print("Data sorted and saved to 'smashwordsorted.csv'")
        self.load_DataFromFile(r'C:\Users\hp\OneDrive\Desktop\resources\smashwordsorted.csv')

        
        

    def trigger_sorting(self,lcd, sorting_algorithm, column_to_sort, ascending):
        try:
            datais = self.readdata()
            datais = self.convert_columns_to_int(datais)
            header = datais[0]
            indextosort = header.index(column_to_sort)

            start_time = time.time()

            
            sorting_complete = False

            def callback(time_diff, result):
                nonlocal sorting_complete
                sorting_complete = True
                
                self.time_display(lcd,time_diff, result)

            thread_sort = Thread(target=self.sorting_thread, args=(sorting_algorithm, datais, indextosort, ascending, callback))

            thread_sort.start()

           
            self.root.after(100, lambda: self.check_sorting_complete(thread_sort, sorting_complete))

            end_time = time.time()
            diff = end_time - start_time

            return diff
        except Exception as e:
            print(f"An error occurred: {e}")
            traceback.print_exc()

    def check_sorting_complete(self, thread_sort, sorting_complete):
        if not sorting_complete:
           
            self.root.after(100, lambda: self.check_sorting_complete(thread_sort, sorting_complete))
 # sorting  ui
    def pushButton_clicked(self):
      try:  
        second_page = loadUi('PROJECT.ui')  
        self.setCentralWidget(second_page)
        lcd=second_page.findChild(QWidget,'widget_2').findChild(QLCDNumber,'lcdNumber')
        print(lcd)
        push3=second_page.findChild(QWidget, "widget_4").findChild(QPushButton, "pushButton_2")
        push3.clicked.connect(self.pushButton2_clicked)
        push4=second_page.findChild(QWidget, "widget_4").findChild(QPushButton, "pushButton_3")
        push4.clicked.connect(self.search)
        push5=second_page.findChild(QWidget, "widget_4").findChild(QPushButton, "pushButton_8")
        push5.clicked.connect(self.close)
        push_button = second_page.findChild(QWidget, "widget_3").findChild(QPushButton, "pushButtonofsingle")
        
        push_button.clicked.connect(
        
    lambda: self.handle_button_click(
        lcd,
        second_page.findChild(QWidget, "widget_3").findChild(QComboBox, "comboBox").currentText(),
        second_page.findChild(QWidget, "widget_3").findChild(QComboBox, "comboBox_2").currentText(),
        second_page.findChild(QWidget, "widget_3").findChild(QComboBox, "comboBox_3").currentText()
    )
)       
       
        
        self.DataTable = second_page.tableWidget
        self.load_DataFromFile(r'C:\Users\hp\OneDrive\Desktop\Book1.csv')
        push_button_multi = second_page.findChild(QWidget, "widget_3").findChild(QPushButton, "pushButtonofsingle_2")
        list_ofcheckoxes=[second_page.findChild(QWidget, "widget_3").findChild(QCheckBox, "checkBox"),
                          second_page.findChild(QWidget, "widget_3").findChild(QCheckBox, "checkBox_2"),
                          second_page.findChild(QWidget, "widget_3").findChild(QCheckBox, "checkBox_3"),
                          second_page.findChild(QWidget, "widget_3").findChild(QCheckBox, "checkBox_4"),
                          second_page.findChild(QWidget, "widget_3").findChild(QCheckBox, "checkBox_5"),
                          second_page.findChild(QWidget, "widget_3").findChild(QCheckBox, "checkBox_6"),
                          second_page.findChild(QWidget, "widget_3").findChild(QCheckBox, "checkBox_7"),
                          second_page.findChild(QWidget, "widget_3").findChild(QCheckBox, "checkBox_8")]
        
        push_button_multi.clicked.connect(lambda:self.multi_trigger_sorting(lcd,list_ofcheckoxes,
                                                                    second_page.findChild(QWidget, "widget_3").findChild(QComboBox, "comboBox_4").currentText()))


         
        self.sorting_instance = Sorting()      
      except Exception as e:
            print(f"An error occurred: {e}")
            
    #multi level integraation  
    def multi_sorting_thread(self,  datais, callback, list_of_texts, order):
        try:
            header = datais[0]
            indexes = [index for index, item in enumerate(header) if item in list_of_texts]

            start_time = time.time()
            
            data = self.sorting_instance.multi_sort(datais, indexes, order)

            end_time = time.time()
            diff = end_time - start_time
            result = True

            callback(diff, result)

            with open(r'C:\Users\hp\OneDrive\Desktop\resources\smashwordsorted.csv', 'w', newline='', encoding='utf-8') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(data)

            print("Data sorted and saved to 'smashwordsorted.csv'")
            self.load_DataFromFile(r'C:\Users\hp\OneDrive\Desktop\resources\smashwordsorted.csv')

        except Exception as e:
            print(f"An error occurred: {e}")
            traceback.print_exc()

    def multi_trigger_sorting(self, lcd,  checkboxes, order):
         try:
            datais = self.readdata()
            datais = self.convert_columns_to_int(datais)
          

            list_of_texts = [checkbox.text() for checkbox in checkboxes if checkbox.isChecked()]

            start_time = time.time()

            sorting_complete = False

            def callback(time_diff, result):
                nonlocal sorting_complete
                sorting_complete = True
                self.time_display(lcd, time_diff, result)

            thread_sort = Thread(target=self.multi_sorting_thread,args=( datais, callback, list_of_texts, order))

            thread_sort.start()

            self.root.after(100, lambda: self.check_sorting_complete(thread_sort, sorting_complete))

            end_time = time.time()
            diff = end_time - start_time

            return diff

         except Exception as e:
            print(f"An error occurred: {e}")
            traceback.print_exc()

    #validation 
    def handle_button_click(self,lcd, combo_1, combo_2, combo_3):
        ans=''
        if combo_1 != "none" and combo_2 != "none" and combo_3 != "none":
            if combo_1 in ["countingsort", "radixsort",'bucketsort']:
                valid_options = ["price", "words", "date"]
                if combo_2 not in valid_options:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText(f"For {combo_1}, valid options for the second combo are: {', '.join(valid_options)}.")
                    msg.setWindowTitle("Invalid Input")
                    msg.exec_()
                else:
                    ans=self.trigger_sorting(lcd,combo_1, combo_2, combo_3)
                    
            else:
                self.trigger_sorting(lcd,combo_1, combo_2, combo_3)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Please choose valid values in all ComboBoxes.")
            msg.setWindowTitle("Invalid Input")
            msg.exec_()
        return ans
    #scarping funation
    
    def start_scraping(self):
        
        thread=Thread(target=main,daemon=True,args=(True,True,'https://www.smashwords.com/books/category/1/newest/0/any/any/95000','https://www.smashwords.com/books/category/1/newest/0/any/any/'))
        thread.start()

    def stop_scraping(self):
        main(False,True,'https://www.smashwords.com/books/category/1/newest/0/any/any/95000','https://www.smashwords.com/books/category/1/newest/0/any/any/')
        self.DataTable = self.tableWidget
        self.load_DataFromFile('smashwordsorted1.csv')
        
        
    def pause(self):
        
        with open(r'C:\Users\hp\OneDrive\Desktop\resources\smashwordsortedurl.txt', 'r',encoding='utf-8') as file:
            content=file.read()
        print(content)
        main(True,False,content,'https://www.smashwords.com/books/category/1/newest/0/any/any/')
        self.DataTable = self.tableWidget
        self.load_DataFromFile('smashwordsorted1.csv')
    def resume(self):
            with open(r'C:\Users\hp\OneDrive\Desktop\resources\smashwordsortedurl.txt', 'r',encoding='utf-8') as file:
                content=file.read()
            thread=Thread(target=main,daemon=True,args=(True,True,content,'https://www.smashwords.com/books/category/1/newest/0/any/any/'))
            thread.start()
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())

