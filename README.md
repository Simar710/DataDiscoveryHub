# Data Discovery Hub

A simple Django-based data discovery web application.

## 🚀 Features
- Create, list, and manage datasets
- PostgreSQL database integration
- Django Admin for managing datasets
- API endpoints (if extended with Django REST Framework)
- Basic authentication (Superuser login)

---

## 🛠 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Simar710/data_discovery_hub.git
cd data_discovery_hub
```

### 2️⃣ Create a Virtual Environment & Install Dependencies
```bash
python -m venv env
source env/bin/activate  # macOS/Linux
env\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 3️⃣ Set Up the Database (PostgreSQL)
- Install PostgreSQL
- Create a database:
```sql
CREATE DATABASE secoda_db;
CREATE USER your_db_user WITH PASSWORD 'your_db_password';
GRANT ALL PRIVILEGES ON DATABASE secoda_db TO your_db_user;
```

### 4️⃣ Configure Django Settings
Update `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'secoda_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5️⃣ Run Migrations & Create Superuser
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 6️⃣ Start the Development Server

```bash
python manage.py runserver
```

### 7️⃣ URLs
- Go to `http://127.0.0.1:8000/` to see the dataset list.
- Click “Add New Dataset” to add a record.
- Visit `http://127.0.0.1:8000/admin/` and log in with your superuser credentials to manage datasets through the Django admin interface.

### 🧪 Running Tests
```bash
python manage.py test
```

### 📌 Deployment
- Configure CI/CD with GitHub Actions.
- Deploy to AWS.