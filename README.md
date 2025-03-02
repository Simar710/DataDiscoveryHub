#  🚀 Data Discovery Hub

Please check **PROJECT_OVERVIEW.md** for details on the architecture and tech stack used in the Data Discovery Hub project.

A Django-based **data discovery platform** with **PostgreSQL, Docker, and Sentry for error tracking**.

---

## 🚀 Features
- **Django Backend** for creating, listing, and managing datasets.
- **PostgreSQL Integration** via Django ORM.
- **Django Admin** for dataset management and basic authentication (superuser login).
- **Django REST Framework** endpoints.
- **Sentry** for Error Tracking
- **Containerization** using Docker & Docker Compose.

---


## 📌 1️⃣ Installation & Setup

## **🔹 Local Development (Without Docker)**
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Simar710/DataDiscoveryHub.git
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
CREATE DATABASE data_hub_discovery;
CREATE USER your_db_user WITH PASSWORD 'your_db_password';
GRANT ALL PRIVILEGES ON DATABASE secoda_db TO your_db_user;
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file in the project root and add:

```bash
DB_NAME=data_hub_discovery
DB_USER=simardeepsingh
DB_PASSWORD=your-secure-password
DB_HOST=localhost
DB_PORT=5432
SENTRY_DSN=your-sentry-dsn
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
- Now, open `http://127.0.0.1:8000` 🚀


## **🔹 Using Docker**

### 1️⃣ Build & Start Docker Containers
```bash
docker-compose up --build
```


### 2️⃣ Create a Superuser (For Admin Access)
```bash
docker-compose exec web python manage.py createsuperuser
```
**Note:** If this command does not work from the CLI, open the web container’s terminal using Docker Desktop and run:

```bash
python manage.py createsuperuser
```

- Now, open `http://127.0.0.1:8000` 🚀


---

## 📌 2️⃣ URLs & What They Do

| URL            | Purpose                                                       |
|----------------|---------------------------------------------------------------|
| **/**  | List all datasets                                           |
| **/add/**  |Add new datasets                                           |
| **/admin/**     | Django Admin Panel (Login required)                          |
| **/sentry-test/** | Manually trigger an error for Sentry                       |
| **/api/datasets/** | (If DRF is enabled) API to fetch datasets                  |


---
## 📌 3️⃣ Error Tracking with Sentry

### ✅ How to Test Sentry Integration:

1. Run your Django project.
2. Visit http://127.0.0.1:8000/sentry-test/ to trigger a test error.
3. Check your Sentry dashboard to confirm that the error was reported.


---
## 4️⃣ Common Commands

| Task                | Command                                                        |
|---------------------|----------------------------------------------------------------|
| Run Migrations      | `docker-compose exec web python manage.py migrate`             |
| Create Superuser    | `docker-compose exec web python manage.py createsuperuser`     |
| Check Logs          | `docker-compose logs web`                                     |
| Restart Containers  | `docker-compose restart`                                      |
| Stop Containers     | `docker-compose down`                                          |


---
## 📌 5️⃣ Troubleshooting
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


---
### 📌 7️⃣ Running Tests locally
```bash
python manage.py test
```
