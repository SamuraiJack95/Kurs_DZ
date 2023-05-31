from sqlalchemy import Column, ForeignKey, Integer, String
from DZ_41.models.database import Base

class Sales(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    id_prod = Column(Integer, ForeignKey('salesmen.id_pr'))
    id_cus = Column(Integer, ForeignKey('customers.id_cus'))
    adress = Column(String(100), nullable=False)
    summa = Column(Integer, nullable=False)
    count_pr = Column(Integer)
    product = Column(String(50))