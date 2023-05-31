from DZ_41.models.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

association_tablec = Table('association_sc', Base.metadata,
                    Column('id_cus', Integer, ForeignKey('customers.id_cus')),
                    Column('id_pr', Integer, ForeignKey('salesmen.id_pr')))
class Customers(Base):
    __tablename__ = 'customers'
    id_cus = Column(Integer, primary_key=True)
    full_name = Column(String(30), nullable=False)
    adress = Column(String(100), nullable=False)
    reyting_kl = Column(Integer)

    salesmens = relationship('Salesmen', secondary='association_sc', backref='customers')
    saless = relationship('Sales')