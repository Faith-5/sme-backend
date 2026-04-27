from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate, UserLogin, Token, UserResponse, UserRole
from app.api.dependencies.auth import get_current_user, require_role
from app.services import auth_service
from app.db.database import get_db

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Auth"]
)

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return auth_service.register_user(db, user)

@router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    return auth_service.login_user(db, user)

@router.get("/me", response_model=UserResponse)
def get_me(current_user = Depends(get_current_user)):
    return current_user

@router.get("/admin-only")
def admin_only(user = Depends(require_role([UserRole.ADMIN]))):
    return {"message": "Only admin can see this"}

@router.get("/finance")
def finance(user = Depends(require_role([UserRole.ADMIN, UserRole.ACCOUNTANT]))):
    return {"message": "Finance data"}

@router.get("/business-owner")
def business_owner(user = Depends(require_role([UserRole.BUSINESS_OWNER]))):
    return {"message": "You're welcome, Business Owner!"}