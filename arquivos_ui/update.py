import sys
from PyQt5 import QtCore
from models.crud_bd import *

from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *

class Update_App(QMainWindow):
  def __init__(self):
    super(Update_App, self).__init__()
    loadUi(r"arquivos_ui\ui\update.ui", self)
    self.setWindowTitle("Atualizar Tabela")

    #INPUT USUARIO, QUAL VINHO VAI ALTERAR
    self.input_pesquisar_id = self.input_pesquisar_id.text()
    self.btn_pesquisar_id.clicked.connect(lambda: self.id_vinho_para_atualizar(self.input_pesquisar_id))

    #VARIAVEIS DO VINHO PARA ALTERAR


    #VAIAVEIS NOVAS DO VINHO

    #PEGAR VALOR DO ID
  def id_vinho_para_atualizar(self, id):
    vinho = session.query(Vinho).filter_by(id=id).first()

    if vinho:
        self.pesq_nome.setText(str(vinho.id))
        self.pesq_uva.setText(vinho.uva)
        self.pesq_nota.setText(str(vinho.nota))
        self.pesq_nacionalidade.setText(vinho.nacionalidade)
        self.pesq_harmonizacao.setText(vinho.harmonizacao)
        self.pesq_coment.setText(vinho.comentario)
    else:
        self.input_pesquisar_id.setText("VINHO NÃO ENCONTRADO.")
    
    #ATUALIZAR TABELA



if __name__ == "__main__":
  app = QApplication(sys.argv)
  ui = Update_App()
  ui.show()
  app.exec_()