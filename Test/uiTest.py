# -*- coding: utf-8 -*-
# __Author__: Sdite
# __Email__ : a122691411@gmail.com

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class UI(QMainWindow):
    """docstring for UI"""

    def __init__(self):
        super(UI, self).__init__()
        self.initUI()

    def initUI(self):
        moreButton = QPushButton(">>")
        moreButton.setCheckable(True)
        moreButton.setAutoDefault(False)

        extension = QWidget()

        wholeWordsCheckBox = QCheckBox("&Whole words")
        backwardCheckBox = QCheckBox("Search &backward")
        searchSelectionCheckBox = QCheckBox("Search se&lection")

        buttonBox = QDialogButtonBox(Qt.Vertical)
        buttonBox.addButton(moreButton, QDialogButtonBox.ActionRole)

        moreButton.toggled.connect(extension.setVisible)

        extensionLayout = QVBoxLayout()
        extensionLayout.setContentsMargins(0, 0, 0, 0)
        extensionLayout.addWidget(wholeWordsCheckBox)
        extensionLayout.addWidget(backwardCheckBox)
        extensionLayout.addWidget(searchSelectionCheckBox)
        extension.setLayout(extensionLayout)

        mainWidgets = QWidget()
        mainLayout = QGridLayout()

        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addWidget(buttonBox, 0, 1)
        mainLayout.addWidget(extension, 1, 0, 1, 2)
        mainLayout.setRowStretch(2, 1)

        extension.hide()

        mainWidgets.setLayout(mainLayout)
        self.setCentralWidget(mainWidgets)
        self.layout().setSizeConstraint(QLayout.SetFixedSize)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ui = UI()
    ui.show()
    sys.exit(app.exec_())