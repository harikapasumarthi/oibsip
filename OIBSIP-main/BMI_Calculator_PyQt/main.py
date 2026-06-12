import sys
from ui.form import *

class MyForm(QtWidgets.QDialog):
 def __init__(self, parent=None):
     QtWidgets.QWidget.__init__(self, parent)
     self.ui = Ui_Dialog()
     self.ui.setupUi(self)
     self.ui.pbtCalculate.clicked.connect(self.BMI)
     self.setStyleSheet("background: #70BDCF")
     self.ui.lneHeight.setStyleSheet("border: 1px solid white; border-radius: 9px; background: #aed9e0")
     self.ui.lneWeight.setStyleSheet("border: 1px solid white; border-radius: 9px; background: #aed9e0")
     self.ui.pbtCalculate.setStyleSheet("border: 1px solid white; border-radius: 9px; background: #aed9e0")

 def BMI(self):
    height = self.ui.lneHeight.text()
    weight = self.ui.lneWeight.text()
    bmi = int(weight) / ((int(height) /100) ** 2)   
    accuracy = round(bmi, 2)

    if accuracy < 18.5:
        range = "You are underweight"
        self.setStyleSheet("background-color: #3498db;")
    elif (accuracy > 18.5) & (accuracy < 24.9):
        range = "You have normal weight"
        self.setStyleSheet("background-color: #2ecc71;")
    elif (accuracy > 25) & (accuracy < 29.9):
        range = "You are overweight"
        self.setStyleSheet("background-color: #f1c40f;")
    else:
       range = "You are obese"
       self.setStyleSheet("background-color: #e67e22;")
    self.ui.lblResult.setText("BMI is "+ str(accuracy) + ". " + range)

if __name__ == "__main__":
 app = QtWidgets.QApplication(sys.argv)
 myapp = MyForm()
 myapp.show()
 sys.exit(app.exec_())