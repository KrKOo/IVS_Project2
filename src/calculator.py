import sys
import os
import signal
from enum import Enum

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QObject

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

    def __init__(self, display):
        self.display = display
        self.error = False

    def appedToDisplay(self, num):
        text = display.property("text")
        if(self.clearNext):
            text = ""

        if len(text) < 10:
            text += str(num)
        
        display.setProperty("text", text)
        self.clearNext = False

        if self.operation == Operation.SUB and self.prevNumber == "":
            self.prevNumber = 0
            self.displayResult()

    def setDisplay(self, num):
        display.setProperty("text", str(num))
        self.clearNext = False

    def clearDisplay(self):
        display.setProperty("text", "")
        self.operation = 0

    def delLastNumber(self):
        text = display.property("text")
        display.setProperty("text", text[:-1])
    
    def setAns(self):
        display.setProperty("text", str(self.lastResult))

    def setOperation(self, operation):
        self.prevNumber = self.displayResult()
        self.operation = operation
        
        if isinstance(self.prevNumber,str):
            self.operation = 0

        if(operation == Operation.FACT):
            self.displayResult()
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

    def displayResult(self, resultBtnPress = False):
        value = self.display.property("text")
        result = 0

        if value == "" or value == "Error":
            return ""
        else:
            value = float(value)

        try:
            result = self.calculateResult(value)
        except (ZeroDivisionError, ValueError):
            self.displayError();
            self.clearNext = False
            return result
        
        result = round(result, 8)
        if len(str(result)) <= 10:
            self.display.setProperty("text", result)
        else:
            result = "{0:.4e}".format(result)
            self.display.setProperty("text", result)

        self.operation = 0
        self.clearNext = True
        if(resultBtnPress):
            self.lastResult = result
        return result
        


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    path = os.path.join(os.path.dirname(__file__), "main.qml")
    engine.load(path)

    window = engine.rootObjects()[0]

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

    display = window.findChild(QObject, "display")

    calculator = Calculator(display)
 
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
