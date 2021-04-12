import sys
import os
import signal

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QObject


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    path = os.path.join(os.path.dirname(__file__), "main.qml")
    engine.load(path)

    window = engine.rootObjects()[0]

    # Button demo

    # button = window.findChild(QObject, "btn1")
    # button.clicked.connect(lambda: print("Hello World!"))

    # Set display text
    display = window.findChild(QObject, "display")
    display.setProperty("text", "1234")

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
