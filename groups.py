# Customizable qtile configuration
# Copyright (C) 2023  mbajdik
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os

from libqtile.config import Group, ScratchPad, DropDown, Key, Match
from libqtile.lazy import lazy

from keys import keys
from settings import group_config, dropdowns, mod, shift, group_switch_on_move


#################################
#            Groups             #
#################################
# Method to get groups from the format in the settings file
def get_groups():
    out = []

    for g in group_config:
        name = g[0]
        label = g[1]
        layout = g[2]
        matches = []
        for m in g[3]:
            matches.append(Match(wm_class=m))
        out.append(Group(name=name, label=label, layout=layout, matches=matches))

    return out


# Get group settings from the settings file
groups = get_groups()

# Add keys to manage groups
for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name)
            ),
            Key(
                [mod, shift],
                i.name,
                lazy.window.togroup(i.name, switch_group=group_switch_on_move),
                desc="Switch"
            ),
        ]
    )


#################################
#          Scratchpads          #
#################################
# Get scratchpad (drop-down) list
def get_dropdowns():
    out = []

    for dd in dropdowns:
        name = dd[2]
        command = dd[3]
        width = dd[4]
        height = dd[5]
        x = (1 - width) / 2
        y = (1 - height) / 2
        opacity = dd[6] if len(dd) >= 7 else 1

        out.append(DropDown(name, command, width=width, height=height, x=x, y=y, opacity=opacity))

    return out


# Add scratchpad with dropdowns and add it to the groups
groups.append(ScratchPad("scratchpad", get_dropdowns()))
