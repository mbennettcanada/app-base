from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text


class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,nullable=False)
    email = Column(String,nullable=False)
    username = Column(String,nullable=False)
    full_name = Column(String,nullable=True)
    disabled = Column(Boolean,nullable=False,default=False)
    hashed_password = Column(String, nullable = True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))