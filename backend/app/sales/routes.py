from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.sales import schema, service
from app.api.dependencies.auth import get_current_user, require_role
from app.schemas.user_schema import UserRole

router = APIRouter(
    prefix="/api/v1/sales",
    tags=["Sales"]
)


@router.post("/")
def create_sale(
    sale: schema.SaleCreate,
    db: Session = Depends(get_db),
    user = Depends(require_role([UserRole.ADMIN, UserRole.BUSINESS_OWNER, UserRole.STAFF]))
):
    return service.create_sale(db, sale)


@router.get("/")
def get_sales(
    db: Session = Depends(get_db),
    user = Depends(require_role([UserRole.ADMIN, UserRole.ACCOUNTANT, UserRole.BUSINESS_OWNER]))
):
    return service.get_sales(db)