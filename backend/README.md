# SME Business Management API

A FastAPI backend for managing Small/Medium Enterprise operations with user authentication.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment:**
   Create a `.env` file with required variables (database URL, JWT secret, etc.)

3. **Run the server:**
   ```bash
   python -m uvicorn app.main:app --reload
   ```
   API runs at: `http://localhost:8000`

## Available Endpoints

### Authentication (`/api/v1/auth`)

**Register a new user:**
```bash
POST /api/v1/auth/register
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "phone_number": "+2348000000000",
  "business_name": "My Business Ltd",
  "password": "Hello?,123"
}
```

**Login:**
```bash
POST /api/v1/auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "securepassword"
}
```
Returns: JWT token for authenticated requests

### Health Check

```bash
GET /
```
Returns: `{"message": "SME API is running successfully!"}`

## API Documentation

- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

## Database

Uses SQLAlchemy with PostgreSQL. Tables are auto-created on startup from models in `app/db/models.py`.

## Notes

- Password hashing: Argon2
- JWT tokens for secure authentication
- CORS enabled for frontend communication
