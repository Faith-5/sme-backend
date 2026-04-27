from sqlalchemy.orm import Session
from app.db import models
from app.schemas.user_schema import UserCreate, UserLogin, Token, UserRole
from app.core.security import hash_password, verify_password, create_access_token
from fastapi import HTTPException, status

def register_user(db: Session, user_data: UserCreate):
    # 1. Check if email already exists
    existing_user = db.query(models.User).filter(models.User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    # 2. Hash password
    hashed_pwd = hash_password(user_data.password)

    # 3. Create User object
    new_user = models.User(
        name=user_data.name,
        email=user_data.email,
        phone_number=user_data.phone_number,
        business_name=user_data.business_name,
        hashed_password=hashed_pwd,
        role=UserRole.BUSINESS_OWNER
    )

    # 4. Save to DB
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created successfully"}

def login_user(db: Session, user_data: UserLogin):
    # 1. Find user
    user = db.query(models.User).filter(models.User.email == user_data.email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    # 2. Verify password
    if not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    # 3. Create JWT token
    access_token = create_access_token(data={"user_id": str(user.id), "role": user.role})

    # 4. Return token
    return Token(access_token=access_token, token_type="bearer")