# ihelper

ihelper: A spyder plugin to get help information from ipython console in editor.

Now it works in spyder 6.02.

## What does this plugin do?

This plugin gives another option to get documents. There are two `inspect the current object` options in spyder. One from the editor, and another from the console. Both have their own advantage, and both work their own way for a reason.

People always can't get documents of some methods in the editor, but can from the console. So for me I always copy the line into the console, get the document, and continue work in the editor. With this plugin, people can get all two kinds of documents from the editor.

## How to use?

There are 3 ways to use the plugin.

1. Toolbar button. With the cursor at the method in the editor, click the `Ihelper toolbar` button, and you'll get the doc. The button doesn't appear by default, you need to check manually.

<img src="https://github.com/user-attachments/assets/0f12b533-d58a-47c6-aa4c-bc94a7ee5ff2" width=550px>

2. Statusbar click. With the cursor at the method in the editor, click the `ihelper:ok` in the status bar, and you'll get the doc.

![image](https://github.com/user-attachments/assets/5ea6b363-422a-427f-b973-d0cf4230f665)

3. Pressing a shortcut key. This plugin registers a function into `Keyboard shortcuts` in preference of spyder, called `request help from console`, without a shortcut. You need to assign one manually, `Alt + I` for example. The with cursor at the method in the editor, pressing `Alt + I`, you'll get the doc.

![image](https://github.com/user-attachments/assets/02639247-fc1a-4b72-9698-a0c6e75c351e)

## How to install?

Download the code, navigate to the directory, then `pip install .`
