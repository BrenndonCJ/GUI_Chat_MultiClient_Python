# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Tela_Chat_Final2MVXvIF.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TelaXAT(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(303, 560)
        MainWindow.setMinimumSize(QSize(303, 560))
        MainWindow.setMaximumSize(QSize(303, 560))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.0);")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.main_frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.main_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 20))
        self.frame.setMaximumSize(QSize(300, 16777215))
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.exit_button = QPushButton(self.frame)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setMinimumSize(QSize(20, 20))
        self.exit_button.setMaximumSize(QSize(20, 20))
        self.exit_button.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 0.01);\n"
"border-radius: 5px;\n"
"font: 63 10pt \"Fira Code SemiBold\";\n"
"color: rgba(255, 255, 255, 0.0);\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgba(255, 255, 255, 0.3);\n"
"border-radius: 5px;\n"
"font: 63 10pt \"Fira Code SemiBold\";\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton::pressed{	\n"
"	color: rgb(0, 255, 0);\n"
"	background-color: qlineargradient(spread:pad, x1:0.358, y1:0.574, x2:1, y2:0, stop:0 rgba(0, 0, 0, 198), stop:1 rgba(255, 255, 255, 0));\n"
"}")

        self.horizontalLayout.addWidget(self.exit_button)


        self.verticalLayout_4.addWidget(self.frame)

        self.frame_principal = QFrame(self.main_frame)
        self.frame_principal.setObjectName(u"frame_principal")
        self.frame_principal.setMinimumSize(QSize(0, 0))
        self.frame_principal.setMaximumSize(QSize(16777215, 16777215))
        self.frame_principal.setStyleSheet(u"QFrame #frame_principal{\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 0, 0, 223), stop:1 rgba(0, 0, 0, 97));\n"
"	border-radius: 20px;\n"
"}")
        self.frame_principal.setFrameShape(QFrame.StyledPanel)
        self.frame_principal.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_principal)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_user = QFrame(self.frame_principal)
        self.frame_user.setObjectName(u"frame_user")
        self.frame_user.setFrameShape(QFrame.NoFrame)
        self.frame_user.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_user)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(6, 4, 6, 0)
        self.horizontalSpacer = QSpacerItem(20, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.label_user = QLabel(self.frame_user)
        self.label_user.setObjectName(u"label_user")
        self.label_user.setStyleSheet(u"font: 63 8pt \"Fira Code SemiBold\";\n"
"color: rgb(255, 255, 255);")
        self.label_user.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_user)

        self.button_exit = QPushButton(self.frame_user)
        self.button_exit.setObjectName(u"button_exit")
        self.button_exit.setMinimumSize(QSize(0, 20))
        self.button_exit.setMaximumSize(QSize(20, 16777215))
        self.button_exit.setLayoutDirection(Qt.LeftToRight)
        self.button_exit.setStyleSheet(u"QPushButton{\n"
"font: 87 8pt \"Arial Black\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.477, x2:1, y2:0.489, stop:0 rgba(0, 0, 0, 81), stop:1 rgba(255, 255, 255, 173));\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	color: rgb(247, 247, 0);\n"
"	background-color: rgba(0, 0, 0, 0.5);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	color: rgb(0, 255, 0);\n"
"}")

        self.horizontalLayout_4.addWidget(self.button_exit)


        self.verticalLayout_2.addWidget(self.frame_user)

        self.frame_cabecalho = QFrame(self.frame_principal)
        self.frame_cabecalho.setObjectName(u"frame_cabecalho")
        self.frame_cabecalho.setMinimumSize(QSize(301, 55))
        self.frame_cabecalho.setMaximumSize(QSize(300, 55))
        self.frame_cabecalho.setStyleSheet(u"")
        self.frame_cabecalho.setFrameShape(QFrame.StyledPanel)
        self.frame_cabecalho.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_cabecalho)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.label = QLabel(self.frame_cabecalho)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(45, 45))
        self.label.setMaximumSize(QSize(45, 45))
        self.label.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 174, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 22px;")

        self.horizontalLayout_2.addWidget(self.label)

        self.cha_name = QLabel(self.frame_cabecalho)
        self.cha_name.setObjectName(u"cha_name")
        self.cha_name.setMinimumSize(QSize(0, 40))
        self.cha_name.setMaximumSize(QSize(16777215, 40))
        self.cha_name.setStyleSheet(u"font: 12pt \"Comic Sans MS\";\n"
"color: rgb(218, 145, 0);background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 174, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.cha_name.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.cha_name)


        self.verticalLayout_2.addWidget(self.frame_cabecalho)

        self.frame_body = QFrame(self.frame_principal)
        self.frame_body.setObjectName(u"frame_body")
        self.frame_body.setMinimumSize(QSize(298, 398))
        self.frame_body.setMaximumSize(QSize(298, 398))
        self.frame_body.setStyleSheet(u"QTextBrowser{\n"
"	background-color: rgba(255, 255, 255, 0.3);\n"
"	border-radius: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 63 10pt \"Fira Code SemiBold\";\n"
"}")
        self.frame_body.setFrameShape(QFrame.StyledPanel)
        self.frame_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_body)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 0, 2, 0)
        self.menssage_box = QTextBrowser(self.frame_body)
        self.menssage_box.setObjectName(u"menssage_box")
        self.menssage_box.setFocusPolicy(Qt.StrongFocus)

        self.verticalLayout_3.addWidget(self.menssage_box)


        self.verticalLayout_2.addWidget(self.frame_body)

        self.frame_bottom = QFrame(self.frame_principal)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setMinimumSize(QSize(301, 61))
        self.frame_bottom.setMaximumSize(QSize(300, 61))
        self.frame_bottom.setStyleSheet(u"\n"
"QTextEdit{\n"
"background-color: rgba(136, 136, 136, 0.3);\n"
"font: 63 10pt \"Fira Code SemiBold\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLabel{\n"
"background-color: rgba(136, 136, 136, 0.3);\n"
"}\n"
"\n"
"QFrame::QLabel #sparser_left{\n"
"border-top-left-radius: 15px;\n"
"border-bottom-left-radius: 15px;\n"
"}\n"
"\n"
"QFrame::QLabel #sparser_right{\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;\n"
"}")
        self.frame_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_bottom)
        self.horizontalLayout_5.setSpacing(4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.sparser_left = QLabel(self.frame_bottom)
        self.sparser_left.setObjectName(u"sparser_left")
        self.sparser_left.setMinimumSize(QSize(15, 0))
        self.sparser_left.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.sparser_left)

        self.entry_message = QTextEdit(self.frame_bottom)
        self.entry_message.setObjectName(u"entry_message")
        self.entry_message.setStyleSheet(u"")
        self.entry_message.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_3.addWidget(self.entry_message)

        self.sparser_right = QLabel(self.frame_bottom)
        self.sparser_right.setObjectName(u"sparser_right")
        self.sparser_right.setMinimumSize(QSize(15, 0))
        self.sparser_right.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.sparser_right)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)

        self.send_message = QPushButton(self.frame_bottom)
        self.send_message.setObjectName(u"send_message")
        self.send_message.setMinimumSize(QSize(35, 25))
        self.send_message.setMaximumSize(QSize(35, 25))
        self.send_message.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(64, 194, 0,0.7);\n"
