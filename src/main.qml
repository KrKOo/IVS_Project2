import QtQuick 2.13
import QtQuick.Window 2.13
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.0
import QtGraphicalEffects 1.0


ApplicationWindow {
    id: window
    width: 400
    height: 400
    visible: true
    title: qsTr("Calculator")
    minimumWidth: 300
    minimumHeight: 350

    Component{
        id: myButton

        Button {
            id: btn;
            property var buttonWidth: (buttonGrid.width/buttonGrid.columns) - (buttonGrid.columns * buttonGrid.columnSpacing)
            property var buttonHeight: (buttonGrid.height/buttonGrid.rows) - (buttonGrid.rows * buttonGrid.rowSpacing)
            property var size: Math.min(buttonWidth, buttonHeight)

            implicitWidth: size
            implicitHeight: size
            background: Rectangle{
                width: size;
                height: size;
                radius: size/2;
                color: btn.down ? "#f2f2f2" : "white"
            }
            layer.enabled: true
            layer.effect: Glow {
                samples: 10
                color: "#ebebeb"
                transparentBorder: true
            }
            contentItem: Text {
                textFormat: Text.RichText
                text: btn.text
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                font.pointSize: size/4
                font.weight: Font.Thin
                font.family: "Tahoma"
                color: "#5c5c5c"
            }
        }
    }

    GridLayout {
        id: buttonGrid
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: display.bottom
        anchors.bottom: parent.bottom
        anchors.rightMargin: 5
        anchors.leftMargin: 5
        anchors.topMargin: 5
        anchors.bottomMargin: 5
        Layout.fillHeight: true
        Layout.fillWidth: true
        Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
        columnSpacing: 2
        rowSpacing: 2
        rows: 4
        columns: 5

        Loader {
            id: btn7
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "7"
                this.item.objectName = "btn7"
            }
        }
        Loader {
            id: btn8
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "8"
                this.item.objectName = "btn8"
            }
        }
        Loader {
            id: btn9
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "9"
                this.item.objectName = "btn9"
            }
        }
        Loader {
            id: btnPower
            Layout.margins: 0
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "x<sup>y</<sup>"
                this.item.objectName = "btnPower"
            }
        }
        Loader {
            id: btnRoot
            Layout.margins: 0
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "√"
                this.item.objectName = "btnRoot"
            }
        }
        Loader {
            id: btn4
            Layout.margins: 0
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "4"
                this.item.objectName = "btn4"
            }
        }
        Loader {
            id: btn5
            Layout.margins: 0
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "5"
                this.item.objectName = "btn5"
            }
        }
        Loader {
            id: btn6
            Layout.margins: 0
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "6"
                this.item.objectName = "btn6"
            }
        }
        Loader {
            Layout.margins: 0
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "!"
                this.item.objectName = "btnFactorial"
            }
        }
        Loader {
            id: btnDiv
            Layout.margins: 0
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "/"
                this.item.objectName = "btnDiv"
            }
        }
        Loader {
            id: btn1
            Layout.margins: 0
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "1"
                this.item.objectName = "btn1"
            }
        }
        Loader {
            id: btn2
            Layout.margins: 0
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "2"
                this.item.objectName = "btn2"
            }
        }
        Loader {
            id: btn3
            Layout.margins: 0
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "3"
                this.item.objectName = "btn3"
            }
        }
        Loader {
            id: btnSub
            Layout.margins: 0
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "-"
                this.item.objectName = "btnSub"
            }
        }
        Loader {
            id: btnMul
            Layout.margins: 0
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "*"
                this.item.objectName = "btnMul"
            }
        }
        Loader {
            id: btn0
            Layout.margins: 0
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "0"
                this.item.objectName = "btn0"
            }
        }

        Loader {
            id: btnFloat
            Layout.margins: 0
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "."
                this.item.objectName = "btnFloat"
            }
        }
        Loader {
            id: btnMod
            Layout.margins: 0
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "%"
                this.item.objectName = "btnMod"
            }
        }
        Loader {
            id: btnAdd
            Layout.margins: 0
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "+"
                this.item.objectName = "btnAdd"
            }
        }
        Loader {
            id: btnResult
            Layout.margins: 0
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "="
                this.item.objectName = "btnResult"
            }
        }
    }

    Item{
        id: display
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
        height: {return Math.min(width/4, 150)}

        Rectangle {
            color: "#f2f2f2"
            anchors.fill: parent
        }
        TextEdit {
            id: displayText
            objectName: "display"
            anchors.fill: parent
            horizontalAlignment: Text.AlignRight
            verticalAlignment: Text.AlignBottom
            font.pointSize: {return Math.max(1, Math.min(width/10, height/2))}
            font.family: "Tahoma"
        }
    }
}
