from pydantic import BaseModel
from uuid import UUID


class SaleCreate(BaseModel):
    product_id: UUID
    quantity: int