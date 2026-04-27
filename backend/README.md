# SME Business Management API

A FastAPI backend for managing Small/Medium Enterprise operations with authentication and role-based access control (RBAC).

---

## 🚀 Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
````

### 2. Configure environment

Create a `.env` file in the root directory and add required variables:

```env
DATABASE_URL=your_database_url
SECRET_KEY=your_jwt_secret
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

### 3. Run the server

```bash
python -m uvicorn app.main:app --reload
```

Server runs at:

```
http://localhost:8000
```

---

## 🔐 Authentication Flow

1. Register a user
2. Login to receive JWT token
3. Use token in protected requests:

```http
Authorization: Bearer <token>
```

---

## 👤 User Roles (RBAC)

The system supports the following roles:

* `admin` → full system access
* `business_owner` → business-wide access
* `staff` → limited operational access
* `accountant` → financial module access

---

## 📡 API Endpoints

---

## 🔑 Authentication (`/api/v1/auth`)

### Register User

```http
POST /api/v1/auth/register
```

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone_number": "+2348000000000",
  "business_name": "My Business Ltd",
  "password": "Hello?,123"
}
```

---

### Login

```http
POST /api/v1/auth/login
```

```json
{
  "email": "user@example.com",
  "password": "securepassword"
}
```

Response:

```json
{
  "access_token": "JWT_TOKEN",
  "token_type": "bearer"
}
```

---

### Get Current User

```http
GET /api/v1/auth/me
```

Headers:

```http
Authorization: Bearer <token>
```

Response:

```json
{
  "id": "uuid",
  "name": "John Doe",
  "email": "john@example.com",
  "phone_number": "+2348000000000",
  "business_name": "My Business Ltd",
  "role": "business_owner",
  "status": "Active"
}
```

---

## 🛡️ RBAC (Role-Based Access Control)

Access is restricted based on user roles.

### Rules:

* `/admin/*` → admin only
* `/finance/*` → admin, accountant
* `/business/*` → admin, business_owner
* `/staff/*` → admin, business_owner, staff

---

### Unauthorized Response

```json
{
  "detail": "Insufficient permissions"
}
```

---

## 🧪 API Testing

* Swagger UI:

```
http://localhost:8000/docs
```

* ReDoc:

```
http://localhost:8000/redoc
```

---

## 🗄️ Database

* SQLAlchemy ORM
* PostgreSQL
* Auto table creation from `app/db/models.py`

---

## 🔐 Security

* Password hashing: Argon2
* JWT authentication
* Role-based access control (RBAC)
* Stateless authentication (no sessions)

---

## ⚡ Frontend Notes

Frontend should:

* Store JWT token after login
* Fetch `/me` to get user role
* Control UI based on role
* Handle `403 Forbidden` responses

---

```
```
