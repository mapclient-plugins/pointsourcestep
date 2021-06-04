# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(418, 228)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.configGroupBox = QGroupBox(Dialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.formLayout = QFormLayout(self.configGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.idLabel = QLabel(self.configGroupBox)
        self.idLabel.setObjectName(u"idLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.idLabel)

        self.idLineEdit = QLineEdit(self.configGroupBox)
        self.idLineEdit.setObjectName(u"idLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.idLineEdit)

        self.fileLocLabel = QLabel(self.configGroupBox)
        self.fileLocLabel.setObjectName(u"fileLocLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.fileLocLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fileLocLineEdit = QLineEdit(self.configGroupBox)
        self.fileLocLineEdit.setObjectName(u"fileLocLineEdit")

        self.horizontalLayout.addWidget(self.fileLocLineEdit)

        self.fileLocButton = QPushButton(self.configGroupBox)
        self.fileLocButton.setObjectName(u"fileLocButton")

        self.horizontalLayout.addWidget(self.fileLocButton)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout)

        self.colLabel = QLabel(self.configGroupBox)
        self.colLabel.setObjectName(u"colLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.colLabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.colXLabel = QLabel(self.configGroupBox)
        self.colXLabel.setObjectName(u"colXLabel")

        self.horizontalLayout_2.addWidget(self.colXLabel)

        self.colXSpinBox = QSpinBox(self.configGroupBox)
        self.colXSpinBox.setObjectName(u"colXSpinBox")

        self.horizontalLayout_2.addWidget(self.colXSpinBox)

        self.colYLabel = QLabel(self.configGroupBox)
        self.colYLabel.setObjectName(u"colYLabel")

        self.horizontalLayout_2.addWidget(self.colYLabel)

        self.colYSpinBox = QSpinBox(self.configGroupBox)
        self.colYSpinBox.setObjectName(u"colYSpinBox")
        self.colYSpinBox.setValue(1)

        self.horizontalLayout_2.addWidget(self.colYSpinBox)

        self.colZLabel = QLabel(self.configGroupBox)
        self.colZLabel.setObjectName(u"colZLabel")

        self.horizontalLayout_2.addWidget(self.colZLabel)

        self.colZSpinBox = QSpinBox(self.configGroupBox)
        self.colZSpinBox.setObjectName(u"colZSpinBox")
        self.colZSpinBox.setValue(2)

        self.horizontalLayout_2.addWidget(self.colZSpinBox)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_2)


        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        QWidget.setTabOrder(self.idLineEdit, self.fileLocLineEdit)
        QWidget.setTabOrder(self.fileLocLineEdit, self.fileLocButton)
        QWidget.setTabOrder(self.fileLocButton, self.colXSpinBox)
        QWidget.setTabOrder(self.colXSpinBox, self.colYSpinBox)
        QWidget.setTabOrder(self.colYSpinBox, self.colZSpinBox)
        QWidget.setTabOrder(self.colZSpinBox, self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Configure Point Source Step", None))
        self.configGroupBox.setTitle("")
        self.idLabel.setText(QCoreApplication.translate("Dialog", u"Identifier:  ", None))
        self.fileLocLabel.setText(QCoreApplication.translate("Dialog", u"Filename:  ", None))
        self.fileLocButton.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.colLabel.setText(QCoreApplication.translate("Dialog", u"Columns:", None))
        self.colXLabel.setText(QCoreApplication.translate("Dialog", u"X", None))
        self.colYLabel.setText(QCoreApplication.translate("Dialog", u"Y", None))
        self.colZLabel.setText(QCoreApplication.translate("Dialog", u"Z", None))
    # retranslateUi

