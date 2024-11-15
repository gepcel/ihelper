# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2021, gepcel
#
# Licensed under the terms of the MIT license
# ----------------------------------------------------------------------------
"""
ihelper: A spyder plugin to get help information from ipython console in editor.
"""

from qtpy.QtCore import Signal
from spyder.api.widgets.status import StatusBarWidget
from spyder.api.widgets.toolbars import ApplicationToolbar

from ihelper.spyder.api import IHelperWidgets


class IHelperStatusWidget(StatusBarWidget):
    """
    Widget to display the status of ihelper plugin

    Notes:
    ----
    * IHelperStatusWidget inherit from StatusBarWidget
    * It's label(status) is updated in ...
    * It's registered in ...
    """
    ID = IHelperWidgets.StatusWidget


class IHelperToolbarWidget(ApplicationToolbar):
    ID = IHelperWidgets.ToolbarWidget
    sig_toolbar_click = Signal()
