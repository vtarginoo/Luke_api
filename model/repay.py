from sqlalchemy import Column, String, Integer, DateTime, Float
from datetime import datetime

from  model import Base


class Repay(Base):
    __tablename__ = 'repay'

    id = Column("pk_repay", Integer, primary_key=True)
    date_insert = Column(DateTime, default=datetime.now())
    repay = Column(String(140), unique=True)
    category = Column(String(140))
    value = Column(Float)
    # date_repay = Column(DateTime, default=datetime.now())


    def __init__(self, repay:str, category:str, value:float,
                 date_insert:str):
        """
        Cria um repay

        Arguments:
            date_insert: data do reembolso segundo o cliente
            repay: Descrição do Reembolso.
            category: A Categoria que se encaixa o reembolso 
            value: valor da nota
            date_repay: data de quando foi feito o processo de reembolso
        """
        new_date_insert = datetime.strptime(date_insert, "%d/%m/%Y")

        self.date_insert = new_date_insert
        self.repay = repay
        self.category = category
        self.value = value






