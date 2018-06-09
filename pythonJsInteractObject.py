# -*- coding: utf-8 -*-
# __Author__: Sdite
# __Email__ : a122691411@gmail.com

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

# 用于python接收JS的消息
class PythonJsInteractObject(QObject):
    sigReceivedMessFromJS = pyqtSignal(str)
    def __init__(self, parent = None):
        super().__init__(parent)

    @pyqtSlot(str)
    def JSSendMessage(self, strParameter):
        self.sigReceivedMessFromJS.emit(strParameter)

