# API Testing Guide

## Authentication Endpoints

### 1. User Registration
**Endpoint:** `POST /api/register/`

**Request:**
```json
{
  "username": "newuser",
  "first_name": "New",
  "last_name": "User",
  "email": "newuser@example.com",
  "password": "securepass123"
}
```

**Response (201 Created):**
```json
{
  "message": "Registration successful",
  "user": {
    "id": 4,
    "username": "newuser",
    "email": "newuser@example.com",
    "first_name": "New",
    "last_name": "User"
  }
}
```

**cURL Command:**
```bash
curl -X POST http://localhost:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"newuser","first_name":"New","last_name":"User","email":"newuser@example.com","password":"securepass123"}'
```

---

### 2. User Login
**Endpoint:** `POST /api/login/`

**Request:**
```json
{
  "username": "testuser",
  "password": "testpass123"
}
```

**Response (200 OK):**
```json
{
  "message": "Login successful",
  "user": {
    "id": 1,
    "username": "testuser",
    "email": "testuser@example.com",
    "first_name": "Test",
    "last_name": "User"
  }
}
```

**cURL Command:**
```bash
curl -X POST http://localhost:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"testpass123"}' \
  -c cookies.txt
```

---

### 3. User Logout
**Endpoint:** `POST /api/logout/`

**Response (200 OK):**
```json
{
  "message": "Logout successful"
}
```

**cURL Command:**
```bash
curl -X POST http://localhost:8000/api/logout/ \
  -H "Content-Type: application/json" \
  -b cookies.txt
```

---

### 4. Get Current User
**Endpoint:** `GET /api/user/`

**Response (200 OK):**
```json
{
  "authenticated": true,
  "user": {
    "id": 1,
    "username": "testuser",
    "email": "testuser@example.com",
    "first_name": "Test",
    "last_name": "User"
  }
}
```

**cURL Command:**
```bash
curl -X GET http://localhost:8000/api/user/ -b cookies.txt
```

---

## Dealer Endpoints

### 5. Get All Dealers
**Endpoint:** `GET /api/dealers/`

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "name": "Best Motors Inc",
    "address": "123 Main Street",
    "city": "Boston",
    "state": "Massachusetts",
    "zip_code": "02101",
    "phone": "(617) 555-0100",
    "email": "info@bestmotors.com",
    "website": "https://www.bestmotors.com",
    "short_desc": "Your trusted car dealer in Boston",
    "full_desc": "Best Motors Inc has been serving the Boston area for over 20 years...",
    "review_count": 2
  }
]
```

**cURL Command:**
```bash
curl -X GET http://localhost:8000/api/dealers/
```

---

### 6. Get Dealer by ID
**Endpoint:** `GET /api/dealers/{id}/`

**Response (200 OK):**
```json
{
  "id": 1,
  "name": "Best Motors Inc",
  "address": "123 Main Street",
  "city": "Boston",
  "state": "Massachusetts",
  "zip_code": "02101",
  "phone": "(617) 555-0100",
  "email": "info@bestmotors.com",
  "website": "https://www.bestmotors.com",
  "short_desc": "Your trusted car dealer in Boston",
  "full_desc": "Best Motors Inc has been serving the Boston area for over 20 years...",
  "review_count": 2
}
```

**cURL Command:**
```bash
curl -X GET http://localhost:8000/api/dealers/1/
```

---

### 7. Get Dealers by State
**Endpoint:** `GET /api/dealers/state/{state}/`

**Example:** Get dealers in Kansas

**Response (200 OK):**
```json
[
  {
    "id": 2,
    "name": "Elite Auto Sales",
    "city": "Kansas City",
    "state": "Kansas",
    "review_count": 1
  },
  {
    "id": 3,
    "name": "Quality Cars",
    "city": "Wichita",
    "state": "Kansas",
    "review_count": 0
  }
]
```

**cURL Command:**
```bash
curl -X GET http://localhost:8000/api/dealers/state/Kansas/
```

---

## Review Endpoints

### 8. Get Dealer Reviews
**Endpoint:** `GET /api/reviews/dealer/{dealer_id}/`

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "dealer": 1,
    "dealer_name": "Best Motors Inc",
    "customer": 1,
    "customer_name": "testuser",
    "purchase": true,
    "purchase_date": "2024-01-15",
    "car_make": "Toyota",
    "car_model": "Camry",
    "car_year": 2023,
    "review_text": "Fantastic services and great customer support!",
    "sentiment": "positive",
    "created_at": "2024-01-16T10:30:00Z",
    "updated_at": "2024-01-16T10:30:00Z"
  }
]
```

**cURL Command:**
```bash
curl -X GET http://localhost:8000/api/reviews/dealer/1/
```

---

### 9. Post a Review
**Endpoint:** `POST /api/reviews/`

**Request:**
```json
{
  "dealer": 1,
  "purchase": true,
  "purchase_date": "2024-01-18",
  "car_make": "Honda",
  "car_model": "Civic",
  "car_year": 2023,
  "review_text": "Excellent service and great deals!"
}
```

