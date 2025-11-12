from sqlalchemy import Column, Integer, String, Boolean, Float, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Shift(Base):
    __tablename__ = "shifts"
    id = Column(Integer, primary_key=True, index=True)
    clinic_id = Column(Integer, ForeignKey("clinics.id"), nullable=False)
    professional_id = Column(Integer, ForeignKey("professionals.id"), nullable=True)
    date = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    hourly_rate = Column(Float, nullable=False)
    urgent = Column(Boolean, default=False)
    status = Column(String, default="open")  # open, matched, completed, cancelled

    clinic = relationship("Clinic", back_populates="shifts")
