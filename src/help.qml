import QtQuick 2.13
import QtQuick.Window 2.13
import QtQuick.Controls 2.3

ApplicationWindow {
    id: helpWindow
    width: 400
    height: 350
    visible: false
    title: qsTr("Help")
    minimumWidth: 300
    minimumHeight: 350
    Text {
        anchors.fill: parent
        wrapMode: Text.WordWrap
        padding: 10
        textFormat: Text.RichText
        text: "
            <h1>Manual</h1>
            <p>Kalkulačka pracuje vždy s dvoma číslami. Najprv sa zadajte prvé číslo, potom
            stlačte operátor a zadajte druhé číslo. Následne sa vyhodnotí výsledok stlačením tlačidla \"=\". Tlačidlo \"CE\" vymaže displeje,
            \"Ans\" zobrazí posledný výsledok a \"DEL\" maže číslice. Faktoriál je jednočíselná operácia. Pre odmocninu
            sa najprv zadáva odmocniteľ \"y\" a potom základ odmocniny. Pre mocninu sa zadáva najprv základ mocniny
            a potom exponent.
            </p>" 

    }
}
