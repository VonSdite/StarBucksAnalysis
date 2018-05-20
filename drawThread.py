# -*- coding: utf-8 -*-
# __Author__: Sdite, amyy4, JX-Soleil, hzgege
# __Email__ : a122691411@gmail.com

from PyQt5.QtCore import QThread, pyqtSignal
import time

class DrawThread(QThread):
    endTrigger = pyqtSignal()

    def __init__(self, target, args):
        super(DrawThread, self).__init__()
        self.fun = target
        self.args = args

    def run(self):
        start = time.time()
        self.fun(*self.args)
        end = time.time()
        self.time = "用时: %fs" % (end-start)
        self.endTrigger.emit()
