# Flask MVP

A minimal Flask web application built using the application factory pattern.  
This project demonstrates a scalable backend structure, database migrations, and environment-based configuration for rapid development.

---

## 📌 Features

- Application factory pattern
- Modular project structure
- SQLite database integration
- Database migrations using Flask-Migrate (Alembic)
- Environment variable configuration
- User authentication system (Register & Login)
- Password hashing for security
- Input validation and error handling

---

## 📁 Project Structure

app/  
├── domain/              (Models / business logic)  
├── views/               (Routes / API endpoints)  
├── __init__.py          (Application factory)  
├── config.py            (Configuration settings)  
└── extensions.py        (Flask extensions initialization)  

instance/  
└── app.db               (SQLite database)  

migrations/  
├── versions/  
├── env.py  
├── alembic.ini  
└── script.py.mako  

run.py                   (Application entry point)  
requirements.txt         (Project dependencies)  

---

## ⚙️ Setup Instructions

### Clone repository
git clone git@github.com:bazul90/nb.git  
cd nb  

---

### Create virtual environment
python -m venv venv  

---

### Activate virtual environment

Linux / Mac:
source venv/bin/activate  

Windows:
venv\Scripts\activate  

---

### Install dependencies
pip install -r requirements.txt  

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

FLASK_APP=run.py  
FLASK_ENV=development  
SECRET_KEY=dev  
DATABASE_URL=sqlite:///instance/app.db  

---

## 🗄️ Database Setup

flask db migrate  
flask db upgrade  

---

## ▶️ Run Application

flask run  

OR  

python run.py  

Application runs at:
http://127.0.0.1:5000/

---

## 🔐 Authentication System

### Register User

POST /auth/register  

Request:
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "123456"
}

Rules:
- Username required
- Email required
- Password required
- Password must be at least 6 characters
- Username must be unique
- Email must be unique

Response:
{
  "status": "success",
  "message": "User registered successfully",
  "data": {
    "id": 1,
    "username": "testuser",
    "email": "test@example.com"
  }
}

---

### Login User

POST /auth/login  

Request:
{
  "email": "test@example.com",
  "password": "123456"
}

Response:
{
  "status": "success",
  "message": "Login successful",
  "data": {
    "id": 1,
    "username": "testuser",
    "email": "test@example.com"
  }
}

---

## 🔒 Security Features

- Passwords are hashed before storing in database
- Input validation for all endpoints
- Duplicate email and username prevention
- Secure login verification

---

## 🚧 Project Status

Backend structure complete.  
Authentication system implemented and tested using Postman.

---

## 🔮 Future Improvements

- JWT authentication
- Role-based access control
- Unit testing
- API documentation (Swagger)

