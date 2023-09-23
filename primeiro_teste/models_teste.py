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
    nome_usuario= Column(String(100))

    def repr (self):
        return "<Vinho{nome={}}, Nota{nota={}}, Uva{uva={}}, Pais{nacionalidade={}}, harmoniza com{harmonizacao={}}>".format(self.nome,self.nota, self.uva, self.nacionalidade, self.harmonizacao)
    
# Cria as tabelas no banco de dados
Base.metadata.create_all(engine)

# Cria uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()


# Create (inserir um novo vinho)
def novo_vinho(nome, uva, nota, nacionalidade, harmonizacao, comentario, nome_usuario):
    novo_vinho = Vinho(nome=nome, uva=uva, nota=nota, nacionalidade=nacionalidade,
                       harmonizacao=harmonizacao, comentario=comentario, nome_usuario=nome_usuario)
    session.add(novo_vinho)
    session.commit()
    
# Read (consultar um vinho por nome)
def consultar_vinho_por_nome(nome_vinho):
    vinho_consultado = session.query(Vinho).filter_by(nome=nome_vinho).first()
    if vinho_consultado:
        print(f'Vinho: {vinho_consultado.nome}\nUva: {vinho_consultado.uva}\nPais: {vinho_consultado.nacionalidade}\nNota: {vinho_consultado.nota}')

# Pesquisar vinhos por ID do usuário
def pesquisar_vinhos_por_id(usuario_id):
    vai_gostar_vinhos = session.query(Vinho).filter_by(usuario_id=usuario_id).all()
    for vinho in vai_gostar_vinhos:
        print(f'Vinho: {vinho.nome}, Uva: {vinho.uva}, Nota: {vinho.nota}, Harmonização: {vinho.harmonizacao}, Comentário: {vinho.comentario}')

def top_10_vinhos():
    session = Session()
    vinho_consultado = session.query(Vinho).filter_by(id=vinho_id).first()
    if vinho_consultado:
        session.delete(vinho_consultado)
        session.commit()

def todos_os_vinho():
    session = Session()
    todos_vinhos = session.query(Vinho).all()
    session.close()
    return todos_vinhos        

# Update (atualizar os dados de um vinho)
def atualizar_vinho(vinho_id, nova_nota):
    session = Session()
    vinho_consultado = session.query(Vinho).filter_by(id=vinho_id).first()
    if vinho_consultado:
        vinho_consultado.nota = nova_nota
        session.commit()


# Delete (excluir um vinho)
def excluir_vinho(vinho_id):
    session = Session()
    vinho_consultado = session.query(Vinho).filter_by(id=vinho_id).first()
    if vinho_consultado:
        session.delete(vinho_consultado)
        session.commit()
