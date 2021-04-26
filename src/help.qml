import QtQuick 2.13
import QtQuick.Window 2.13
import QtQuick.Controls 2.3

ApplicationWindow {
    id: helpWindow
    width: 400
    height: 500
    visible: false
    title: qsTr("Help")
    minimumWidth: 300
    minimumHeight: 500
    Text {
        anchors.fill: parent
        wrapMode: Text.WordWrap
        padding: 10
        textFormat: Text.RichText
        horizontalAlignment: Text.AlignJustify
        text: "
            <h1>Manual</h1>
            <p>Pri dvojčíselných operáciach pracuje kalkulačka s dvoma číslami. Najprv zadajte prvé číslo, potom
            stlačte operátor a zadajte druhé číslo. Pri jednočíselných operáciach napíšte číslo a stlačte operátor.
            Následne sa vyhodnotí výsledok stlačením tlačidla <b>=</b>. <br><br>
            <b>CE</b> - vymaže displej<br/>
            <b>Ans</b> - zobrazí posledný výsledok<br/>
            <b>DEL</b> - vymaže poslednú číslicu<br/>
            <b>x!</b> - jednočíselná operácia pre rátanie faktoriálu z <b>x</b><br/>
            <b>%</b> - dvojčíselná operácia pre vyrátanie zvyšku po delení prvého čísla druhým číslom<br/>
            <b><sup>y</sup>√x</b> - dvojčíselná operácia, pred stlačením odmocniny zadajte odmocniteľa <b>y</b>. Po stlační odmocniny zadajte základ <b>x</b><br/>
            <b>x<sup>y</sup></b> - dvojčíselná operácia, pred stlačením mocniny zadajte základ mocniny, po stlačení mocniny zadajte exponent<br/>
            </p>"

    }
}
