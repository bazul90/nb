# Flask MVP

A minimal Flask web application built using the application factory pattern.
This project demonstrates a scalable backend structure, database migrations, and environment-based configuration for rapid development.

---

## 📌 Features

* Application factory pattern
* Modular project structure
* SQLite database integration
* Database migrations using Flask-Migrate (Alembic)
* Environment variable configuration

---

## 📁 Project Structure

```bash
app/
│── domain/              # Business logic (models, services, etc.)
│── __init__.py          # Application factory
│── config.py            # Configuration settings
│── extensions.py        # Flask extensions initialization

instance/
│── app.db               # SQLite database

migrations/
│── versions/            # Migration files
│── env.py
│── alembic.ini
│── script.py.mako

run.py                   # Application entry point
requirements.txt         # Project dependencies
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone git@github.com:bazul90/nb.git
cd nb
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

```bash
# Linux / Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory and add:

```env
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=dev
DATABASE_URL=sqlite:///instance/app.db
```

**Explanation:**

* `FLASK_APP` – Entry point of the application
* `FLASK_ENV` – Enables development mode
* `SECRET_KEY` – Used for session security
* `DATABASE_URL` – Database connection string

---

## 🗄️ Database Setup

This project uses Flask-Migrate for handling database migrations.

```bash
flask db migrate   # Generate migration files
flask db upgrade   # Apply migrations to the database
```

---

## ▶️ Running the Application

```bash
flask run
```

Or alternatively:

```bash
python run.py
```

The app will be available at:
http://127.0.0.1:5000/

---

## 🚧 Project Status

This project is currently in development.
Core structure and database setup are complete, with additional features planned.

---

## 🔮 Future Improvements

* Add authentication (login/register)
* Build RESTful API endpoints
* Improve error handling and logging
* Add unit and integration tests

---


