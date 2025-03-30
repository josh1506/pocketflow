# PocketFlow

PocketFlow is a simple Django application designed to help users track their income and expenses. It provides features for adding, editing, deleting, and viewing financial entries, allowing users to monitor their financial health effectively.

## Features
- Add, edit, delete, and view income entries.
- Add, edit, delete, and view expense entries.
- Tailwind CSS integrated for responsive and modern UI.
- Supports PostgreSQL for production-ready deployment.
- Environment-based settings using `.env` files.

## Tech Stack
- **Backend:** Django (Python)
- **Frontend:** Tailwind CSS
- **Database:** SQLite (Development), PostgreSQL (Production)
- **Deployment:** Gunicorn, Nginx

## Installation & Setup

### 1. Clone the Repository
```
git clone <repository-url>
cd pocketflow
```

### 2. Create a Virtual Environment
```
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### 3. Install Dependencies
```
pip install -r requirements.txt
npm install
```

### 4. Create a `.env` File
```
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=sqlite:///db.sqlite3
```

### 5. Run Migrations
```
python manage.py makemigrations
python manage.py migrate
```

### 6. Collect Static Files
```
python manage.py collectstatic
```

### 7. Run Development Server
```
python manage.py runserver
```

### 8. Build Tailwind CSS (Development)
```
npm run dev
```

### 9. Build Tailwind CSS (Production)
```
npm run build
```

## Deployment
- Use `gunicorn` as the WSGI server:
```
gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3
```
- Serve static files using Nginx or another web server.

## Author
Joshua Michael Jabor
