import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from visualizar import *
from avaliar import *

class StartApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Avaliação de Vinhos')
        self.setGeometry(300, 300, 400, 200)

        #self.user_label = QLabel('Digite seu nome:')
        #self.user_edit = QLineEdit()

        self.avaliar_button = QPushButton('Avaliar')
        self.avaliar_button.clicked.connect(self.start_avaliar_app)

        self.visualizar_button = QPushButton('Visualizar')
        self.visualizar_button.clicked.connect(self.start_visualizar_app)

        self.remove_button = QPushButton('Excluir a ultima avaliação')
        self.remove_button.clicked.connect(self.delete_last_wine)

        layout = QVBoxLayout()
        #layout.addWidget(self.user_label)
        #layout.addWidget(self.user_edit)
        layout.addWidget(self.avaliar_button)
        layout.addWidget(self.visualizar_button)
        layout.addWidget(self.remove_button)

        self.setLayout(layout)

    def start_avaliar_app(self):
        self.avaliar_app = WineApp()

        self.avaliar_app.show()
        self.close()

    
    def start_visualizar_app(self):
        self.visualizar_app = App_visualizar()
        
        self.visualizar_app.show()
        self.close()

    def delete_last_wine(self):
        pass
        

    def show_menu(self):
        self.user_edit.clear()
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    start_app = StartApp()
    start_app.show()
    sys.exit(app.exec_())
