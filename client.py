import sys
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from frontend.tela_login import *
from frontend.tela_chat import *


class TelaXat(QMainWindow):
    def __init__(self, cs, username):
        super().__init__()

        self.client_socket = cs
        
        # Load GUIs
        self.tela_chat = Ui_TelaXAT()
        self.tela_chat.setupUi(self)
        self.tela_chat.label_user.setText(username)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Mover Janela
        self.tela_chat.label_user.mouseMoveEvent = self.moveWindow
        self.tela_chat.cha_name.mouseMoveEvent = self.moveWindow

        receive_thread = Thread(target=self.recebe)
        receive_thread.start()
        
        # Call Functions
        self.tela_chat.send_message.clicked.connect(self.btSend)
        self.tela_chat.button_exit.clicked.connect(self.exit_)
        self.tela_chat.exit_button.clicked.connect(self.quit_)

    # Functions
    def btSend(self):
        msg = self.tela_chat.entry_message.toPlainText()
        self.client_socket.send(msg.encode())
        self.tela_chat.entry_message.setText('')

    def recebe(self):
        """Lida com o recebimento de mensagens"""
        while True:
            try:
                msg = self.client_socket.recv(1024).decode("utf8")
                self.tela_chat.menssage_box.append(f'@{msg}')

            except OSError:  # Possivelmente o cliente saiu do chat.
                break

    def exit_(self):
        self.client_socket.close()
        self.tela_login = MainWindow()
        self.tela_login.show()
        self.hide()

    def closeEvent(self, event):
        self.client_socket.close()
        event.accept()

        # mover janela
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def moveWindow(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()

    # quit Janela
    def quit_(self):
        self.close()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Conexão com o server
        HOST = "localhost"
        PORT = 50000
        self.ADDR = (HOST, PORT)
        self.client_socket = socket(AF_INET, SOCK_STREAM)

        threadConn = Thread(target=self.ver_conn)
        threadConn.start()
        
        # Load GUIs
        self.ui = Ui_TelaLogin()
        self.ui.setupUi(self)
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # Mover Janela
        self.ui.frame.mouseMoveEvent = self.moveWindow

        self.ui.label_status.setStyleSheet(u"border-radius:5px;\n"
"background-color: rgb(255, 0, 0);")

        # Call Functions
        self.ui.button_login.clicked.connect(self.login)
        self.ui.pushButton.clicked.connect(self.quit_)

    # Functions
    def ver_conn(self):
        while True:
            try:
                self.client_socket.connect(self.ADDR)
                self.ui.label_status.setStyleSheet(u"border-radius:5px;\n"
    "background-color: rgb(0, 255, 0);")
                self.ui.label_on_off.setText('online')
                break
            except:                
                pass

    def login(self):
        user = self.ui.username.text()
        print(user)
        self.client_socket.send(user.encode())
        self.tela_chat = TelaXat(self.client_socket, f'@{user}')
        self.tela_chat.show()
        self.hide()

    # mover janela
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def moveWindow(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()

    # quit Janela
    def quit_(self):
        self.close()


if __name__ == "__main__":

    n_clients = 3   # Defina o numero de clientes a serem inicializados

    app = QApplication(sys.argv)
    window = [MainWindow() for _ in range(n_clients)]
    for w in window:
        w.show()
        
    sys.exit(app.exec_())