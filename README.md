#  🚀 Data Discovery Hub


A Django-based **data discovery platform** with **PostgreSQL, Docker, and Sentry for error tracking**.

---

## 🚀 Features
- Django Backend
- Create, list, and manage datasets
- PostgreSQL database integration
- Django Admin for managing datasets
- Django REST Framework
- Basic authentication (Superuser login)
- Sentry for Error Tracking
- Admin Panel for Dataset Management

---

## 📌 1️⃣ Installation & Setup

## **🔹 Local Development (Without Docker)**
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

### 5️⃣ Set Up Environment Variables
Create a `.env` file in the project root and add:

```bash
SENTRY_DSN=your_sentry_dsn_here
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

- **Note:** Don't forget to uncomment the following snippent in settings.py:
```bash
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "data_hub_discovery",
        "USER": "simardeepsingh",
        "PASSWORD": "Canada123",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

- Now, open `http://127.0.0.1:8000` 🚀

## **🔹 Using Docker**

### 1️⃣ Build & Start Docker Containers
```bash
docker-compose up --build
```

### 2️⃣ Run Migrations Inside the `web` Container
```bash
docker-compose exec web python manage.py migrate
```
**Note:** If the above step doesn't work, use docker desktop to open the web container terminal and run `python manage.py migrate`

### 3️⃣ Create a Superuser (For Admin Access)
```bash
docker-compose exec web python manage.py createsuperuser
```

- Now, open `http://127.0.0.1:8000` 🚀

- **Note:** Don't forget to uncomment the following snippent in settings.py:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'data_hub_discovery'),
        'USER': os.getenv('POSTGRES_USER', 'simardeepsingh'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'Canada123'),
        'HOST': 'db',  # Change 'localhost' to 'db' (the Docker service name)
        'PORT': '5432',
    }
}
```

## 📌 2️⃣ URLs & What They Do

| URL            | Purpose                                                       |
|----------------|---------------------------------------------------------------|
| **/admin/**     | Django Admin Panel (Login required)                          |
| **/datasets/**  | List all datasets                                            |
| **/sentry-test/** | Manually trigger an error for Sentry                       |
| **/api/datasets/** | (If DRF is enabled) API to fetch datasets                  |

## 📌 3️⃣ Error Tracking with Sentry

### ✅ How to Test Sentry Integration:

1. Run your Django project.
2. Visit http://127.0.0.1:8000/sentry-test/
3. Go to your Sentry dashboard → Check if the error appears.

## 📌 4️⃣ Deployment (Production)
To deploy this Django app:
- Use Gunicorn & Nginx
- Store Sentry DSN in environment variables
- Deploy on AWS
- Configure CI/CD with GitHub Actions.

## 5️⃣ Common Commands

| Task                | Command                                                        |
|---------------------|----------------------------------------------------------------|
| Run Migrations      | `docker-compose exec web python manage.py migrate`             |
| Create Superuser    | `docker-compose exec web python manage.py createsuperuser`     |
| Check Logs          | `docker-compose logs web`                                     |
| Restart Containers  | `docker-compose restart`                                      |
| Stop Containers     | `docker-compose down`                                          |

## 📌 6️⃣ Troubleshooting
- 🚨 Error: "relation 'datahub_dataset' does not exist"
  - ✅ Fix: Run migrations inside the Docker container:
```bash
docker-compose exec web python manage.py migrate
```

- 🚨 Error: "connection refused to PostgreSQL"
  - ✅ Fix: Ensure your settings.py has:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'db',  # NOT localhost!
        'PORT': '5432',
    }
}
```

### 📌 7️⃣ Running Tests locally
```bash
python manage.py test
```