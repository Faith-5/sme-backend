from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.inventory import schema, service
from app.api.dependencies.auth import get_current_user, require_role
from app.schemas import UserRole

router = APIRouter(
    prefix="api/v1/inventory",
    tags=["Inventory"]
)

@router.post("/products")
def create_product(
    product: schema.ProductCreate,
    db: Session = Depends(get_db),
    current_user = Depends(require_role([UserRole.ADMIN, UserRole.BUSINESS_OWNER]))
):
    return service.create_product(db, product)

@router.get("/products")
def get_products(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return service.get_products(db)

@router.get("/products/{product_id}")
def get_product(
    product_id: str,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return service.get_product(db, product_id)

@router.put("/products/{product_id}")
def update_product(
    product_id: str,
    product: schema.ProductUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(require_role([UserRole.ADMIN, UserRole.BUSINESS_OWNER]))
):
    return service.update_product(db, product_id, product)

@router.delete("/products/{product_id}")
def delete_product(
    product_id: str,
    db: Session = Depends(get_db),
    current_user = Depends(require_role([UserRole.ADMIN, UserRole.BUSINESS_OWNER]))
):
    return service.delete_product(db, product_id)