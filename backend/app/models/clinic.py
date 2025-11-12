from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.database import Base

class Clinic(Base):
    __tablename__ = "clinics"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)  # link to users.id (light for now)
    name = Column(String, nullable=False)
    address = Column(String)
    geo_lat = Column(Float)
    geo_long = Column(Float)

    shifts = relationship("Shift", back_populates="clinic")
