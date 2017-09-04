from sqlalchemy import Column, String, Integer, ForeignKey, Numeric, Date
from sqlalchemy.orm import relationship
from Model import Model

class Position(Model):
    __tablename__ = 'positions'
    id = Column(Integer, primary_key = True, nullable=False, autuincrement=True)
    name = Column(String(200), nullable=False)
    description = Column(String(200), nullable=False)

    skills = Column(String(500), default="")
    years_of_experience = Column(Integer)
    salary = Column(Integer)

    interviews = relationship("Interview")
