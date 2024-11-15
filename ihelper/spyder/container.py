# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2021, gepcel
#
# Licensed under the terms of the MIT license
# ----------------------------------------------------------------------------
"""
ihelper: A spyder plugin to get help information from ipython console in editor.
"""

# Third-party imports
from qtpy.QtCore import Signal

# Spyder imports
from spyder.api.config.decorators import on_conf_change
from spyder.api.plugin_registration.decorators import on_plugin_available
from spyder.api.plugins import Plugins
from spyder.api.translations import get_translation
from spyder.api.widgets.main_container import PluginMainContainer
from ihelper.spyder.api import IHelperActions, IHelperToolbarSections

# Local imports
from ihelper.spyder.widgets import IHelperStatusWidget, IHelperToolbarWidget


class IHelperWidgetsContainer(PluginMainContainer):

    # Signals
    sig_toolbar_click = Signal()
    """
    This is signal is emitted to inspect the current and request help from ipython console in editor.
    """

    # --- PluginMainContainer API
    # ------------------------------------------------------------------------
    def setup(self):
        # Status bar widgets
        self.status_widget = IHelperStatusWidget(self)
        self.status_widget.set_value('ihelper:ok')

        self.toolbar_widget = IHelperToolbarWidget(self, "IHelper toolbar")
        self.toolbar_widget.sig_toolbar_click.connect(self.sig_toolbar_click)

        self.toolbar_click_action = self.create_action(
            IHelperActions.ToolbarClickAction,
            text="Click to display help",
            tip="Click to display help",
            icon=self.create_icon("MessageBoxInformation"),
            triggered=self.button_click,
        )

        self.add_item_to_toolbar(
            self.toolbar_click_action,
            self.toolbar_widget,
            section=IHelperToolbarSections.First,
        )

    def update_actions(self):
        pass

    def button_click(self):
        self.sig_toolbar_click.emit()

    @on_plugin_available(plugin=Plugins.Editor)
    def on_editor_available(self):
        self.editor_ok = True
        if self.editor_ok and self.console_ok:
            self.status_widget.set_value('ihelper: √')

    @on_plugin_available(plugin=Plugins.Console)
    def on_console_available(self):
        self.console_ok = True
        if self.editor_ok and self.console_ok:
            self.status_widget.set_value('ihelper: √')
