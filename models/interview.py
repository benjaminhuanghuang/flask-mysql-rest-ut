from sqlalchemy import Column, String, Integer, ForeignKey, Numeric, Date
from sqlalchemy.orm import relationship
from Model import Model

class Interview(Model):
    __tablename__ = 'interviews'
    id = Column(Integer, primary_key = True, nullable=False, autuincrement=True)
    date = Column(Date)
    feedback = Column(String(200), nullable=False)

    position = Column(Integer, ForeignKey('positions.id'))

    recruiter_id = Column(Integer, ForeignKey('recruiters.id'))
    recruiter = relationship("Recruiter")

    candidate = Column(Integer, ForeignKey('candidates.id'))
