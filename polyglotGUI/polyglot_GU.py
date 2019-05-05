# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\polyglot_icons_and_renaming_objects.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from polyglotGUI import polyglot
import bitsv
import polyglot
import webbrowser
import os

my_path = os.path.abspath(os.path.dirname(__file__))

# ICONS
SUCCESS_ICON = os.path.join(my_path, "./icons/png/001-success.png")
ERROR_ICON = os.path.join(my_path, "./icons/png/002-error.png")
GLOTTIS_ICON = os.path.join(my_path, "./icons/png/mouth.png")

SUPPORTED_EXTENSIONS = [
    # text
    'html',

    # images
    'png',
    'jpg'
]

BROWSER_URL_ENDPOINTS = {
    'BICODOTMEDIA': 'https://bico.media/'
}


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 360)
        MainWindow.setMinimumSize(QtCore.QSize(640, 360))
        MainWindow.setMaximumSize(QtCore.QSize(640, 360))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(GLOTTIS_ICON), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 641, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.top_level_verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.top_level_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_level_verticalLayout.setObjectName("top_level_verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.B_tab = QtWidgets.QWidget()
        self.B_tab.setObjectName("B_tab")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.B_tab)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 611, 281))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.inside_B_tab_verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.inside_B_tab_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.inside_B_tab_verticalLayout.setObjectName("inside_B_tab_verticalLayout")
        self.B_tab_gridLayout = QtWidgets.QGridLayout()
        self.B_tab_gridLayout.setObjectName("B_tab_gridLayout")
        self.browse_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.browse_pushButton.setObjectName("browse_pushButton")
        self.browse_pushButton.clicked.connect(self.getOpenFileNames)  # Event --> getOpenFileNames()
        self.B_tab_gridLayout.addWidget(self.browse_pushButton, 1, 2, 1, 1)
        self.activate_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.activate_pushButton.setObjectName("activate_pushButton")
        self.activate_pushButton.clicked.connect(self.check_private_key)  # Event --> check_private_key()
        self.B_tab_gridLayout.addWidget(self.activate_pushButton, 0, 2, 1, 1)
        self.browse_icon_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.browse_icon_label.setMaximumSize(QtCore.QSize(30, 30))
        self.browse_icon_label.setText("")
        self.browse_icon_label.setPixmap(QtGui.QPixmap(ERROR_ICON))
        self.browse_icon_label.setScaledContents(True)
        self.browse_icon_label.setObjectName("browse_icon_label")
        self.B_tab_gridLayout.addWidget(self.browse_icon_label, 1, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.B_tab_gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        self.private_key_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.private_key_lineEdit.setObjectName("private_key_lineEdit")
        self.B_tab_gridLayout.addWidget(self.private_key_lineEdit, 0, 1, 1, 1)
        self.file_name_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.file_name_lineEdit.setObjectName("file_name_lineEdit")
        self.B_tab_gridLayout.addWidget(self.file_name_lineEdit, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.view_content_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.view_content_pushButton.setObjectName("view_content_pushButton")
        self.view_content_pushButton.clicked.connect(self.view_content)  # Event --> view_content()
        self.horizontalLayout.addWidget(self.view_content_pushButton)
        self.preview_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.preview_pushButton.setObjectName("preview_pushButton")
        self.horizontalLayout.addWidget(self.preview_pushButton)
        self.B_tab_gridLayout.addLayout(self.horizontalLayout, 4, 1, 1, 1)
        self.broadcast_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.broadcast_pushButton.setObjectName("broadcast_pushButton")
        self.broadcast_pushButton.clicked.connect(self.broadcast)  # Event --> broadcast()
        self.B_tab_gridLayout.addWidget(self.broadcast_pushButton, 4, 2, 1, 1)
        self.private_key_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.private_key_label.setObjectName("private_key_label")
        self.B_tab_gridLayout.addWidget(self.private_key_label, 0, 0, 1, 1)
        self.file_name_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.file_name_label.setObjectName("file_name_label")
        self.B_tab_gridLayout.addWidget(self.file_name_label, 1, 0, 1, 1)

        self.activate_icon_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.activate_icon_label.setMaximumSize(QtCore.QSize(30, 30))
        self.activate_icon_label.setText("")
        self.activate_icon_label.setPixmap(QtGui.QPixmap(ERROR_ICON))  # starts out as red
        self.activate_icon_label.setScaledContents(True)
        self.activate_icon_label.setObjectName("activate_icon_label")
        self.B_tab_gridLayout.addWidget(self.activate_icon_label, 0, 3, 1, 1)

        self.outputs_plainTextEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_4)
        self.outputs_plainTextEdit.setObjectName("outputs_plainTextEdit")
        self.B_tab_gridLayout.addWidget(self.outputs_plainTextEdit, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.B_tab_gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.inside_B_tab_verticalLayout.addLayout(self.B_tab_gridLayout)

        # BCAT TAB #
        self.tabWidget.addTab(self.B_tab, "")
        self.BCAT_tab = QtWidgets.QWidget()
        self.BCAT_tab.setObjectName("BCAT_tab")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.BCAT_tab)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 10, 611, 281))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")

        self.inside_BCAT_tab_verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.inside_BCAT_tab_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.inside_BCAT_tab_verticalLayout.setObjectName("inside_BCAT_tab_verticalLayout")
        self.BCAT_tab_gridLayout = QtWidgets.QGridLayout()
        self.BCAT_tab_gridLayout.setObjectName("BCAT_tab_gridLayout")
        self.browse_pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.browse_pushButton_2.setObjectName("browse_pushButton_2")
        self.browse_pushButton_2.clicked.connect(self.getOpenFileNames_2)  # Event --> getOpenFileNames_2()
        self.BCAT_tab_gridLayout.addWidget(self.browse_pushButton_2, 1, 2, 1, 1)
        self.activate_pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.activate_pushButton_2.setObjectName("activate_pushButton_2")
        self.activate_pushButton_2.clicked.connect(self.check_private_key_2)  # Event --> check_private_key_2()

        self.BCAT_tab_gridLayout.addWidget(self.activate_pushButton_2, 0, 2, 1, 1)
        self.browse_icon_label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.browse_icon_label_2.setMaximumSize(QtCore.QSize(30, 30))
        self.browse_icon_label_2.setText("")
        self.browse_icon_label_2.setPixmap(QtGui.QPixmap(ERROR_ICON))
        self.browse_icon_label_2.setScaledContents(True)
        self.browse_icon_label_2.setObjectName("browse_icon_label_2")
        self.BCAT_tab_gridLayout.addWidget(self.browse_icon_label_2, 1, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.BCAT_tab_gridLayout.addItem(spacerItem2, 3, 1, 1, 1)
        self.private_key_lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.private_key_lineEdit_2.setObjectName("private_key_lineEdit_2")
        self.BCAT_tab_gridLayout.addWidget(self.private_key_lineEdit_2, 0, 1, 1, 1)
        self.file_name_lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.file_name_lineEdit_2.setObjectName("file_name_lineEdit_2")
        self.BCAT_tab_gridLayout.addWidget(self.file_name_lineEdit_2, 1, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.view_content_pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.view_content_pushButton_2.setObjectName("view_content_pushButton_2")
        self.view_content_pushButton_2.clicked.connect(self.view_content_2)  # Event --> view_content_2()
        self.horizontalLayout_2.addWidget(self.view_content_pushButton_2)
        self.preview_pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.preview_pushButton_2.setObjectName("preview_pushButton_2")
        self.horizontalLayout_2.addWidget(self.preview_pushButton_2)
        self.BCAT_tab_gridLayout.addLayout(self.horizontalLayout_2, 4, 1, 1, 1)
        self.broadcast_pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.broadcast_pushButton_2.setObjectName("broadcast_pushButton_2")
        self.broadcast_pushButton_2.clicked.connect(self.broadcast_2)  # Event --> broadcast_2()

        self.BCAT_tab_gridLayout.addWidget(self.broadcast_pushButton_2, 4, 2, 1, 1)
        self.private_key_label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.private_key_label_2.setObjectName("private_key_label_2")
        self.BCAT_tab_gridLayout.addWidget(self.private_key_label_2, 0, 0, 1, 1)
        self.file_name_label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.file_name_label_2.setObjectName("file_name_label_2")
        self.BCAT_tab_gridLayout.addWidget(self.file_name_label_2, 1, 0, 1, 1)
        self.activate_icon_label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.activate_icon_label_2.setMaximumSize(QtCore.QSize(30, 30))
        self.activate_icon_label_2.setText("")
        self.activate_icon_label_2.setPixmap(QtGui.QPixmap(ERROR_ICON))
        self.activate_icon_label_2.setScaledContents(True)
        self.activate_icon_label_2.setObjectName("activate_icon_label_2")
        self.BCAT_tab_gridLayout.addWidget(self.activate_icon_label_2, 0, 3, 1, 1)
        self.outputs_plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_5)
        self.outputs_plainTextEdit_2.setObjectName("outputs_plainTextEdit_2")
        self.BCAT_tab_gridLayout.addWidget(self.outputs_plainTextEdit_2, 2, 1, 1, 1)
        self.outputs_label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.outputs_label_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.outputs_label_2.setObjectName("outputs_label_2")
        self.BCAT_tab_gridLayout.addWidget(self.outputs_label_2, 2, 0, 1, 1)
        self.inside_BCAT_tab_verticalLayout.addLayout(self.BCAT_tab_gridLayout)

        self.tabWidget.addTab(self.BCAT_tab, "")
        self.AIP_tab_3 = QtWidgets.QWidget()
        self.AIP_tab_3.setObjectName("AIP_tab_3")
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.AIP_tab_3)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(0, 0, 693, 291))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setMaximumSize(QtCore.QSize(640, 240))
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_15.setWordWrap(True)
        self.label_15.setIndent(0)
        self.label_15.setOpenExternalLinks(True)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_8.addWidget(self.label_15)
        self.tabWidget.addTab(self.AIP_tab_3, "")
        self.top_level_verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionCredits = QtWidgets.QAction(MainWindow)
        self.actionCredits.setObjectName("actionCredits")
        self.menuFile.addAction(self.actionSettings)
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuHelp.addAction(self.actionCredits)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Polyglot"))
        self.browse_pushButton.setText(_translate("MainWindow", "Browse"))
        self.activate_pushButton.setText(_translate("MainWindow", "Activate"))
        self.view_content_pushButton.setText(_translate("MainWindow", "View Content"))
        self.preview_pushButton.setText(_translate("MainWindow", "Preview tx"))
        self.broadcast_pushButton.setText(_translate("MainWindow", "Broadcast"))
        self.private_key_label.setText(_translate("MainWindow", " Private Key:\n"
                                                                "(WIF format)"))
        self.file_name_label.setText(_translate("MainWindow", " File name:"))
        self.outputs_plainTextEdit.setPlainText(
            _translate("MainWindow",
                       "Welcome to Polyglot!\n"
                       "- Bitcoin protocols made easy!\n"
                       "\n"
                       "To get started, enter your PrivateKey (WIF format) above.\n"
                       "- One easy way to do this is with the ElectrumSV wallet.\n"
                       "   1) Open up the \'addresses\' tab\n"
                       "       (you may have to first go to \'View\' --> \'show addresses\'\n"
                       "   2) Right click an address with Bitcoins in it and click on \'Private key\'\n"
                       "   3) Copy and paste\n"
                       "\n"
                       "B:// protocol is for files <100kb."))
        self.label.setText(_translate("MainWindow", " Outputs:"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.B_tab), _translate("MainWindow", "B://"))
        self.browse_pushButton_2.setText(_translate("MainWindow", "Browse"))
        self.activate_pushButton_2.setText(_translate("MainWindow", "Activate"))
        self.view_content_pushButton_2.setText(_translate("MainWindow", "View Content"))
        self.preview_pushButton_2.setText(_translate("MainWindow", "Preview tx"))
        self.broadcast_pushButton_2.setText(_translate("MainWindow", "Broadcast"))
        self.private_key_label_2.setText(_translate("MainWindow", " Private Key:\n"
                                                                  "(WIF format)"))
        self.file_name_label_2.setText(_translate("MainWindow", " File name:"))
        self.outputs_plainTextEdit_2.setPlainText(
            _translate("MainWindow",
                       "BCAT:// protocol is for large files up to 310mb uncompressed (110GB with nested gzip).\n"
                       "\n"
                       "See spec at: https://bcat.bico.media/"))
        self.outputs_label_2.setText(_translate("MainWindow", " Outputs:"))

        # MARK
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.BCAT_tab), _translate("MainWindow", "BCAT://"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Coming soon...</span></p><p align=\"center\"><a href=\"https://github.com/BitcoinFiles/AUTHOR_IDENTITY_PROTOCOL\"><span style=\" font-size:18pt; text-decoration: underline; color:#0000ff;\">https://github.com/BitcoinFiles/AUTHOR_IDENTITY_PROTOCOL</span></a></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AIP_tab_3), _translate("MainWindow", "AIP"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation"))
        self.actionCredits.setText(_translate("MainWindow", "Credits"))

        # DEFAULT SETTINGS AT STARTUP
        self.DEFAULT_VIEWER_URL = BROWSER_URL_ENDPOINTS['BICODOTMEDIA']
        self.LATEST_TXID = ''
        self.LATEST_TXID_2 = ''  # tab2 so user can switch between tabs and view each previously uploaded file easily

    def getOpenFileNames(self):
        """Dialogue box for browsing and selecting files"""
        # FIXME - can easily add "getExistingDirectory()" function for batch processing of multiple files later
        # Note to self - to get this working...
        # Needed to provide "MainWindow" as the parent QWidget for the getOpenFileNames() function
        # Rather than "self" which == ui_MainWindow object

        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.upload_file_path = str(QtWidgets.QFileDialog.getOpenFileName(MainWindow,
                                                                          "select file to upload", options=options))
        # If cancels out of selecting a file
        if self.upload_file_path != "('', '')":
            print(self.upload_file_path)
            # String formatting to pull out a clean path from QFileDialogue
            file_path = self.upload_file_path.split(os.sep)[0]
            file_path = file_path.split(",")[0].strip().strip('()')
            self.file_name_lineEdit.setText(file_path.strip(r"'"))

            # Log recognition of file extension and give "Success" signal to Browse icon
            # FIXME - also need to check if total transaction size is going to be > 100 kB
            #  will need to then warn them that this will therefore end up being sent with BCAT://
            #  also should have a dialogue box pop-up:
            #  on "broadcast.clicked()" --> xyz fee, file size + BCAT protocol + "are you sure? [Cancel, Broadcast]"
            file_extension = file_path.split(r".")[1].strip(r"'")
            if self.ext_is_supported(file_extension):
                self.log_to_plainTextEdit("Success! File extension recognised as: " + file_extension)
                self.browse_icon_success()
            elif self.ext_is_supported(file_extension) is False:
                self.log_to_plainTextEdit("Error! File extension, '{}' not officially recognised currently."
                                          "Would you like to try anyway? ".format(file_extension))
                self.browse_icon_error()
        else:
            # Cancelled out of selecting a file
            pass

    # FIXME It's quicker for me right now to just duplicate code for the coingeek hackathon -
    #  fix requires big refactor!!!
    def getOpenFileNames_2(self):
        """Dialogue box for browsing and selecting files"""

        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog

        # The broadcast function pulls the path to file from the LineEdit so it's fine for tabs to share
        # the self.upload_file_path variable and overwrite it
        self.upload_file_path = str(QtWidgets.QFileDialog.getOpenFileName(MainWindow,
                                                                          "select file to upload", options=options))
        # If cancels out of selecting a file
        if self.upload_file_path != "('', '')":
            print(self.upload_file_path)
            # String formatting to pull out a clean path from QFileDialogue
            file_path = self.upload_file_path.split(os.sep)[0]
            file_path = file_path.split(",")[0].strip().strip('()')
            self.file_name_lineEdit_2.setText(file_path.strip(r"'"))

            # Log recognition of file extension and give "Success" signal to Browse icon
            # FIXME - also need to check if total transaction size is going to be > 100 kB
            #  will need to then warn them that this will therefore end up being sent with BCAT://
            #  also should have a dialogue box pop-up:
            #  on "broadcast.clicked()" --> xyz fee, file size + BCAT protocol + "are you sure? [Cancel, Broadcast]"
            file_extension = file_path.split(r".")[1].strip(r"'")
            if self.ext_is_supported(file_extension):
                self.log_to_plainTextEdit_2("Success! File extension recognised as: " + file_extension)
                self.browse_icon_success_2()
            elif self.ext_is_supported(file_extension) is False:
                self.log_to_plainTextEdit_2("Error! File extension, '{}' not officially recognised currently."
                                          "Would you like to try anyway? ".format(file_extension))
                self.browse_icon_error_2()
        else:
            # Cancelled out of selecting a file
            pass

    def check_private_key(self):
        """checks private key for B tab"""
        priv_key = self.private_key_lineEdit.text()

        if bitsv.format.wif_checksum_check(priv_key):
            # Success icon!
            self.activate_icon_success()
            self.log_to_plainTextEdit('Success! Private Key is valid.')
        else:
            # Error icon.
            self.activate_icon_error()
            self.log_to_plainTextEdit('Error! Private Key is not valid.')

    def check_private_key_2(self):
        """checks private key for BCAT tab"""
        priv_key = self.private_key_lineEdit_2.text()

        if bitsv.format.wif_checksum_check(priv_key):
            # Success icon!
            self.activate_icon_success_2()
            self.log_to_plainTextEdit_2('Success! Private Key is valid.')
        else:
            # Error icon.
            self.activate_icon_error_2()
            self.log_to_plainTextEdit_2('Error! Private Key is not valid.')

    def activate_icon_success(self):
        self.activate_icon_label.setPixmap(QtGui.QPixmap(SUCCESS_ICON))

    def activate_icon_success_2(self):
        self.activate_icon_label_2.setPixmap(QtGui.QPixmap(SUCCESS_ICON))

    def activate_icon_error(self):
        self.activate_icon_label.setPixmap(QtGui.QPixmap(ERROR_ICON))

    def activate_icon_error_2(self):
        self.activate_icon_label_2.setPixmap(QtGui.QPixmap(ERROR_ICON))

    @staticmethod
    def ext_is_supported(file_extension):
        if file_extension in SUPPORTED_EXTENSIONS:
            return True
        else:
            return False

    def browse_icon_success(self):
        self.browse_icon_label.setPixmap(QtGui.QPixmap(SUCCESS_ICON))

    def browse_icon_success_2(self):
        self.browse_icon_label_2.setPixmap(QtGui.QPixmap(SUCCESS_ICON))

    def browse_icon_error(self):
        self.browse_icon_label.setPixmap(QtGui.QPixmap(ERROR_ICON))

    def browse_icon_error_2(self):
        self.browse_icon_label_2.setPixmap(QtGui.QPixmap(ERROR_ICON))

    # Get contents of outputs_plainTextEdit
    def log_to_plainTextEdit(self, output):
        """logs plain test to outputs_plainTextEdit
        e.g. txids of recently broadcasted transactions
        e.g. fee required to send currently loaded file"""
        self.outputs_plainTextEdit.setPlainText(output)

    # Get contents of outputs_plainTextEdit
    def log_to_plainTextEdit_2(self, output):
        """logs plain test to outputs_plainTextEdit
        e.g. txids of recently broadcasted transactions
        e.g. fee required to send currently loaded file"""
        self.outputs_plainTextEdit_2.setPlainText(output)

    def clear_plainTextEdit(self):
        self.outputs_plainTextEdit.clear()

    def view_content(self):
        url = self.DEFAULT_VIEWER_URL + "/" + self.LATEST_TXID
        print(self.DEFAULT_VIEWER_URL + "/" + self.LATEST_TXID)
        webbrowser.open(url)

    def view_content_2(self):
        webbrowser.open(self.DEFAULT_VIEWER_URL + self.LATEST_TXID_2)

    def broadcast(self):
        # FIXME - on broadcast list out
        priv_key = self.private_key_lineEdit.text()
        print(priv_key)
        file = self.file_name_lineEdit.text()
        print(file)
        txid = ''

        # Make rawtx
        uploader = polyglot.Upload(priv_key)
        print(uploader.get_unspents())
        rawtx = uploader.b_create_rawtx_from_file_ezmode(file)

        # FIXME - ARE YOU SURE? DIALOGUE BOX NEEDS TO GO HERE...

        # Broadcast
        txid = bitsv.network.services.BitIndex.broadcast_rawtx(rawtx)['data']['txid']  # FIXME - will need updating to handle bcat://

        # Primes the View Content Button
        self.LATEST_TXID = txid
        url = self.DEFAULT_VIEWER_URL + "/" + txid

        print(self.LATEST_TXID)
        print(self.DEFAULT_VIEWER_URL)
        print(url)

        # FIXME - only handles one txid currently and only setup for b:// NOT bcat:// (YET)
        print(txid)
        self.log_to_plainTextEdit("Success!\n"
                                  "Your file has been uploaded via the {} protocol\n".format('b://') +
                                  "txid: " + txid + "\n\n"
                                  "click on 'View Content' button to go to:\n" +
                                  "url: " + url)

    def broadcast_2(self):
        # FIXME - on broadcast list out
        priv_key = self.private_key_lineEdit_2.text()
        file = self.file_name_lineEdit_2.text()
        txid = ''

        # Make rawtx
        uploader = polyglot.Upload(priv_key)

        # FIXME - Change from b --> bcat!
        rawtx = uploader.b_create_tx_from_file_easy_mode(file)

        # FIXME - ARE YOU SURE? DIALOGUE BOX NEEDS TO GO HERE...

        # Broadcast
        txid = bitsv.network.services.BitIndex.broadcast_rawtx(rawtx)['data']['txid']  # FIXME - will need updating to handle bcat://

        # Primes the View Content Button
        self.LATEST_TXID_2 = txid
        url = self.DEFAULT_VIEWER_URL + "/" + txid

        # FIXME - only handles one txid currently and only setup for b:// NOT bcat:// (YET)
        print(txid)
        self.log_to_plainTextEdit("Success!\n"
                                  "Your file has been uploaded via the {} protocol\n".format('bcat://') +
                                  "txid: " + txid + "\n\n"
                                  "click on 'View Content' button to go to:\n" +
                                  "url: " + url)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

