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

# Import from config files (ide warns cause not used, but it is used)
from mouse import mouse
from keys import keys
from groups import groups
from layouts import layouts, floating_layout
from screens import screens, extension_defaults, widget_defaults
from hooks import *


#################################
#        Basic settings         #
#################################
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = False
wl_input_rules = None
wmname = "Qtile"
