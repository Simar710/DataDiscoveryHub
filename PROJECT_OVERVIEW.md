# Data Discovery Hub – Project Documentation

## Project Overview
The **Data Discovery Hub** is a Django-based web application designed to provide an organized platform for managing and discovering datasets. The application leverages a robust tech stack to ensure a consistent and secure experience across development, production, and CI/CD environments.

## Tech Stack and How Each is Used

### 1. Backend
- **Django (Python)**
  - **Usage**: Serves as the core web framework for routing, business logic, and database interactions via the ORM.
  - **Development vs. Production**:
    - **Development**: Uses Django’s built-in development server (`runserver`) with `DEBUG=True`.
    - **Production**: Configured with `DEBUG=False` and served using Gunicorn—a production-ready WSGI server.
- **Django REST Framework (DRF)**
  - **Usage**: Provides a framework to build RESTful APIs, enabling external services or frontend applications to interact with the system.

### 2. Database
- **PostgreSQL**
  - **Usage**: Acts as the primary relational database for storing dataset information.
  - **Containerized Setup**:
    - Runs in a Docker container for both local development and CI/CD.
    - **Configuration**: 
      - In Docker Compose for local development, the database host is set to the service name (e.g., `db`).
      - In CI/CD, environment variables are used to configure the host (typically `localhost` when services are exposed).

### 3. Frontend
- **HTML, CSS, JavaScript**
  - **Usage**: Implements the presentation layer of the application.
  - **Static Files**: Managed by Django’s staticfiles system to serve CSS, JavaScript, and images.
- **Gunicorn**
  - **Usage**: Serves as the production WSGI server for the Django application.
  - **Development vs. Production**:
    - **Development**: Typically, Django’s `runserver` is used.
    - **Production**: Gunicorn handles concurrent requests efficiently and is used with a reverse proxy (e.g., Nginx or WhiteNoise for static files).

### 4. Containerization and Deployment
- **Docker & Docker Compose**
  - **Usage**: Containerizes both the Django application and PostgreSQL database to ensure consistency across environments.
  - **Local Development**: Uses `docker-compose up --build` to start the application and database in isolated containers.
  - **CI/CD**: GitHub Actions uses Docker Compose to spin up the containers, run migrations, and execute tests in an isolated environment.

### 5. Error Tracking
- **Sentry**
  - **Usage**: Integrated with Django to capture, log, and report errors in real time.
  - **Configuration**: Initialized in `settings.py` using environment variables (such as a DSN) to facilitate debugging during development and monitoring in production.

### 6. Continuous Integration & Deployment (CI/CD)
- **GitHub Actions**
  - **Usage**: Automates testing and deployment processes.
  - **Pipeline Functions**:
    - Checks out code.
    - Sets up the Python environment.
    - Installs dependencies.
    - Runs migrations and tests.
  - **Secrets Management**: Sensitive information (database credentials, Sentry DSN, etc.) is stored as GitHub Secrets and injected into the workflow.

### 7. Environment Variables & Secrets Management
- **Local Development**
  - **.env File**: Used to store sensitive credentials (e.g., database settings, secret keys). This file is excluded from version control.
- **CI/CD**
  - **GitHub Secrets**: Securely store credentials (e.g., `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, etc.) and access them in the GitHub Actions workflow using the `${{ secrets.SECRET_NAME }}` syntax.

## Development vs. Production

### Development Environment
- **Server**: Uses Django’s built-in development server (`runserver`), which is ideal for debugging and iterative development.
- **Static Files**: Served directly from the `static/` directory configured via `STATICFILES_DIRS`.
- **Debugging**: Enabled by setting `DEBUG=True`, allowing detailed error messages and logging.
- **Database Host**: Configured via environment variables; in Docker Compose, this might be set to `db` (or `localhost` when not containerized).

### Production Environment
- **Server**: Uses Gunicorn as the WSGI server for a production-ready setup.
- **Static Files**: Collected into a single directory (`STATIC_ROOT`) using `python manage.py collectstatic` and served by a dedicated static file server (e.g., Nginx or WhiteNoise).
- **Debugging**: Disabled (`DEBUG=False`) for enhanced security and performance.
- **Error Tracking**: Sentry is enabled for real-time error monitoring.
- **Database Host**: Configured via environment variables to ensure that the application connects to the appropriate database host (e.g., `db` in Docker or `localhost` in CI/CD).

## Project Highlights
- **Full-stack Django Application** with RESTful API capabilities.
- **Containerized Deployment** using Docker and Docker Compose for consistent environments across local, production, and CI/CD setups.
- **PostgreSQL Database** running in its own container.
- **Production-Ready Server**: Gunicorn serves the Django application for high performance.
- **Real-time Error Tracking** with Sentry for proactive monitoring.
- **Automated CI/CD Pipeline** with GitHub Actions to streamline testing and deployment.
- **Secure Secrets Management**: Sensitive information is handled via `.env` files locally and GitHub Secrets in CI/CD.

## Final Notes
This documentation outlines the architecture and tech stack used in the **Data Discovery Hub** project. The configuration is designed to ensure that the same codebase and settings work seamlessly across local development, production, and CI/CD environments. The focus is on consistency, security, and scalability.