**Response (201 Created):**
```json
{
  "message": "Review posted successfully",
  "review": {
    "id": 2,
    "dealer": 1,
    "dealer_name": "Best Motors Inc",
    "customer": 1,
    "customer_name": "testuser",
    "purchase": true,
    "purchase_date": "2024-01-18",
    "car_make": "Honda",
    "car_model": "Civic",
    "car_year": 2023,
    "review_text": "Excellent service and great deals!",
    "sentiment": "positive",
    "created_at": "2024-01-18T15:30:00Z",
    "updated_at": "2024-01-18T15:30:00Z"
  }
}
```

**cURL Command:**
```bash
curl -X POST http://localhost:8000/api/reviews/ \
  -H "Content-Type: application/json" \
  -b cookies.txt \
  -d '{"dealer":1,"purchase":true,"purchase_date":"2024-01-18","car_make":"Honda","car_model":"Civic","car_year":2023,"review_text":"Excellent service and great deals!"}'
```

---

## Car Endpoints

### 10. Get All Car Makes
**Endpoint:** `GET /api/cars/makes/`

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "name": "Toyota",
    "description": "Japanese automobile manufacturer"
  },
  {
    "id": 2,
    "name": "Honda",
    "description": "Japanese automobile manufacturer"
  },
  {
    "id": 3,
    "name": "Ford",
    "description": "American automobile manufacturer"
  }
]
```

**cURL Command:**
```bash
curl -X GET http://localhost:8000/api/cars/makes/
```

---

### 11. Get All Car Models
**Endpoint:** `GET /api/cars/models/`

**Optional Query Parameter:** `?make=1` (filter by make ID)

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "make": 1,
    "make_name": "Toyota",
    "name": "Camry",
    "car_type": "Sedan",
    "year": 2023
  },
  {
    "id": 2,
    "make": 1,
    "make_name": "Toyota",
    "name": "RAV4",
    "car_type": "SUV",
    "year": 2023
  }
]
```

**cURL Commands:**
```bash
# Get all models
curl -X GET http://localhost:8000/api/cars/models/

# Get models for specific make
curl -X GET http://localhost:8000/api/cars/models/?make=1
```

---

## Sentiment Analysis Endpoint

### 12. Analyze Review Sentiment
**Endpoint:** `POST /api/analyze/`

**Request:**
```json
{
  "text": "Fantastic services"
}
```

**Response (200 OK):**
```json
{
  "text": "Fantastic services",
  "sentiment": "positive"
}
```

**Examples:**

**Positive:**
```bash
curl -X POST http://localhost:8000/api/analyze/ \
  -H "Content-Type: application/json" \
  -d '{"text":"Fantastic services"}'
```

**Negative:**
```bash
curl -X POST http://localhost:8000/api/analyze/ \
  -H "Content-Type: application/json" \
  -d '{"text":"Terrible experience, very disappointing"}'
```

**Neutral:**
```bash
curl -X POST http://localhost:8000/api/analyze/ \
  -H "Content-Type: application/json" \
  -d '{"text":"The dealership is located downtown"}'
```

---

## Error Responses

### 400 Bad Request
```json
{
  "error": "Invalid input data",
  "details": {
    "field_name": ["Error message"]
  }
}
```

### 401 Unauthorized
```json
{
  "error": "Invalid credentials"
}
```

### 404 Not Found
```json
{
  "error": "Resource not found"
}
```

### 500 Internal Server Error
```json
{
  "error": "Internal server error"
}
```

---

## Testing Workflow

### Complete Test Sequence:

1. **Register a new user**
2. **Login with credentials**
3. **Get all dealers**
4. **Filter dealers by state**
5. **Get specific dealer details**
6. **View dealer reviews**
7. **Post a new review**
8. **Get car makes and models**
9. **Test sentiment analysis**
10. **Logout**

### Sample Test Script:

```bash
#!/bin/bash

echo "1. Registering new user..."
curl -X POST http://localhost:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser2","first_name":"Test","last_name":"User2","email":"testuser2@example.com","password":"testpass123"}'

echo "\n2. Logging in..."
curl -X POST http://localhost:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"testpass123"}' \
  -c cookies.txt

echo "\n3. Getting all dealers..."
curl -X GET http://localhost:8000/api/dealers/

echo "\n4. Getting dealers in Kansas..."
curl -X GET http://localhost:8000/api/dealers/state/Kansas/

echo "\n5. Getting dealer reviews..."
curl -X GET http://localhost:8000/api/reviews/dealer/1/

echo "\n6. Analyzing sentiment..."
curl -X POST http://localhost:8000/api/analyze/ \
  -H "Content-Type: application/json" \
  -d '{"text":"Fantastic services"}'

echo "\n7. Logging out..."
curl -X POST http://localhost:8000/api/logout/ \
  -H "Content-Type: application/json" \
  -b cookies.txt

rm cookies.txt
echo "\nTest sequence completed!"
```

---

## Notes

- All POST requests require `Content-Type: application/json` header
- Authentication uses session-based authentication
- Review posting requires authentication
- Sentiment is automatically analyzed when posting reviews
- CORS is configured to allow frontend requests from localhost:3000