"color: rgb(250, 250, 250);\n"
"border-radius: 10px;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"border: 1px solid #ffffff;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid #216300;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"color: rgb(64, 194, 0);\n"
"}")

        self.horizontalLayout_5.addWidget(self.send_message)


        self.verticalLayout_2.addWidget(self.frame_bottom)


        self.verticalLayout_4.addWidget(self.frame_principal)


        self.verticalLayout.addWidget(self.main_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.exit_button.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.label_user.setText(QCoreApplication.translate("MainWindow", u"User1", None))
        self.button_exit.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; color:#000000;\">\u2606</span></p></body></html>", None))
        self.cha_name.setText(QCoreApplication.translate("MainWindow", u"SISTEMAS DISTRIBUIDOS", None))
        self.menssage_box.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Fira Code SemiBold'; font-size:10pt; font-weight:56; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.sparser_left.setText("")
        self.entry_message.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Fira Code SemiBold'; font-size:10pt; font-weight:56; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.entry_message.setPlaceholderText(QCoreApplication.translate("MainWindow", u"         menssagem", None))
        self.sparser_right.setText("")
        self.send_message.setText(QCoreApplication.translate("MainWindow", u"\u27a4", None))
    # retranslateUi


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    TelaXAT = QMainWindow()
    ui = Ui_TelaXAT()
    ui.setupUi(TelaXAT)
    TelaXAT.show()
    sys.exit(app.exec_())