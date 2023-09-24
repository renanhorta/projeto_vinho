import sys
from PyQt5 import QtCore
from crud_bd import *
from update import Update_App

from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *

class Main_app(QMainWindow):
  def __init__(self):
    super(Main_app, self).__init__()
    loadUi(r"ui\menu.ui", self)
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

    #PESQUISAR VINHOS
    self.pesquisar_vinho_btn.clicked.connect(lambda: self.pesquisar_vinho())

    #MOSTRAR DATABASE INTEIRA (MOSTRAR TODOS OS VINHOS)
    self.todos_vinhos_btn.clicked.connect(lambda: self.carregar_db())
    self.todos_vinhos_btn.clicked.connect(lambda: self.Pages_show.setCurrentWidget(self.page_show_visualizar))

    #REMOVER ULTIMA AVALIACAO
    self.remover_btn.clicked.connect(lambda: self.excluir_ultima_avaliacao())

    #UPDATE TABLE
    self.update_btn.clicked.connect(lambda: self.atualizar_table())

    #MOSTRAT TOP 5
    self.top10_btn.clicked.connect(lambda: self.pesquisar_melhores_vinhos())
    self.top10_btn.clicked.connect(lambda: self.Pages_show.setCurrentWidget(self.page_show_top_vinhos))
    
    
  #carregar DB
  def carregar_db(self):
    database = session.query(Vinho).all()

    self.vinho_table.setRowCount(len(database))
    self.vinho_table.setColumnCount(8)

    for i, vinho in enumerate(database):
          self.vinho_table.setItem(i, 0, QTableWidgetItem(str(vinho.id)))
          self.vinho_table.setItem(i, 1, QTableWidgetItem(vinho.nome))
          self.vinho_table.setItem(i, 2, QTableWidgetItem(vinho.uva))
          self.vinho_table.setItem(i, 3, QTableWidgetItem(str(vinho.ano)))
          self.vinho_table.setItem(i, 4, QTableWidgetItem(vinho.nacionalidade))
          self.vinho_table.setItem(i, 5, QTableWidgetItem(str(vinho.nota)))
          self.vinho_table.setItem(i, 6, QTableWidgetItem(vinho.harmonizacao))
          self.vinho_table.setItem(i, 7, QTableWidgetItem(vinho.comentario))

  def enviar_vinho(self):
    #Vinho(nome=nome, avaliacao=avaliacao, uva=uva, armonizacao=armonizacao, nacionalidade=nacionalidade, comentario=comentario)

    #INPUTS DA AVALIAÇÃO
    self.nome_vinho = self.input_nome_vinho.text()
    self.uva_vinho = self.input_uva.text()
    self.ano_vinho = self.input_ano.text()
    self.nota_vinho = self.input_nota.text()
    self.harmo_vinho = self.input_harmonizacao.text()
    self.pais_vinho = self.input_pais.text()
    self.coment_vinho = self.input_coment.toPlainText()    

    add_vinho(self.nome_vinho, self.nota_vinho, self.uva_vinho, self.ano_vinho,self.harmo_vinho,self.pais_vinho,self.coment_vinho, None)
    self.input_nome_vinho.clear()
    self.input_uva.clear()
    self.input_ano.clear()
    self.input_nota.clear()
    self.input_harmonizacao.clear()
    self.input_pais.clear()
    self.input_coment.clear()
    

  def excluir_ultima_avaliacao(self):
    remover_ultimo_vinho()
    

  def atualizar_table(self):
    self.update_app = Update_App()
    self.update_app.show()
     
  def pesquisar_vinho(self):
    vinho = self.input_nome.text()

    vinhos = pesquisar_vinho_por_nome(vinho)

    if vinhos:
      # Limpar a tabela
      self.vinho_table.clearContents()
      self.vinho_table.setRowCount(len(vinhos))
      self.vinho_table.setColumnCount(8)

      for i, vinho in enumerate(vinhos):
          self.vinho_table.setItem(i, 0, QTableWidgetItem(str(vinho.id)))
          self.vinho_table.setItem(i, 1, QTableWidgetItem(vinho.nome))
          self.vinho_table.setItem(i, 2, QTableWidgetItem(vinho.uva))
          self.vinho_table.setItem(i, 3, QTableWidgetItem(str(vinho.ano)))
          self.vinho_table.setItem(i, 4, QTableWidgetItem(vinho.nacionalidade))
          self.vinho_table.setItem(i, 5, QTableWidgetItem(str(vinho.nota)))
          self.vinho_table.setItem(i, 6, QTableWidgetItem(vinho.harmonizacao))
          self.vinho_table.setItem(i, 7, QTableWidgetItem(vinho.comentario))
    else:
      self.input_nome.setText("NÃO ENCONTRADO")

    
  def pesquisar_melhores_vinhos(self):
    melhores_vinhos = pesquisar_top10()
    print(melhores_vinhos)

    #for idx, vinho in enumerate(melhores_vinhos, start=1):
        #print(f"{idx}. {vinho.nome}: {vinho.average_rating:.2f}")

    #melhores_vinhos = pesquisar_top5()
    #print(melhores_vinhos)

    # Limpar a tabela
    self.top_vinhos_table.clearContents()
    self.top_vinhos_table.setRowCount(len(melhores_vinhos))
    self.top_vinhos_table.setColumnCount(2)

    for i, vinho in enumerate(melhores_vinhos):
        #self.vinho_table.setItem(i, 0, QTableWidgetItem(str(vinho.id)))
        self.top_vinhos_table.setItem(i, 0, QTableWidgetItem(vinho.nome))
        #self.vinho_table.setItem(i, 2, QTableWidgetItem(vinho.uva))
        #self.vinho_table.setItem(i, 3, QTableWidgetItem(str(vinho.ano)))
        #self.vinho_table.setItem(i, 4, QTableWidgetItem(vinho.nacionalidade))
        self.top_vinhos_table.setItem(i, 1, QTableWidgetItem(str(vinho.nota_media)))
        #self.vinho_table.setItem(i, 6, QTableWidgetItem(vinho.harmonizacao))
        #self.vinho_table.setItem(i, 7, QTableWidgetItem(vinho.comentario))


if __name__ == "__main__":
  app = QApplication(sys.argv)
  ui = Main_app()
  ui.show()
  app.exec_()