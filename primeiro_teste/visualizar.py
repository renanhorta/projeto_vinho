from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication
import sys
from models_teste import *

class WineVisualizationApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Visualização de Vinhos')
        self.setGeometry(300, 300, 400, 400)

        self.top_rated_button = QPushButton('10 Melhores Vinhos')
        self.top_rated_button.clicked.connect(self.mostrar_top10)

        self.all_wines_button = QPushButton('Todos os Vinhos')
        self.all_wines_button.clicked.connect(self.show_all_wines)

        self.user_wines_button = QPushButton('Avaliações do Usuário')
        self.user_wines_button.clicked.connect(self.show_user_wines)

        layout = QVBoxLayout()
        layout.addWidget(self.top_rated_button)
        layout.addWidget(self.all_wines_button)
        layout.addWidget(self.user_wines_button)

        self.setLayout(layout)

    def mostrar_top10(self):
        vinhos = top_10_vinhos()
        self.mostrar_vinhos(vinhos)

    #def consultar_vinho(self):
        #vinho = consultar_vinho_por_nome()
        

    def show_all_wines(self):
        vinhos = todos_os_vinho()
        self.mostrar_vinhos(vinhos)

    def show_user_wines(self):
        user = get_user_by_id(self.user_id)
        if user:
            wines = get_wines_by_user(self.user_id)
            self.mostrar_vinhos(wines)
        else:
            print('Usuário não encontrado.')

    def mostrar_vinhos(self, vinhos):
        print('Avaliações de Vinho:')
        for vinho in vinhos:
            print(f'Nome: {vinho.nome}, Nota: {vinho.nota}, Uva: {vinho.uva}, Harmonização: {vinho.harmonizacao}, Nacionalidade: {vinho.nacionalidade}, Comentário: {vinho.comentario}')

if __name__ == '__main__':
    # Este é apenas um exemplo de como usar a interface de visualização
    # Substitua pelo código que você deseja usar para exibir a interface
    app = QApplication(sys.argv)
    ex = WineVisualizationApp()
    ex.show()
    app.exec_()
