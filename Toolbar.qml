import QtQuick 1.1
import "CameraEnums.js" as CameraEnums

Rectangle {
    id: toolbar
    color: "#30000000"

    property Camera camera

    Behavior on y { NumberAnimation { duration: 500 } }

    Column {
        anchors.left: parent.left
        anchors.bottom: parent.bottom
        width: 50
        height: childrenRect.height
        spacing: 50

        ToolbarButton {
            anchors.left: parent.left
            source: "assets/record_off.png"

            onClicked: console.log("click")
        }

        FlashButton {
            anchors.left: parent.left
            state: { switch (camera.flashMode) {
                case CameraEnums.FlashModeOff: return "off";
                case CameraEnums.FlashModeOn: return "on";
                case CameraEnums.FlashModeAuto:
                default: return "auto";
            }}

            onClicked: { switch (state) {
                case "off": camera.flashMode = CameraEnums.FlashModeOn; break;
                case "on": camera.flashMode = CameraEnums.FlashModeAuto; break;
                case "auto":
                default: camera.flashMode = CameraEnums.FlashModeOff; break;
            }}
        }
    }

    Column {
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        width: 50
        height: childrenRect.height
        spacing: 50

        ToolbarButton {
            anchors.right: parent.right
            source: "assets/swap_camera.png"
        }

        ToolbarButton {
            anchors.right: parent.right
            source: "assets/gallery.png"
        }
    }

    Item {
        anchors.bottom: parent.bottom
        anchors.left: parent.left
        anchors.right: parent.right
        height: 50

        ToolbarButton {
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.bottom: parent.bottom

            source: "assets/zoom.png"
        }
    }
}
