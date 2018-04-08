# -*- coding: utf-8 -*-
# __Author__: Sdite
# __Email__ : a122691411@gmail.com

import os, sys, time
import pickle
import platform
import threading
import pandas as pd
from draw import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class UI(QMainWindow):
    """docstring for UI"""
    def __init__(self):
        super(UI, self).__init__()
        self.initUI()

    def initUI(self):
        # 将任务栏图标改成 image/StarBucks.png
        if platform.system() == 'Windows':
            import ctypes
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
                "image/StarBucks.png")

        self.resize(380, 350)  # 设置窗口初始大小
        self.center()           # 将窗口居中
        self.setWindowTitle('星巴克数据分析')
        self.setWindowIcon(QIcon('image/StarBucks.png'))

        self.menuBar()
        self.statusBar()

        self.setOpenFileMenu()

        self.setButton()

        self.show()

    def setButton(self):
        self.drawMapButton = QPushButton('世界分布图', self)

        self.drawColorMapButton = QPushButton('国家分布彩色图', self)

        self.countStoreByTimezoneButton_bar = QPushButton('时区店铺数量柱状图', self)
        self.countStoreByTimezoneButton_pie = QPushButton('时区店铺数量饼图', self)
        self.countStoreByCountryButton_bar = QPushButton('国家店铺数量柱状图', self)
        self.countStoreByCountryButton_pie = QPushButton('国家店铺数量饼图', self)

        self.drawMapButton.setEnabled(False)
        self.drawColorMapButton.setEnabled(False)
        self.countStoreByTimezoneButton_bar.setEnabled(False)
        self.countStoreByTimezoneButton_pie.setEnabled(False)
        self.countStoreByCountryButton_bar.setEnabled(False)
        self.countStoreByCountryButton_pie.setEnabled(False)

        self.drawMapButton.clicked.connect(self.drawMap)
        self.drawColorMapButton.clicked.connect(self.drawColorMap)
        self.countStoreByTimezoneButton_bar.clicked.connect(
            lambda : self.drawBar(self.csv_file['Timezone'],
                                  'html/timezoneBar.html', '时区店铺数量柱状图'))
        self.countStoreByTimezoneButton_pie.clicked.connect(
            lambda: self.drawPie(self.csv_file['Timezone'],
                                 'html/timezonePie.html', '时区店铺数量饼图'))
        self.countStoreByCountryButton_bar.clicked.connect(
            lambda: self.drawBar(self.csv_file['Country'],
                                 'html/countryBar.html', '国家店铺数量柱状图'))
        self.countStoreByCountryButton_pie.clicked.connect(
            lambda: self.drawPie(self.csv_file['Country'],
                                 'html/countryPie.html', '国家店铺数量饼图'))

        mainWidget = QWidget()
        boxLayout = QVBoxLayout()

        boxLayout.addWidget(self.drawMapButton)
        boxLayout.addWidget(self.drawColorMapButton)
        boxLayout.addWidget(self.countStoreByTimezoneButton_bar)
        boxLayout.addWidget(self.countStoreByTimezoneButton_pie)
        boxLayout.addWidget(self.countStoreByCountryButton_bar)
        boxLayout.addWidget(self.countStoreByCountryButton_pie)

        mainWidget.setLayout(boxLayout)

        self.setCentralWidget(mainWidget)

    def drawMap(self):
        threading.Thread(target=drawMap, args=(self.csv_file,
                                               'html/map.html',
                                               '世界分布图(不同时区不同颜色点)')).start()

    def drawColorMap(self):
        threading.Thread(target=drawColorMaps,
                         args=(self.csv_file['Country'],
                               'html/colorMap.html', '国家分布彩色图')).start()

    def drawBar(self, data, fileName='html/bar.html', title=''):
        threading.Thread(target=drawBar, args=(data, fileName, title)).start()

    def drawPie(self, data, fileName='html/pie.hmtl', title=''):
        threading.Thread(target=drawPie, args=(data, fileName, title)).start()


    # 设置打开文件的功能
    def setOpenFileMenu(self):
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('File')

        openFile = QAction(QIcon('image/open.png'), 'open file', self)
        openFile.setShortcut('Ctrl + O')
        openFile.setStatusTip('打开文件')
        openFile.triggered.connect(self.showFileDialog)

        fileMenu.addAction(openFile)

    # 显示文件对话框
    def showFileDialog(self):
        # 打开文件，只允许打开'csv'文件
        filePath = QFileDialog.getOpenFileName(self, caption='打开文件', directory='./',
                                               filter='*.csv')
        if filePath[0]:
            file = filePath[0]
            filename = os.path.split(file)[1].split('.')[0]

            savePickle = 'config/' + filename + '.pickle'
            threading.Thread(target=self.openFile, args=(file, savePickle)).start()
            self.setWindowTitle(file)

    # 检查上次打开的这个csv文件修改时间和这次打开的这个csv文件的时间是否一致
    def checkFile(self, file, savePickle):
        savePickleChange = savePickle + 'change'
        with open(savePickleChange, 'rb') as f:
            changeTime = pickle.load(f)
        nowChangeTime = time.localtime(os.stat(file).st_mtime)

        # 如果时间一致，表明两个文件相同， 不一致则需要重新打开
        if changeTime == nowChangeTime:
            return True
        else:
            return False

    def openFile(self, file, savePickle):
        if os.path.isfile(savePickle) and self.checkFile(file, savePickle):
            # 该文件曾被打开过， 有pickle缓存
            # 该文件没有被修改过
            with open(savePickle, 'rb') as f:
                self.csv_file = pickle.load(f)
        else:
            # 该文件没有被打开过
            # 一是打开它
            # 二是保存该文件的csv类型， 提高下次打开效率
            # 三是保存该文件的最后修改时间，用于下次打开时判断是否被修改过
            csv_file = pd.read_csv(file)
            self.csv_file = csv_file.fillna('Not set')  # 空值设置为Not set
            with open(savePickle, 'wb') as f:
                pickle.dump(self.csv_file, f)

            changeTime = time.localtime(os.stat(file).st_mtime)
            savePickleChange = savePickle + 'change'
            with open(savePickleChange, 'wb') as f:
                pickle.dump(changeTime, f)

        self.drawMapButton.setEnabled(True)
        self.drawColorMapButton.setEnabled(True)
        self.countStoreByTimezoneButton_bar.setEnabled(True)
        self.countStoreByTimezoneButton_pie.setEnabled(True)
        self.countStoreByCountryButton_bar.setEnabled(True)
        self.countStoreByCountryButton_pie.setEnabled(True)

    # 窗口居中
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = UI()

    sys.exit(app.exec_())