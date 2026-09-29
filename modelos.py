from sqlalchemy import create_engine, Column, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base


# Cria a conexão do Banco
db = create_engine("sqlite:///banco.db")

# Cria a base do banco de dados
Base = declarative_base()

# Criar as classes/tebelas do banco
# Usuario
class Usuario(Base):
    __tablename__ = "usuarios"

    id = 
# Pedido
# ItensPedido
# Executa a criação dos metadados do seu banco (cria efetivamente o banco de dados)