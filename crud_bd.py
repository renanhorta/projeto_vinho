from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import desc, func


engine = create_engine('sqlite:///vinhos.db')#, echo = True)
Base = declarative_base()

class Vinho(Base):
    __tablename__ = 'vinhos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    uva = Column(String(50), nullable=False)
    ano = Column(Integer, nullable=False)
    nacionalidade = Column(String(50))
    nota = Column(Float(precision=2))
    harmonizacao = Column(String(200))
    comentario = Column(String(500))

    def __repr__(self):
        return f"<Vinho(nome={self.nome}, Nota={self.nota}, Uva={self.uva}, Pais={self.nacionalidade}, harmoniza com={self.harmonizacao})>"
    
    
# Cria as tabelas no banco de dados
Base.metadata.create_all(engine)

# Cria uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()
#####   QUERYS

# ADD IN TABLE
def add_vinho(nome, nota, uva, ano, harmonizacao, nacionalidade, comentario, id):
    vinho = Vinho(id = id, nome=nome, nota=nota, uva=uva, ano=ano, harmonizacao=harmonizacao, nacionalidade=nacionalidade, comentario=comentario)
    session.add(vinho)
    session.commit()
    session.close()
    print("\nAdição feita com sucesso")


# READ TEABLE

def todos_os_vinho():

    todos_vinhos = session.query(Vinho).all()
    session.close()
    return todos_vinhos  

# REMOVE WINE

def remover_ultimo_vinho():

    ultimo_id_vinho = session.query(Vinho.id).order_by(desc(Vinho.id)).first()

    if ultimo_id_vinho:
        # Apagar o vinho com o último ID
        session.query(Vinho).filter_by(id=ultimo_id_vinho[0]).delete()
        session.commit()
    else:
        print("Não há vinhos para remover.")

#PESQUISAR POR UM VINHO POR NOME
def pesquisar_vinho_por_nome(nome):
    vinhos_pesquisados = session.query(Vinho).filter(Vinho.nome == nome).all()
    print(vinhos_pesquisados)
   #session.close()
    return vinhos_pesquisados

#PESQUISAR POR UM VINHO POR ID
def selecionar_vinho(id):
    id = int(id)
    vinho = session.query(Vinho).filter_by(id=id).first()
    return vinho

#PESQUISAR MELHORES VINHOS
def pesquisar_top10():
    # Calculate the average rating for each wine
    nota_media = session.query(Vinho.nome,func.avg(Vinho.nota).label('nota_media')).group_by(Vinho.nome).all()

    # Sort the wines by average rating in descending order and take the top 5
    top_5_wines = sorted(nota_media, key=lambda x: x[1], reverse=True)[:10]

    return top_5_wines
  

# INSERIR DADOS FICTICIOS (inserir somente 1 vez)
def inserir_dados():
    dados = [
    
    (1, 'Pomerol', 'Merlot', 2011, 'France', 4.5, 'Massas', 'Frutado'),
    (2, 'Lirac', 'Grenache', 2010, 'France', 4.5, 'Peixe', 'Amadeirado'),
    (3, 'Erta e China Rosso di Toscana', 'Sangiovese', 2012, 'Italy', 4.8, 'Queijos, Carnes', 'Frutado'),
    (4, 'Bardolino', 'Corvina', 2013, 'Italy', 4.2, 'Carnes', 'Citrico'),
    (5, 'Ried Scheibner Pinot Noir', 'Pinot Noir', 2014, 'Austria', 4.5, 'Carnes', 'Citrico'),
    (6, 'Gigondas', 'Grenache', 2015, 'France', 4.8, 'Queijos', 'Amadeirado'),
    (7, 'Marions', 'Sauvignon Blanc', 2016, 'New Zealand', 4.2, 'Massas', 'Frutado'),
    (8, 'Vineyard Pinot Noir', 'Pinot Noir', 2017, 'Chile', 4.5, 'Massas', 'Floral'),
    (9, 'Red Blend', 'Merlot, Cabernet Sauvignon', 2018, 'Italy', 4.8, '', 'Floral'),
    (10, 'Chianti', 'Sangiovese', 2019, 'Italy', 2.2, 'Massas', 'Amadeirado'),
    (11, 'Pomerol', 'Merlot', 2020, 'France', 3.5, 'Massas', 'Frutado'),
    (12, 'Lirac', 'Grenache', 2021, 'France', 4.4, 'Peixe', 'Amadeirado'),
    (13, 'Erta e China Rosso di Toscana', 'Sangiovese', 2019, 'Italy', 2.8, 'Queijos, Carnes', 'Frutado'),
    (14, 'Bardolino', 'Corvina', 2017, 'Italy', 3.2, 'Carnes', 'Citrico'),
    (15, 'Ried Scheibner Pinot Noir', 'Pinot Noir', 2015, 'Austria', 2.8, 'Carnes', 'Citrico'),
    (16, 'Gigondas', 'Grenache', 2016, 'France', 2.3, 'Queijos', 'Amadeirado'),
    (17, 'Marions', 'Sauvignon Blanc', 2018, 'New Zealand', 1.9, 'Massas', 'Frutado'),
    (18, 'Vineyard Pinot Noir', 'Pinot Noir', 2020, 'Chile', 3.9, 'Massas', 'Floral'),
    (19, 'Red Blend', 'Merlot, Cabernet Sauvignon', 2021, 'Italy', 3.8, '', 'Floral'),
    (20, 'Chianti', 'Merlot', 'Pinot Noir', 'Italy', 2.8, 'Massas', 'Amadeirado'),
    (21, 'Chateau Margaux', 'Cabernet Sauvignon', 2016, 'France', 3.5, 'Massas', 'Frutado'),
    (22, 'Chateau Latour', 'Merlot', 2017, 'France', 3.5, 'Peixe', 'Amadeirado'),
    (23, 'Sangiovese Supreme', 'Sangiovese', 2019, 'Italy', 4.8, 'Queijos, Carnes', 'Frutado'),
    (24, 'Barolo Brilliance', 'Nebbiolo', 2017, 'Italy', 4.2, 'Carnes', 'Citrico'),
    (25, 'Zinfandel Zing', 'Zinfandel', 2015, 'USA', 4.5, 'Carnes', 'Citrico'),
    (26, 'Malbec Marvel', 'Malbec', 2016, 'Argentina', 1.8, 'Queijos', 'Amadeirado'),
    (27, 'Sauvignon Symphony', 'Sauvignon Blanc', 2018, 'New Zealand', 3.2, 'Massas', 'Frutado'),
    (28, 'Rioja Radiance', 'Tempranillo', 2020, 'Spain', 2.5, 'Massas', 'Floral'),
    (29, 'Gewürztraminer Glory', 'Gewürztraminer', 2021, 'Germany', 3.3, '', 'Floral'),
    (30, 'Riesling Radiance', 'Riesling', 2019, 'Germany', 2.3, 'Massas', 'Amadeirado') 
]
    
    for item in dados:
        vinho = Vinho(
            nome=item[1],
            uva=item[2],
            ano=item[3],
            nacionalidade=item[4],
            nota=item[5],
            harmonizacao=item[6],
            comentario=item[7]
        )
        session.add(vinho)

    session.commit()

