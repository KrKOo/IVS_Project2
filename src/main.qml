import QtQuick 2.13
import QtQuick.Window 2.13
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.0
import QtGraphicalEffects 1.0
import QtQuick.Dialogs 1.1

ApplicationWindow {
    id: window
    width: 400
    height: 500
    visible: true
    title: qsTr("Calculator")
    minimumWidth: 300
    minimumHeight: 400
    property var helpComponent : Qt.createComponent("help.qml")
    property var helpWindow    : helpComponent.createObject("helpWindow")
    property var aboutComponent: Qt.createComponent("about.qml")
    property var aboutWindow   : aboutComponent.createObject("aboutWindow")
    onClosing: {
        helpWindow.close();
        aboutWindow.close();
    }

    menuBar: MenuBar {
        contentHeight: 2
        Menu {
                title: "Help"
                MenuItem {
                    text: "Manual"
                    onTriggered: {
                        helpWindow.show()
                    }
                }

                MenuItem {
                    text: "About"
                    onTriggered: {
                        aboutWindow.show()
                    }
                }
            }
        }

    Component{
        id: myButton

        Button {
            id: btn;
            property var buttonWidth: (buttonGrid.width/buttonGrid.columns) - (buttonGrid.columns * buttonGrid.columnSpacing)
            property var buttonHeight: (buttonGrid.height/buttonGrid.rows) - (buttonGrid.rows * buttonGrid.rowSpacing)
            property var size: Math.min(buttonWidth, buttonHeight)

            implicitWidth: size
            implicitHeight: size
            focusPolicy: Qt.NoFocus
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
        rows: 5
        columns: 5

        Loader {
            id: btnRoot
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "<sup>y</sup>√x"
                this.item.objectName = "btnRoot"
            }
        }
        Loader {
            id: btnFact
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "x!"
                this.item.objectName = "btnFact"
            }
        }
        Loader {
            id: btnMod
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "%"
                this.item.objectName = "btnMod"
            }
        }
        Loader {
            id: btnClear
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "CE"
                this.item.objectName = "btnClear"
            }
        }
        Loader {
            id: btnDel
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "DEL"
                this.item.objectName = "btnDel"
            }
        }
        Loader {
            id: btnPower
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "x<sup>y</<sup>"
                this.item.objectName = "btnPower"
            }
        }
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
            id: btnDiv
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "/"
                this.item.objectName = "btnDiv"
            }
        }
        Loader {
            id: btnPi
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "π"
                this.item.objectName = "btnPi"
            }
        }
        Loader {
            id: btn4
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "4"
                this.item.objectName = "btn4"
            }
        }
        Loader {
            id: btn5
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "5"
                this.item.objectName = "btn5"
            }
        }
        Loader {
            id: btn6
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "6"
                this.item.objectName = "btn6"
            }
        }
        Loader {
            id: btnMul
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "*"
                this.item.objectName = "btnMul"
            }
        }
        Loader {
            id: btnEul
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "e"
                this.item.objectName = "btnEul"
            }
        }
        Loader {
            id: btn1
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "1"
                this.item.objectName = "btn1"
            }
        }
        Loader {
            id: btn2
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "2"
                this.item.objectName = "btn2"
            }
        }
        Loader {
            id: btn3
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "3"
                this.item.objectName = "btn3"
            }
        }
        Loader {
            id: btnSub
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "-"
                this.item.objectName = "btnSub"
            }
        }
        Loader {
            id: btnAns
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "Ans"
                this.item.objectName = "btnAns"
            }
        }
        Loader {
            id: btn0
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "0"
                this.item.objectName = "btn0"
            }
        }

        Loader {
            id: btnFloat
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            sourceComponent: myButton
            onLoaded: {
                this.item.text = "."
                this.item.objectName = "btnFloat"
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

        TextInput {
            id: displayEquation
            objectName: "equation"
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            horizontalAlignment: Text.AlignRight
            verticalAlignment: Text.AlignBottom
            activeFocusOnPress: true
            selectByMouse: true
            readOnly: true
            leftPadding: 5
            rightPadding: 5
            clip: true
            height: (parent.height/3)
            font.pointSize: {return Math.max(1, Math.min(width/10, height/2))}
            font.family: "Tahoma"
            color: "#adadad"
        }

        TextInput {
            id: displayText
            objectName: "display"
            anchors.top: displayEquation.bottom
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.bottom: parent.bottom
            horizontalAlignment: Text.AlignRight
            verticalAlignment: Text.AlignBottom
            focus: true
            selectByMouse: true
            leftPadding: 5
            rightPadding: 5
            height: (parent.height/3)*2
            font.pointSize: {return Math.max(1, Math.min(width/10, height/2))}
            font.family: "Tahoma"
            color: "#454545"
            validator: RegExpValidator { regExp: /[+-]?([0-9]*[.])?[0-9]+/ }
            maximumLength: 13
        }
    }
}
