from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import sys
import csv
class Searching(QMainWindow):
    def _init_(self):
        super(Searching, self)._init_()

    def LinearSearch(self,array, column_name, filter, Type):
         try:
            result = []
            
            for row in array:
                
                if len(row) > column_name:
                    
                    
                    value = row[column_name]
                    
                    
                    if Type == 'starts_with' and value.startswith(filter):
                        result.append(row)
                    elif Type == 'ends_with' and value.endswith(filter):
                        result.append(row)
                    elif Type == 'contains' and filter in value:
                        result.append(row)
            
            return result
         except Exception as e:
            print(f"An error occurred: {e}")
    def multi_level_search_2d(self,data, search_criteria):

        search_results = []

    
        for row in data:
            if all(row[column] == value for column, value in search_criteria):
                search_results.append(row)

        return search_results


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Searching()
    window.show()
    sys.exit(app.exec_())