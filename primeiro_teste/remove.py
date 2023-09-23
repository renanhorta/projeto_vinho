from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Wine(Base):
    __tablename__ = 'wines'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    rating = Column(Integer)
    grape = Column(String)
    pairing = Column(String)
    origin = Column(String)
    comment = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User')

# Configuração do banco de dados
DATABASE_URL = 'sqlite:///wines.db'
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# Restante do código permanece igual...

def delete_last_wine():
    session = Session()
    last_wine = session.query(Wine).order_by(Wine.id.desc()).first()
    if last_wine:
        session.delete(last_wine)
        session.commit()
        print('Última avaliação excluída com sucesso.')
    else:
        print('Não há avaliações para excluir.')

# Restante do código permanece igual...
