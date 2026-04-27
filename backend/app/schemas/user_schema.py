from pydantic import BaseModel, EmailStr, Field, field_validator
from uuid import UUID
from enum import Enum
import re

class UserRole(str, Enum):
    ADMIN = "admin"
    BUSINESS_OWNER = "business_owner"
    STAFF = "staff"
    ACCOUNTANT = "accountant"

class UserCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="User's full name")
    email: EmailStr
    phone_number: str = Field(..., min_length=10, max_length=15, description="Phone number (e.g., +234 800 000 0000)")
    business_name: str = Field(..., min_length=1, max_length=100, description="Business name")
    password: str = Field(..., min_length=8, description="Password (8+ chars, uppercase, lowercase, number, special char)")
    
    @field_validator('name')
    @classmethod
    def name_not_blank(cls, v):
        if not v or v.isspace():
            raise ValueError('Name cannot be blank or whitespace only')
        return v.strip()
    
    @field_validator('phone_number')
    @classmethod
    def phone_number_format(cls, v):
        if not v or v.isspace():
            raise ValueError('Phone number cannot be blank')
        # Basic phone number validation (allows international format)
        cleaned = re.sub(r'[^\d+]', '', v)
        if not re.match(r'^\+?\d{10,15}$', cleaned):
            raise ValueError('Invalid phone number format')
        return v.strip()
    
    @field_validator('business_name')
    @classmethod
    def business_name_not_blank(cls, v):
        if not v or v.isspace():
            raise ValueError('Business name cannot be blank or whitespace only')
        return v.strip()
    
    @field_validator('password')
    @classmethod
    def password_strength(cls, v):
        if not v or v.isspace():
            raise ValueError('Password cannot be blank or whitespace only')
        
        # Check password requirements
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not re.search(r'[A-Z]', v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not re.search(r'[a-z]', v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not re.search(r'\d', v):
            raise ValueError('Password must contain at least one number')
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', v):
            raise ValueError('Password must contain at least one special character')
        
        return v

class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=1, description="Password")

class UserResponse(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    phone_number: str
    business_name: str
    role: UserRole
    status: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str