# -*- coding: utf-8 -*-
# __Author__: Sdite
# __Email__ : a122691411@gmail.com

import pickle
import os, sys, time
import platform
import threading
import pandas as pd
from draw import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QIcon, QIntValidator
from PyQt5.QtCore import Qt, QUrl
from drawThread import DrawThread

class UI(QMainWindow):
    """docstring for UI"""

    def __init__(self):
        super(UI, self).__init__()
        self.initUI()

    def initUI(self):
        # 将任务栏图标改成 image/StarBucks.png
        if platform.system() == 'Windows':
            # windows任务栏要这样设置才能和图标一致
            import ctypes
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
                "image/StarBucks.png")

        self.setWindowTitle('星巴克数据分析')
        self.setWindowIcon(QIcon('image/StarBucks.png'))

        self.mainWidget = QWidget()          # 主窗体控件
        self.mainLayout = QGridLayout()      # 主窗体layout

        self.menuBar()              # 菜单栏
        self.statusBar()            # 状态栏
        self.setOpenFileMenu()      # 打开文件菜单

        self.setButton()            # 设置按钮
        self.setFindTopKWidget()
        self.setWebEngineView()

        self.mainWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.mainWidget)

        self.adjustSize()
        self.center()  # 将窗口居中
        self.show()

    def setWebEngineView(self):
        self.webEngine = QWebEngineView(self)
        self.mainLayout.addWidget(self.webEngine, 3, 1, 6, 6)


    # top-k的输入框，按钮的控件
    def setFindTopKWidget(self):
        longitudeLabel = QLabel()
        latitudeLabel = QLabel()
        rangeLabel = QLabel()
        kLabel = QLabel()

        longitudeLabel.setText("经度: ")
        latitudeLabel.setText("纬度: ")
        rangeLabel.setText("range:")
        kLabel.setText("k: ")

        self.longitudeEdit = QLineEdit()
        self.latitudeEdit = QLineEdit()
        self.rangeEdit = QLineEdit()
        self.kEdit = QLineEdit()

        self.findRangeButton = QPushButton()
        self.findRangeButton.setText("查找range")
        self.findRangeButton.setEnabled(False)
        self.findRangeButton.clicked.connect(self.fingRange)

        self.findTopKButton = QPushButton()
        self.findTopKButton.setText("查找top-k")
        self.findTopKButton.setEnabled(False)
        self.findTopKButton.clicked.connect(self.findSlot)

        hBox = QHBoxLayout(self)
        hBox.addWidget(longitudeLabel)
        hBox.addWidget(self.longitudeEdit, 0)
        hBox.addWidget(latitudeLabel)
        hBox.addWidget(self.latitudeEdit, 0)
        hBox.addWidget(rangeLabel)
        hBox.addWidget(self.rangeEdit,0)
        hBox.addWidget(kLabel)
        hBox.addWidget(self.kEdit, 0)
        hBox.addWidget(self.findRangeButton,0)
        hBox.addWidget(self.findTopKButton, 0)

        self.longitudeEdit.setEnabled(False)
        self.latitudeEdit.setEnabled(False)
        self.rangeEdit.setEnabled(False)
        self.kEdit.setEnabled(False)

        hWidget = QWidget()
        hWidget.setLayout(hBox)
        self.mainLayout.addWidget(hWidget, 1, 1, 1, 6)

    def checkLongAndLat(self):
        self.longitude = self.longitudeEdit.text()
        self.latitude = self.latitudeEdit.text()
        if self.longitude == "":
            QMessageBox.warning(self, "警告", "请输入经度", QMessageBox.Ok)
            return False

        try:
            self.longitude = float(self.longitude)
            if self.longitude > 180 or self.longitude < -180:
                QMessageBox.warning(self, "错误", "经度在-180~180之间", QMessageBox.Ok)
                return False
        except:
            QMessageBox.warning(self, "错误", "请输入数字", QMessageBox.Ok)
            return False

        if self.latitude == "":
            QMessageBox.warning(self, "警告", "请输入纬度", QMessageBox.Ok)
            return False

        try:
            self.latitude = float(self.latitude)
            if self.latitude > 90 or self.latitude < -90:
                QMessageBox.warning(self, "错误", "纬度在-90~90之间", QMessageBox.Ok)
                return False
        except:
            QMessageBox.warning(self, "错误", "请输入数字", QMessageBox.Ok)
            return False
        return True

    def fingRange(self):

        if not self.checkLongAndLat():
            return

        r = self.rangeEdit.text()

        if r == "":
            QMessageBox.warning(self, "警告", "请输入range值", QMessageBox.Ok)
            return

        r = int(r)

        self.t = DrawThread(target=drawRangeMap,
                            args=(self.csv_file,
                                  self.longitude,
                                  self.latitude,
                                  r,
                                  'html/RangeMap.html', 'topK点图'))
        self.t.endTrigger.connect(lambda: self.showInWebEngineView('/html/RangeMap.html'))
        self.t.start()


    def findSlot(self):
        if not self.checkLongAndLat():
            return

        k = self.kEdit.text()

        if k == "":
            QMessageBox.warning(self, "警告", "请输入k值", QMessageBox.Ok)
            return

        k = int(k)

        self.t = DrawThread(target=drawTopKMap,
                            args=(self.csv_file,
                                  self.longitude,
                                  self.latitude,
                                  k,
                                  'html/topKMap.html', 'topK点图'))
        self.t.endTrigger.connect(lambda: self.showInWebEngineView('/html/topKMap.html'))
        self.t.start()

    # 设置基本按钮， 后续可能要重写
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
            lambda: self.drawBar(self.csv_file['Timezone'],
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

        self.mainLayout.addWidget(self.drawMapButton, 2, 1)
        self.mainLayout.addWidget(self.drawColorMapButton, 2, 2)
        self.mainLayout.addWidget(self.countStoreByTimezoneButton_bar, 2, 3)
        self.mainLayout.addWidget(self.countStoreByTimezoneButton_pie, 2, 4)
        self.mainLayout.addWidget(self.countStoreByCountryButton_bar, 2, 5)
        self.mainLayout.addWidget(self.countStoreByCountryButton_pie, 2, 6)


    # 加载html
    def showInWebEngineView(self, fileName):
        self.statusBar().showMessage(self.t.time)
        self.webEngine.load(QUrl.fromLocalFile(fileName))


    # 画时区店铺数量渐变彩色点
    def drawMap(self):
        self.t = DrawThread(drawMap, (self.csv_file, 'html/map.html', '不同时区店铺数量渐变图'))
        self.t.endTrigger.connect(lambda :self.showInWebEngineView('/html/map.html'))
        self.t.start()

    # 画国家分布彩色渐变图
    def drawColorMap(self):
        self.t = DrawThread(target=drawColorMaps,
                         args=(self.csv_file['Country'],
                               'html/colorMap.html', '国家分布彩色图'))
        self.t.endTrigger.connect(lambda: self.showInWebEngineView('/html/colorMap.html'))
        self.t.start()

    # 画柱状图
    def drawBar(self, data, fileName='html/bar.html', title=''):
        self.t = DrawThread(target=drawBar, args=(data, fileName, title))
        self.t.endTrigger.connect(lambda: self.showInWebEngineView('/'+fileName))
        self.t.start()

    # 画饼图
    def drawPie(self, data, fileName='html/pie.hmtl', title=''):
        self.t = DrawThread(target=drawPie, args=(data, fileName, title))
        self.t.endTrigger.connect(lambda: self.showInWebEngineView('/' + fileName))
        self.t.start()

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
            self.csv_file = pd.read_csv(file)
            with open(savePickle, 'wb') as f:
                pickle.dump(self.csv_file, f)

            changeTime = time.localtime(os.stat(file).st_mtime)
            savePickleChange = savePickle + 'change'
            with open(savePickleChange, 'wb') as f:
                pickle.dump(changeTime, f)

        self.csv_file.fillna(0)
        self.drawMapButton.setEnabled(True)
        self.drawColorMapButton.setEnabled(True)
        self.countStoreByTimezoneButton_bar.setEnabled(True)
        self.countStoreByTimezoneButton_pie.setEnabled(True)
        self.countStoreByCountryButton_bar.setEnabled(True)
        self.countStoreByCountryButton_pie.setEnabled(True)
        self.findTopKButton.setEnabled(True)

        self.longitudeEdit.setEnabled(True)
        self.latitudeEdit.setEnabled(True)
        self.kEdit.setEnabled(True)
        #
        # self.RlongitudeEdit.setEnabled(True)
        # self.RlatitudeEdit.setEnabled(True)
        self.rangeEdit.setEnabled(True)

        kIntValidator = QIntValidator(self)
        kIntValidator.setRange(0, len(self.csv_file))
        self.kEdit.setPlaceholderText("输入0-"+str(len(self.csv_file))+"间的整数值")
        self.kEdit.setValidator(kIntValidator)

    # 窗口居中
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
