import sys
import os
import signal
from enum import Enum

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import Qt, QObject, QEvent

import mathlib

##
# @file calculator.py
# @brief Implementation of the connection to gui.
# @author Kristián Kováč xkovac61 @author Martin Kozák
# Date: 18.4.2021


class Operation(Enum):
    ADD = 1
    SUB = 2
    MUL = 3
    DIV = 4
    ROOT = 5
    POW = 6
    MOD = 7
    FACT = 8


class Calculator():
    operation = 0
    prevNumber = 0
    lastResult = 0
    clearNext = False

    operations = {Operation.ADD: "+",
                  Operation.SUB: "-",
                  Operation.MUL: "*",
                  Operation.DIV: "/",
                  Operation.ROOT: "root of",
                  Operation.POW: "^",
                  Operation.MOD: "%",
                  Operation.FACT: "!"}

    def __init__(self, display, equation):
        self.display = display
        self.equation = equation
    
    def appedToDisplay(self, num):
        text = display.property("text")
        if self.clearNext or text == "Error":
            text = ""

        if len(text) < 10:
            if num == ".":
                if "." not in text:
                    text += num
            else:
                text += str(num)
        

        display.setProperty("text", text)
        self.clearNext = False

        if self.operation == Operation.SUB and (self.prevNumber == "" or self.prevNumber == "Error"):
            self.prevNumber = 0
            self.displayResult()

    def setDisplay(self, num):
        display.setProperty("text", str(num))
        self.clearNext = False

    def clearDisplay(self):
        display.setProperty("text", "")
        equation.setProperty("text", "")
        self.operation = 0

    def delLastNumber(self):
        text = display.property("text")
        display.setProperty("text", text[:-1])
        equation.setProperty("text", "")
    
    def setAns(self):
        display.setProperty("text", self.lastResult)

    def setOperation(self, operation):
        self.prevNumber = self.displayResult()        
        self.operation = operation
        
        if isinstance(self.prevNumber,str):
            if self.prevNumber == "" or self.prevNumber == "Error": 
                if self.operation != Operation.SUB:
                    self.operation = 0

        if(operation == Operation.FACT):
            self.displayResult(True)
        self.clearNext = True

    def calculateResult(self, currentNumber):
        
        if self.operation == Operation.ADD:
            return mathlib.add(self.prevNumber, currentNumber)
        if self.operation == Operation.SUB:
            return mathlib.sub(self.prevNumber, currentNumber)
        if self.operation == Operation.MUL:
            return mathlib.mul(self.prevNumber, currentNumber)
        if self.operation == Operation.DIV:     
            return mathlib.div(self.prevNumber, currentNumber)
        if self.operation == Operation.ROOT:    
            return mathlib.nth_root(currentNumber, self.prevNumber)
        if self.operation == Operation.POW:     
            return mathlib.pow(self.prevNumber, currentNumber)
        if self.operation == Operation.MOD:     
            return mathlib.mod(self.prevNumber, currentNumber)
        if self.operation == Operation.FACT:
            if currentNumber > 100:
                raise ValueError("{} is too big number for factorial.".format(currentNumber))    
            return mathlib.fact(currentNumber)

        return currentNumber

    def displayError(self):
        self.display.setProperty("text", "Error")

    def displayEquation(self, second, result):
        if self.operation == 0:
            return
        elif self.operation == Operation.FACT:
            eqn = format(self.prevNumber,'.10g')
            eqn += self.operations[self.operation]
            self.equation.setProperty("text", eqn)
        else:
            eqn = format(self.prevNumber,'.10g')
            eqn += " " + self.operations[self.operation] + " "
            eqn += format(second,'.10g') + " ="
            self.equation.setProperty("text", eqn)

    def displayResult(self, resultBtnPress = False):
        value = self.display.property("text")
        result = 0.0

        
        if value == "" or value == "Error":
            return value
        else:
            value = float(value)

        try:
            result = self.calculateResult(value)
        except (ZeroDivisionError, ValueError, OverflowError):
            self.displayError();
            self.operation = 0
            self.clearNext = False
            return result

        result = round(result, 8)
        if len(format(result,'.10g')) <= 10:
            self.display.setProperty("text", result)
        else:
            result = float("{0:.4e}".format(result))
            self.display.setProperty("text", result)

        
        if resultBtnPress or self.operation != 0:
            self.displayEquation(value,result)
            self.lastResult = result
        self.operation = 0
        self.clearNext = True
        return result
       
