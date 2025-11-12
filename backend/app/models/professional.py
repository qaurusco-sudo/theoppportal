from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Professional(Base):
    __tablename__ = "professionals"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)  # link to users.id (light for now)
    role_type = Column(String, nullable=False)  # RDH, CDA, etc.
    hourly_rate = Column(Float)
    experience = Column(String)
