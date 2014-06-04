/*
 * Copyright 2014 Canonical Ltd.
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; version 3.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

import QtQuick 2.0
import Ubuntu.Components 1.0

AbstractButton {
    property alias iconWidth: icon.width
    property alias iconHeight: icon.height
    property alias iconName: icon.name
    property alias iconColor: icon.color

    width: units.gu(4)
    height: units.gu(4)

    Icon {
        id: icon
        anchors.centerIn: parent
        width: parent.width
        height: parent.height
        color: "white"
    }
}

