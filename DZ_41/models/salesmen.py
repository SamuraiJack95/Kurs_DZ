import sys
# sys.path.append('database.py')

from DZ_41.models.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Salesmen(Base):
    __tablename__ = 'salesmen'
    id_pr = Column(Integer, primary_key=True)
    full_name = Column(String(30), nullable=False)
    adress = Column(String(100), nullable=False)
    reyting_pr = Column(Integer)

    custumerss = relationship('Sales')