from sqlalchemy import Column, String, Integer, ForeignKey, Numeric, Date
from sqlalchemy.orm import relationship
from Model import Model

class Client(Model):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key = True, nullable=False, autuincrement=True)
    name = Column(String(200), nullable=False)
    phone = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)

    position = Column(Integer, ForeignKey('positions.id'))
