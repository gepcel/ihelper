# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2021, gepcel
#
# Licensed under the terms of the MIT license
# ----------------------------------------------------------------------------
"""
ihelper: A spyder plugin to get help information from ipython console in editor.
"""
import re
from qtpy.QtCore import Qt
from qtpy.QtGui import QTextCursor

# Local imports
from spyder.api.plugins import Plugins, SpyderPluginV2
from spyder.api.plugin_registration.decorators import on_plugin_available
# from spyder.api.translations import get_translation
from spyder.plugins.mainmenu.api import ApplicationMenus
from spyder.py3compat import to_text_string

from ihelper.spyder.container import IHelperWidgetsContainer
from ihelper.spyder.api import IHelperActions, IHelperToolbarSections


class IHelper(SpyderPluginV2):
    NAME = "ihelper"
    # WIDGET_CLASS = IHelperWidgets
    CONF_SECTION = NAME
    # CONF_WIDGET_CLASS = PylintConfigPage
    REQUIRES = [Plugins.StatusBar, Plugins.Editor, Plugins.MainMenu, Plugins.Toolbar]
    CONTAINER_CLASS = IHelperWidgetsContainer
    # CONF_FILE = False
    DISABLE_ACTIONS_WHEN_HIDDEN = False

    @staticmethod
    def get_name():
        return "ihelper"

    def get_description(self):
        return "A spyder plugin to get help information from ipython console in editor."

    def on_initialize(self):
        container = self.get_container()
        # container.sig_request_ihelp.connect(self.inspect_current_object_via_console)
        container.sig_toolbar_click.connect(
            lambda: self.inspect_current_object_via_console(debug=True))
        ihelper_action = self.create_action(
            IHelperActions.ShortcutAction,
            text="Request help from console",
            tip="Request help from console",
            triggered=self.inspect_current_object_via_console,
            register_shortcut=True,
            context=Qt.WindowShortcut
        )
        ihelper_action.setEnabled(True)

    @on_plugin_available(plugin=Plugins.MainMenu)
    def on_main_menu_available(self):
        mainmenu = self.get_plugin(Plugins.MainMenu)
        ihelper_action = self.get_action(IHelperActions.ShortcutAction)
        mainmenu.add_item_to_application_menu(
            ihelper_action, menu_id=ApplicationMenus.Source)

    @on_plugin_available(plugin=Plugins.StatusBar)
    def on_statusbar_available(self):
        container = self.get_container()
        statusbar = self.get_plugin(Plugins.StatusBar)
        statusbar.add_status_widget(container.status_widget)

    @on_plugin_available(plugin=Plugins.Toolbar)
    def on_toolbvar_available(self):
        container = self.get_container()
        toolbar = self.get_plugin(Plugins.Toolbar)
        toolbar.add_application_toolbar(container.toolbar_widget)

    def inspect_current_object_via_console(self, debug=False):
        self.editor = self.get_plugin(Plugins.Editor).get_current_editor()
        cursor = self.editor.textCursor()
        # text, pos = self.get_current_word2(cursor, console=True)
        # help = self.main.get_plugin(Plugins.Help)
        # help.set_object_text({'name': text, 'ignore_unknown': False})
        try:
            text, pos = self.get_current_word2(cursor, console=True)
            help = self.main.get_plugin(Plugins.Help)
            help.set_object_text({'name': text, 'ignore_unknown': False})
        except BaseException as e:
            if debug:
                raise e
            else:
                pass

    def get_current_word2(self, cursor, completion=False, help_req=False,
                          valid_python_variable=True,
                          console=False):
        """
        Return current word, i.e. word at cursor position, and the start
        position.
        """
        # cursor = self.editor.textCursor()
        cursor_pos = cursor.position()

        if cursor.hasSelection():
            # Removes the selection and moves the cursor to the left side
            # of the selection: this is required to be able to properly
            # select the whole word under cursor (otherwise, the same word is
            # not selected when the cursor is at the right side of it):
            cursor.setPosition(min([cursor.selectionStart(),
                                    cursor.selectionEnd()]))
        else:
            # Checks if the first character to the right is a white space
            # and if not, moves the cursor one word to the left (otherwise,
            # if the character to the left do not match the "word regexp"
            # (see below), the word to the left of the cursor won't be
            # selected), but only if the first character to the left is not a
            # white space too.
            def is_space(move):
                curs = self.editor.textCursor()
                curs.movePosition(move, QTextCursor.KeepAnchor)
                return not to_text_string(curs.selectedText()).strip()

            def is_special_character(move):
                """Check if a character is a non-letter including numbers."""
                curs = self.editor.textCursor()
                curs.movePosition(move, QTextCursor.KeepAnchor)
                text_cursor = to_text_string(curs.selectedText()).strip()
                if console:
                    return len(re.findall(r'([a-zA-Z_]+[0-9a-zA-Z_\.]*)', text_cursor, re.UNICODE)) == 0
                return len(
                    re.findall(r'([^\d\W]\w*)', text_cursor, re.UNICODE)) == 0

            if help_req:
                if is_special_character(QTextCursor.PreviousCharacter):
                    cursor.movePosition(QTextCursor.NextCharacter)
                elif is_special_character(QTextCursor.NextCharacter):
                    cursor.movePosition(QTextCursor.PreviousCharacter)
            elif not completion:
                if is_space(QTextCursor.NextCharacter):
                    if is_space(QTextCursor.PreviousCharacter):
                        return
                    cursor.movePosition(QTextCursor.WordLeft)
            else:
                if is_space(QTextCursor.PreviousCharacter):
                    return
                if (is_special_character(QTextCursor.NextCharacter)):
                    cursor.movePosition(QTextCursor.WordLeft)

        cursor.select(QTextCursor.WordUnderCursor)
        text = to_text_string(cursor.selectedText())
        startpos = cursor.selectionStart()

        # Find a valid Python variable name
        if console:
            cursor.select(QTextCursor.BlockUnderCursor)
            block = to_text_string(cursor.selectedText())
            _pos_start = block.find(text)
            _delta = block.rfind(' ', 0, _pos_start)
            text = block[_delta + 1:]
            match = re.findall(r'([a-zA-Z_]+[0-9a-zA-Z_\.]*)', text, re.UNICODE)
            if not match:
                return None
            else:
                text = match[0]
        elif valid_python_variable:
            match = re.findall(r'([^\d\W]\w*)', text, re.UNICODE)
            if not match:
                # This is assumed in several places of our codebase,
                # so please don't change this return!
                return None
            else:
                text = match[0]
        if completion:
            text = text[:cursor_pos - startpos]

        return text, startpos
