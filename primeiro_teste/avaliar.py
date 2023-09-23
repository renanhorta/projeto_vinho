import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from models_teste import *

class WineApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Avaliação de Vinhos')
        self.setGeometry(300, 300, 400, 300)

        self.nome_vinho_label = QLabel('Nome do Vinho:')
        self.nome_vinho_edit = QLineEdit()

        self.nota_label = QLabel('Nota:')
        self.nota_edit = QLineEdit()

        self.uva_label = QLabel('Uva:')
        self.uva_edit = QLineEdit()

        self.harmonizacao_label = QLabel('Harmonização:')
        self.harmonizacao_edit = QLineEdit()

        self.nacionalidade_label = QLabel('Pais:')
        self.nacionalidade_edit = QLineEdit()

        self.comentario_label = QLabel('Comentário:')
        self.comentario_edit = QTextEdit()

        self.nome_user_label = QLabel('Nome do Usuário:')
        self.nome_user_edit = QLineEdit()

        self.enviar_btn = QPushButton('Submeter')
        self.enviar_btn.clicked.connect(self.submit_data)

        layout = QVBoxLayout()
        layout.addWidget(self.nome_vinho_label)
        layout.addWidget(self.nome_vinho_edit)
        layout.addWidget(self.nota_label)
        layout.addWidget(self.nota_edit)
        layout.addWidget(self.uva_label)
        layout.addWidget(self.uva_edit)
        layout.addWidget(self.harmonizacao_label)
        layout.addWidget(self.harmonizacao_edit)
        layout.addWidget(self.nacionalidade_label)
        layout.addWidget(self.nacionalidade_edit)
        layout.addWidget(self.comentario_label)
        layout.addWidget(self.comentario_edit)
        layout.addWidget(self.nome_user_label)
        layout.addWidget(self.nome_user_edit)
        layout.addWidget(self.enviar_btn)

        self.setLayout(layout)

    def submit_data(self):
        nome = self.nome_vinho_edit.text()
        nota = int(self.nota_edit.text())
        uva = self.uva_edit.text()
        harmonizacao = self.harmonizacao_edit.text()
        nacionalidade = self.nacionalidade_edit.text()
        comentario = self.comentario_edit.toPlainText()
        nome_usuario = self.nome_user_edit.text()

        # Adiciona a avaliação do vinho associada ao usuário
        novo_vinho(nome, uva, nota, nacionalidade, harmonizacao, comentario, nome_usuario)
        print('Avaliação de vinho submetida com sucesso!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WineApp()
    ex.show()
    sys.exit(app.exec_())
