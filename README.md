Flask MVP

This is a Flask MVP built using the application factory pattern. The project follows a modular structure and is currently at the early development stage (US-01 and US-02).

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
4. Environment variables

Create a .env file:

FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=dev
DATABASE_URL=sqlite:///instance/app.db
Database Setup (US-02)

Database migrations are already configured using Flask-Migrate (Alembic).

To initialize the database:

flask db upgrade

If needed:

flask db init
flask db migrate -m "initial migration"
flask db upgrade
Run the Application
python run.py

or:

flask run

Then open:

http://127.0.0.1:5000