from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Wine(Base):
    __tablename__ = 'vinhos'
    id_vinho = Column(Integer, primary_key=True)
    nome = Column(String(40))
    avaliacao = Column(Integer)
    uva = Column(String(40))
    armonizacao = Column(String(40))
    nacionalidade = Column(String(40))
    comentario = Column(String(40))
    id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'))
    usuario = relationship('User')



engine = create_engine('sqlite:///wines.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def add_wine(nome, avaliacao, uva, armonizacao, nacionalidade, comentario, id_usuario):
    session = Session()
    wine = Wine(nome=nome, avaliacao=avaliacao, uva=uva, armonizacao=armonizacao, nacionalidade=nacionalidade, comentario=comentario, id_usuario=id_usuario)
    session.add(wine)
    session.commit()
    session.close()

def get_top_rated_wines(limit=10):
    session = Session()
    wines = session.query(Wine).order_by(Wine.avaliacao.desc()).limit(limit).all()
    session.close()
    return wines

def get_all_wines():
    session = Session()
    all_wines = session.query(Wine).all()
    session.close()
    return all_wines

def add_user(nome):
    session = Session()
    user = User(nome=nome)
    session.add(user)
    session.commit()
    session.close()

def get_user_by_id(user_id):
    session = Session()
    user = session.query(User).filter(User.id == user_id).first()
    session.close()
    return user

def get_wines_by_user(user_id):
    session = Session()
    wines = session.query(Wine).filter(Wine.user_id == user_id).all()
    session.close()
    return wines