from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional


class ProductCreate(BaseModel):
    name: str
    sku: str
    cost_price: float = Field(..., gt=0)
    selling_price: float = Field(..., gt=0)
    stock_quantity: int = Field(default=0, ge=0)
    reorder_level: int = Field(default=0, ge=0)


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    sku: Optional[str] = None
    cost_price: Optional[float] = None
    selling_price: Optional[float] = None
    stock_quantity: Optional[int] = None
    reorder_level: Optional[int] = None


class ProductResponse(BaseModel):
    id: UUID
    name: str
    sku: str
    cost_price: float
    selling_price: float
    stock_quantity: int
    reorder_level: int

    class Config:
        from_attributes = True