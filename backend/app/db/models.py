from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from .database import Base
from sqlalchemy import func
import uuid

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone_number = Column(String, nullable=False)
    business_name = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="Staff")
    status = Column(String, default="Active")
    created_at = Column(DateTime, server_default=func.now())