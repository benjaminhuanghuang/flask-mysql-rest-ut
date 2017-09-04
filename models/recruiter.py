from sqlalchemy import Column, String, Integer, ForeignKey, Numeric, Date
from sqlalchemy.orm import relationship
from Model import Model

class Recuiter(Model):
    __tablename__ = 'recuiters'
    id = Column(Integer, primary_key = True, nullable=False, autuincrement=True)
    first_name = Column(String(200), nullable=False)
    last_name = Column(String(200), nullable=False)
    phone = Column(String(200), nullable=True)

    interviews = relationship("Interview")
    position = Column(Integer, ForeignKey('positions.id'))

