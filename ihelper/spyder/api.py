# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2021, gepcel
#
# Licensed under the terms of the MIT license
# ----------------------------------------------------------------------------
"""
ihelper: A spyder plugin to get help information from ipython console in editor.
"""


class IHelperActions:
    ShortcutAction = 'request help from console'
    ToolbarClickAction = 'Click to show help from console'
    InspectCurrentObject = 'request help from console'


class IHelperToolbarSections:
    First = 'first_section'


class IHelperWidgets:
    StatusWidget = 'ihelper_status'
    ToolbarWidget = 'ihelper_toolbar'