class KeyPressFilter(QObject):
    def eventFilter(self, obj, e):
        if e.type() == QEvent.KeyPress:
            if e.key() == Qt.Key_0:
                calculator.appedToDisplay("0")
            elif e.key() == Qt.Key_1:
                calculator.appedToDisplay("1")
            elif e.key() == Qt.Key_2:
                calculator.appedToDisplay("2")
            elif e.key() == Qt.Key_3:
                calculator.appedToDisplay("3")
            elif e.key() == Qt.Key_4:
                calculator.appedToDisplay("4")
            elif e.key() == Qt.Key_5:
                calculator.appedToDisplay("5")
            elif e.key() == Qt.Key_6:
                calculator.appedToDisplay("6")
            elif e.key() == Qt.Key_7:
                calculator.appedToDisplay("7")
            elif e.key() == Qt.Key_8:
                calculator.appedToDisplay("8")
            elif e.key() == Qt.Key_9:
                calculator.appedToDisplay("9")

            elif e.key() ==  Qt.Key_Plus:
                calculator.setOperation(Operation.ADD)
            elif e.key() == Qt.Key_Minus:
                calculator.setOperation(Operation.SUB)
            elif e.key() == Qt.Key_Asterisk:
                calculator.setOperation(Operation.MUL)
            elif e.key() == Qt.Key_Slash:
                calculator.setOperation(Operation.DIV)

            elif (e.key() == Qt.Key_Return) or (e.key() == Qt.Key_Enter):
                calculator.displayResult(True)
            elif e.key() == Qt.Key_Backspace:
                calculator.delLastNumber()
            elif e.key() == Qt.Key_Delete:
                calculator.clearDisplay()
            elif e.key() == Qt.Key_Escape:
                sys.exit(0)
            return True
        else:
            return QObject.eventFilter(self, obj, e)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    path = os.path.join(os.path.dirname(__file__), "main.qml")
    engine.load(path)

    window = engine.rootObjects()[0]

    keyPressFilter = KeyPressFilter(window)
    window.installEventFilter(keyPressFilter)

    btn0 = window.findChild(QObject, "btn0")
    btn1 = window.findChild(QObject, "btn1")
    btn2 = window.findChild(QObject, "btn2")
    btn3 = window.findChild(QObject, "btn3")
    btn4 = window.findChild(QObject, "btn4")
    btn5 = window.findChild(QObject, "btn5")
    btn6 = window.findChild(QObject, "btn6")
    btn7 = window.findChild(QObject, "btn7")
    btn8 = window.findChild(QObject, "btn8")
    btn9 = window.findChild(QObject, "btn9")
    btnFloat = window.findChild(QObject, "btnFloat")

    btnAdd = window.findChild(QObject, "btnAdd")
    btnSub = window.findChild(QObject, "btnSub")
    btnMul = window.findChild(QObject, "btnMul")
    btnDiv = window.findChild(QObject, "btnDiv")
    btnFact = window.findChild(QObject, "btnFact")
    btnMod = window.findChild(QObject, "btnMod")
    btnPow = window.findChild(QObject, "btnPower")
    btnRoot = window.findChild(QObject, "btnRoot")
    btnPi = window.findChild(QObject, "btnPi")
    btnEul = window.findChild(QObject, "btnEul")

    btnClear = window.findChild(QObject, "btnClear")
    btnDel = window.findChild(QObject, "btnDel")
    btnAns = window.findChild(QObject, "btnAns")
    btnResult = window.findChild(QObject, "btnResult")
    
    equation = window.findChild(QObject, "equation")
    display = window.findChild(QObject, "display")


    calculator = Calculator(display,equation)

    btn0.clicked.connect(lambda: calculator.appedToDisplay(0))
    btn1.clicked.connect(lambda: calculator.appedToDisplay(1))
    btn2.clicked.connect(lambda: calculator.appedToDisplay(2))
    btn3.clicked.connect(lambda: calculator.appedToDisplay(3))
    btn4.clicked.connect(lambda: calculator.appedToDisplay(4))
    btn5.clicked.connect(lambda: calculator.appedToDisplay(5))
    btn6.clicked.connect(lambda: calculator.appedToDisplay(6))
    btn7.clicked.connect(lambda: calculator.appedToDisplay(7))
    btn8.clicked.connect(lambda: calculator.appedToDisplay(8))
    btn9.clicked.connect(lambda: calculator.appedToDisplay(9))
    btnFloat.clicked.connect(lambda: calculator.appedToDisplay('.'))
    btnEul.clicked.connect(lambda: calculator.setDisplay('2.71828182'))
    btnPi.clicked.connect(lambda: calculator.setDisplay('3.14159265'))
    btnClear.clicked.connect(lambda: calculator.clearDisplay())
    btnDel.clicked.connect(lambda: calculator.delLastNumber())
    btnAns.clicked.connect(lambda: calculator.setAns())

    btnAdd.clicked.connect(lambda: calculator.setOperation(Operation.ADD))
    btnSub.clicked.connect(lambda: calculator.setOperation(Operation.SUB))
    btnMul.clicked.connect(lambda: calculator.setOperation(Operation.MUL))
    btnDiv.clicked.connect(lambda: calculator.setOperation(Operation.DIV))
    btnRoot.clicked.connect(lambda: calculator.setOperation(Operation.ROOT))
    btnPow.clicked.connect(lambda: calculator.setOperation(Operation.POW))
    btnMod.clicked.connect(lambda: calculator.setOperation(Operation.MOD))
    btnFact.clicked.connect(lambda: calculator.setOperation(Operation.FACT))
    btnResult.clicked.connect(lambda: calculator.displayResult(True))

    # Set display text
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
