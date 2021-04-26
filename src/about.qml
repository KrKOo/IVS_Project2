import QtQuick 2.13
import QtQuick.Window 2.13
import QtQuick.Controls 2.3

ApplicationWindow {
    id: helpWindow
    width: 400
    height: 250
    visible: false
    title: qsTr("About")
    minimumWidth: 300
    minimumHeight: 250
    Text {
        anchors.fill: parent
        wrapMode: Text.WordWrap
        padding: 10
        textFormat: Text.RichText
        text: "
            <h1>About</h1>
            <p>Aplikácia PyCalc je jednoduchá kalkulačka, ktorá bola vyvinutá v programovacom jazyku Python. 
            Kalkulačka bola vytvorená v rámci školského projektu. Aplikácia zvláda základné matematické operácie, ako aj 
            odmocninu, mocninu, faktoriál a výpočet zvyšku po delení - modulo. 
            </p>"

    }
}
