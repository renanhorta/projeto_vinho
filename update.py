import sys
from PyQt5 import QtCore
from crud_bd import *

from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *

class Update_App(QMainWindow):
  def __init__(self):
    super(Update_App, self).__init__()
    loadUi(r"ui\update.ui", self)
    self.setWindowTitle("Atualizar Tabela")

    #INPUT USUARIO, QUAL VINHO VAI ALTERAR
    #self.input_pesquisar_id = self.input_pesquisar_id.text()
    self.btn_pesquisar_id.clicked.connect(lambda: self.id_vinho_para_atualizar())
    self.btn_update_table.clicked.connect(lambda :self.atualizar_tabela())

    #VARIAVEIS DO VINHO PARA ALTERAR


    #VAIAVEIS NOVAS DO VINHO
  
  #Mostrar vinho selecionado
  def id_vinho_para_atualizar(self):
    id = self.input_pesquisar_id.text()
    vinho = selecionar_vinho(id)

    if vinho:
        self.pesq_nome.setText(str(vinho.nome))
        self.pesq_uva.setText(vinho.uva)
        self.pesq_ano.setText(str(vinho.ano))
        self.pesq_nota.setText(str(vinho.nota))
        self.pesq_nacionalidade.setText(vinho.nacionalidade)
        self.pesq_harmonizacao.setText(vinho.harmonizacao)
        self.pesq_coment.setText(vinho.comentario)
    else:
        self.input_pesquisar_id.setText("VINHO NÃO ENCONTRADO.")
        self.pesq_nome.clear()
        self.pesq_uva.clear()
        self.pesq_ano.clear()
        self.pesq_nota.clear()
        self.pesq_nacionalidade.clear()
        self.pesq_harmonizacao.clear()
        self.pesq_coment.clear()
    
  #ATUALIZAR TABELA

  def atualizar_tabela(self):
    id = self.input_pesquisar_id.text()
    vinho = selecionar_vinho(id)
    print(vinho)
    #VARIAVEIS NOVAS 
    nome_nova = self.update_nome.text()
    uva_nova = self.update_uva.text()
    ano_nova = self.update_ano.text()
    nota_nova = self.update_nota.text()
    nacionalidade_nova = self.update_nacionalidade.text()
    harmonizacao_nova = self.update_harmonizacao.text()
    coment_nova = self.update_coment.toPlainText()

    #ATUALIZA O VINHO
    vinho.nome = nome_nova
    vinho.uva = uva_nova
    vinho.ano = int(ano_nova)
    vinho.nota = float(nota_nova)
    vinho.nacionalidade = nacionalidade_nova
    vinho.harmonizacao = harmonizacao_nova
    vinho.comentario = coment_nova
    session.commit()
    print(vinho)



     


if __name__ == "__main__":
  app = QApplication(sys.argv)
  ui = Update_App()
  ui.show()
  app.exec_()