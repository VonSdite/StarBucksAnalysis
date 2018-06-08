# -*- coding: utf-8 -*-
# __Author__: Sdite
# __Email__ : a122691411@gmail.com

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

class TInteractObj(QObject):
    sigReceivedMessFromJS = pyqtSignal(str)
    # SigSendMessageToJS = pyqtSignal(str)
    def __init__(self, parent = None):
        super().__init__(parent)

    @pyqtSlot(str)
    def JSSendMessage(self, strParameter):
        print('JSSendMessage(%s) from Html' %strParameter)
        self.sigReceivedMessFromJS.emit(strParameter)

