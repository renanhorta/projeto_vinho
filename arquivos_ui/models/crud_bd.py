from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


engine = create_engine('sqlite:///vinhos.db', echo = True)
Base = declarative_base()

class Vinho(Base):
    __tablename__ = 'vinhos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    uva = Column(String(50), nullable=False)
    nacionalidade = Column(String(50))
    nota = Column(Integer)
    harmonizacao = Column(String(200))
    comentario = Column(String(500))

    def repr (self):
        return "<Vinho{nome={}}, Nota{nota={}}, Uva{uva={}}, Pais{nacionalidade={}}, harmoniza com{harmonizacao={}}>".format(self.nome,self.nota, self.uva, self.nacionalidade, self.harmonizacao)
    
# Cria as tabelas no banco de dados
Base.metadata.create_all(engine)

# Cria uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()
#####   QUERYS

# ADD IN TABLE
def add_vinho(nome, nota, uva, harmonizacao, nacionalidade, comentario):
    session = Session()
    vinho = Vinho(nome=nome, nota=nota, uva=uva, harmonizacao=harmonizacao, nacionalidade=nacionalidade, comentario=comentario)
    session.add(vinho)
    session.commit()
    session.close()
    print("\nAdição feita com sucesso")


# READ TEABLE

def todos_os_vinho():
    session = Session()
    todos_vinhos = session.query(Vinho).all()
    session.close()
    return todos_vinhos  

# REMOVE WINE

def remover_ultimo_vinho():
    session = Session()
    ultimo_id_vinho = session.query(Vinho.id_vinho).order_by(desc(Vinho.id_vinho)).first()

    if ultimo_id_vinho:
        # Apagar o vinho com o último ID
        session.query(Vinho).filter_by(id_vinho=ultimo_id_vinho[0]).delete()
        session.commit()
    else:
        print("Não há vinhos para remover.")