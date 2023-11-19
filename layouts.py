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

from libqtile import layout
from libqtile.config import Match

from settings import wm_border_width, wm_margin, wm_border_normal, wm_border_focus, \
    floating_window_titles, floating_window_classes


#################################
#            Themes             #
#################################
columns_theme = {
    "border_focus": wm_border_focus,
    "border_normal": wm_border_normal,
    "border_width": wm_border_width,
    "margin": wm_margin,
    "border_on_single": True,
}

default_theme = {
    "border_focus": wm_border_focus,
    "border_normal": wm_border_normal,
    "border_width": wm_border_width,
    "margin": wm_margin,
}


#################################
#        Enabling layouts       #
#################################
layouts = [
    # layout.MonadWide(),
    # layout.Bsp(),
    # layout.Stack(stacks=2),
    # layout.RatioTile(),
    # layout.Tile(shift_windows=True),
    # layout.VerticalTile(),
    # layout.Matrix(),
    # layout.Zoomy(),
    # layout.Stack(num_stacks=2),
    # layout.RatioTile(),
    # layout.TreeTab(),
    # layout.MonadTall(),
    # layout.Floating(),

    # Used layouts
    layout.Max(**default_theme),
    layout.Columns(**columns_theme),
]


#################################
#        Floating layout        #
#################################
# Method to get the windows which need to be floating by default
def get_float_rules():
    out = []
    out.extend(layout.Floating.default_float_rules)

    for clazz in floating_window_classes:
        out.append(Match(wm_class=clazz))

    for title in floating_window_titles:
        out.append(Match(title=title))

    return out


floating_theme = {
    "border_focus": wm_border_focus,
    "border_normal": wm_border_normal,
    "border_width": wm_border_width,
}

floating_layout = layout.Floating(
    **floating_theme,
    float_rules=get_float_rules()
)
