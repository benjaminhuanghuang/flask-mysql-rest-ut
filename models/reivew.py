from sqlalchemy import Column, String, Integer, ForeignKey, Numeric, Date
from sqlalchemy.orm import relationship
from Model import Model

class Review(Model):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key = True, nullable=False, autuincrement=True)
    reivew_date = Column(Date)
    content = Column(String(500), default="")

    reviewer = relationship("Interview")
    candidate = relationship("Candidate")

    def serialize(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "id":self.id
        }