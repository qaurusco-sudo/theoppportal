from sqlalchemy import Column, Integer, Boolean, ForeignKey
from app.database import Base

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    shift_id = Column(Integer, ForeignKey("shifts.id"), nullable=False)
    professional_id = Column(Integer, ForeignKey("professionals.id"), nullable=False)
    confirmed = Column(Boolean, default=False)
    completed = Column(Boolean, default=False)
