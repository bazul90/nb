Flask MVP

This project is a Flask application built using the application factory pattern. It is currently at the initial scaffold stage, with core configuration and database setup completed.

Project Structure
app/
├── domain/
│   ├── __init__.py
│   ├── config.py
│   ├── extensions.py

instance/
├── app.db

migrations/
│   ├── versions/
│   ├── env.py
│   ├── alembic.ini
│   ├── script.py.mako

run.py
.gitignore
venv/
Setup Instructions
1. Clone the repository
git clone git@github.com:bazul90/nb.git
cd nb
2. Create virtual environment
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Environment setup

Create a .env file in the root directory:

FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=dev
DATABASE_URL=sqlite:///instance/app.db
Database Setup (US-02)

The project uses Flask-Migrate for database version control.

To initialize or update the database:

flask db upgrade

If setting up from scratch:

flask db init
flask db migrate -m "initial migration"
flask db upgrade
Running the Application
python run.py

or:

flask run

Then open:

http://127.0.0.1:5000

Current Status
US-01: Completed
Application factory structure implemented
Modular project layout created
Configuration and extensions set up
US-02: Completed / Configured
Flask-Migrate integrated
Database initialized with Alembic
SQLite database configured in instance/
Notes
Flask application follows factory pattern
SQLAlchemy setup handled via extensions
Database migrations managed with Flask-Migrate
Project structure prepared for scalable development
Summary

The project is in its initial scaffold stage with core infrastructure in place. Future work will focus on adding models, routes, and business logic layers.