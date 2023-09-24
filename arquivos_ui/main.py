import sys
from PyQt5 import QtCore
from models.crud_bd import *
from update import Update_App

from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *

class Main_app(QMainWindow):
  def __init__(self):
    super(Main_app, self).__init__()
    loadUi(r"arquivos_ui\ui\menu.ui", self)
    self.setWindowTitle("Avaliador de Vinho")

    #TROCA PARA PAGINA VISUALIZAR
    self.visualizar_btn.clicked.connect(lambda: self.Pages_menu.setCurrentWidget(self.page_visualizar))
    self.visualizar_btn.clicked.connect(lambda:self.Pages_show.setCurrentWidget(self.page_show_visualizar))

    self.visualizar_btn_avaliar.clicked.connect(lambda: self.Pages_menu.setCurrentWidget(self.page_visualizar))
    self.visualizar_btn_avaliar.clicked.connect(lambda:self.Pages_show.setCurrentWidget(self.page_show_visualizar))

    #TROCA PARA PAGINA AVALIAR
    self.avaliar_btn.clicked.connect(lambda: self.Pages_menu.setCurrentWidget(self.page_avaliar))
    self.avaliar_btn.clicked.connect(lambda: self.Pages_show.setCurrentWidget(self.page_show_avaliar))

    self.avaliar_btn_visualizar.clicked.connect(lambda: self.Pages_menu.setCurrentWidget(self.page_avaliar))
    self.avaliar_btn_visualizar.clicked.connect(lambda: self.Pages_show.setCurrentWidget(self.page_show_avaliar))

    #ENVIO DO VINHO NOVO PARA A TABELA
    self.btn_enviar.clicked.connect(lambda: self.enviar_vinho())

    #MOSTRAR DATABASE INTEIRA (MOSTRAR TODOS OS VINHOS)
    self.todos_vinhos_btn.clicked.connect(lambda: self.carregar_db())

    #REMOVER ULTIMA AVALIACAO
    self.remover_btn.clicked.connect(lambda: self.excluir_ultima_avaliacao())

    #UPDATE TABLE
    self.update_btn.clicked.connect(lambda: self.atualizar_table())

  #carregar DB
  def carregar_db(self):
    database = session.query(Vinho).all()

    self.vinho_table.setRowCount(len(database))
    self.vinho_table.setColumnCount(6)

    for i, vinho in enumerate(database):
          self.vinho_table.setItem(i, 0, QTableWidgetItem(str(vinho.id)))
          self.vinho_table.setItem(i, 1, QTableWidgetItem(vinho.nome))
          self.vinho_table.setItem(i, 2, QTableWidgetItem(vinho.uva))
          self.vinho_table.setItem(i, 3, QTableWidgetItem(vinho.nacionalidade))
          self.vinho_table.setItem(i, 4, QTableWidgetItem(str(vinho.nota)))
          self.vinho_table.setItem(i, 5, QTableWidgetItem(vinho.comentario))

  def enviar_vinho(self):
    #Vinho(nome=nome, avaliacao=avaliacao, uva=uva, armonizacao=armonizacao, nacionalidade=nacionalidade, comentario=comentario)

    #INPUTS DA AVALIAÇÃO
    self.nome_vinho = self.input_nome_vinho.text()
    self.uva_vinho = self.input_uva.text()
    self.nota_vinho = self.input_nota.text()
    self.harmo_vinho = self.input_harmonizacao.text()
    self.pais_vinho = self.input_pais.text()
    self.coment_vinho = self.input_coment.toPlainText()
    print(self.nome_vinho,self.uva_vinho,self.nota_vinho,self.coment_vinho)
    

    add_vinho(self.nome_vinho, self.nota_vinho, self.uva_vinho,self.harmo_vinho,self.pais_vinho,self.coment_vinho, None)
    self.input_nome_vinho.clear()
    self.input_uva.clear()
    self.input_nota.clear()
    self.input_harmonizacao.clear()
    self.input_pais.clear()
    self.input_coment.clear()
    

  def excluir_ultima_avaliacao(self):
    remover_ultimo_vinho()
    

  def atualizar_table(self):
    self.update_app = Update_App()
    self.update_app.show()
     
  def pesquisar_vinho(self, vinho):
    self.vinho_pesquisado = pesquisar_vinho(vinho)
    


if __name__ == "__main__":
  app = QApplication(sys.argv)
  ui = Main_app()
  ui.show()
  app.exec_()