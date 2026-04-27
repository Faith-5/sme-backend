from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.db.database import Base
import uuid


class Sale(Base):
    __tablename__ = "sales"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    product_id = Column(UUID(as_uuid=True), ForeignKey("products.id"))
    
    quantity = Column(Integer, nullable=False)
    selling_price = Column(Float, nullable=False)
    cost_price = Column(Float, nullable=False)

    total_amount = Column(Float, nullable=False)

    created_at = Column(DateTime, server_default=func.now())