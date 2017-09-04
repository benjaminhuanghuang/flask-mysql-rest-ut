from sqlalchemy import Column, String, Integer, ForeignKey, Numeric, Date
from sqlalchemy.orm import relationship
from Model import Model

class Candidate(Model):
    __tablename__ = 'candidates'
    id = Column(Integer, primary_key = True, nullable=False, autuincrement=True)
    first_name = Column(String(200), nullable=False)
    last_name = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    birthday = Column(Date, nullable=True)
    phone = Column(String(200), nullable=True)
    languages = Column(String(500), default="")
    skills = Column(String(500), default="")
    interviews = relationship("Interview")
    reviews = relationship("Review")

    def serialize(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "id":self.id
        }