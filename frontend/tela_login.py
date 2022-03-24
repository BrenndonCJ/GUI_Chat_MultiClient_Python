from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TelaLogin(object):
    def setupUi(self, TelaLogin):
        if not TelaLogin.objectName():
            TelaLogin.setObjectName(u"TelaLogin")
        TelaLogin.resize(300, 195)
        TelaLogin.setMinimumSize(QSize(300, 195))
        TelaLogin.setMaximumSize(QSize(300, 195))
        self.centralwidget = QWidget(TelaLogin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(16777215, 167772))
        self.centralwidget.setStyleSheet(u"QWidget #centralwidget{\n"
"background-color: rgba(0, 0, 0, 0.3);\n"
"border-radius: 20px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 1677772))
        self.frame.setCursor(QCursor(Qt.ArrowCursor))
        self.frame.setFocusPolicy(Qt.NoFocus)
        self.frame.setLayoutDirection(Qt.LeftToRight)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 20))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(260, 0, 21, 23))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(255, 255, 255, 0.3);\n"
"border-radius: 5px;\n"
"font: 63 10pt \"Fira Code SemiBold\";\n"
"}\n"
"\n"
"QPushButton::pressed{	\n"
"	color: rgb(214, 214, 0);\n"
"	background-color: qlineargradient(spread:pad, x1:0.358, y1:0.574, x2:1, y2:0, stop:0 rgba(0, 0, 0, 198), stop:1 rgba(255, 255, 255, 0));\n"
"}")

        self.verticalLayout_2.addWidget(self.frame_3)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setFamily(u"Fira Code SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.username = QLineEdit(self.frame)
        self.username.setObjectName(u"username")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username.sizePolicy().hasHeightForWidth())
        self.username.setSizePolicy(sizePolicy)
        self.username.setMinimumSize(QSize(190, 25))
        self.username.setMaximumSize(QSize(190, 25))
        self.username.setFocusPolicy(Qt.ClickFocus)
        self.username.setLayoutDirection(Qt.LeftToRight)
        self.username.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.username)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.button_login = QPushButton(self.frame)
        self.button_login.setObjectName(u"button_login")
        self.button_login.setMinimumSize(QSize(75, 25))
        self.button_login.setMaximumSize(QSize(75, 25))
        self.button_login.setFocusPolicy(Qt.NoFocus)
        self.button_login.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.button_login)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 15))
        self.frame_2.setMaximumSize(QSize(16777215, 15))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(160, 0, 0, 0)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_status = QLabel(self.frame_2)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setMaximumSize(QSize(10, 10))
        self.label_status.setStyleSheet(u"border-radius:5px;\n"
"background-color: rgb(0, 255, 0);")

        self.horizontalLayout.addWidget(self.label_status)

        self.label_on_off = QLabel(self.frame_2)
        self.label_on_off.setObjectName(u"label_on_off")

        self.horizontalLayout.addWidget(self.label_on_off)


        self.verticalLayout.addWidget(self.frame_2)

        TelaLogin.setCentralWidget(self.centralwidget)

        self.retranslateUi(TelaLogin)

        QMetaObject.connectSlotsByName(TelaLogin)
    # setupUi

    def retranslateUi(self, TelaLogin):
        TelaLogin.setWindowTitle(QCoreApplication.translate("TelaLogin", u"Login XAT", None))
        self.pushButton.setText(QCoreApplication.translate("TelaLogin", u"x", None))
        self.label.setText(QCoreApplication.translate("TelaLogin", u"<html><head/><body><p><span style=\" color:#ffffff;\">Insira seu nome</span></p></body></html>", None))
        self.button_login.setText(QCoreApplication.translate("TelaLogin", u"Entrar", None))
        self.label_2.setText(QCoreApplication.translate("TelaLogin", u"Status Server", None))
        self.label_status.setText("")
        self.label_on_off.setText(QCoreApplication.translate("TelaLogin", u"online", None))
    # retranslateUi


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    TelaLogin = QMainWindow()
    ui = Ui_TelaLogin()
    ui.setupUi(TelaLogin)
    TelaLogin.show()
    sys.exit(app.exec_())