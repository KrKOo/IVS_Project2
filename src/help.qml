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
    minimumHeight: 400
    Text {
        anchors.fill: parent
        wrapMode: Text.WordWrap
        padding: 10
        textFormat: Text.RichText
        text: "
            <h1>Manual</h1>
            <p>Wafer apple pie muffin cake halvah fruitcake dessert caramels brownie. Macaroon liquorice chupa chups I love dragée donut danish.
            Apple pie sugar plum muffin dragée jelly-o cookie. Cotton candy tart chupa chups jelly beans.

            I love chocolate liquorice brownie. Fruitcake oat cake tart cookie croissant danish tootsie roll I love ice cream.
            Gingerbread oat cake marshmallow topping bonbon cupcake liquorice.

            Brownie bear claw jelly beans. Chupa chups bonbon dragée. Sesame snaps cake biscuit halvah toffee.
            I love cake jujubes lollipop chocolate bar marzipan apple pie.

            Gummies tart halvah wafer sugar plum halvah I love jelly-o biscuit.
            Marzipan cupcake croissant sweet marzipan dragée tart sweet liquorice. Cookie donut candy I love.
            Chocolate bar jelly-o tart oat cake.

            I love apple pie sesame snaps biscuit danish gummi bears I love.
            Bear claw tiramisu jujubes icing biscuit.
            Sweet roll jelly candy canes sesame snaps oat cake donut chocolate chocolate cake.</p>" //TODO: write manual text

    }
}
