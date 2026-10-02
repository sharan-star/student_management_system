# Student Management System

A Django-based student management application for registering users, managing student records, storing resumes, browsing courses, and viewing job drives.

## Features

- User registration and login
- Student record creation, search, update, and deletion
- Resume uploads for student records
- Course listing with course images and technical details
- Job drive listing
- Django admin interface
- MySQL database support
- Static file serving with WhiteNoise

## Technology Stack

- Python 3.10+
- Django 4.2
- MySQL
- `django-environ` for environment configuration
- WhiteNoise for static files
- Pillow for image uploads

## Project Structure

```text
student_management_system/
|-- dashboard/                    # Application code, models, views, and URLs
|-- student_management_system/    # Django project configuration
|-- templates/                    # HTML templates
|-- static/                       # Source CSS, JavaScript, and static assets
|-- media/                        # Uploaded resumes and images
|-- manage.py
|-- requirements.txt
|-- .env.example
|-- LICENSE
`-- README.md
```

## Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd student_management_system
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy `.env.example` to `.env` and provide values for the application and MySQL database:

```env
DEBUG=True
SECRET_KEY=replace-with-a-development-secret-key
DATABASE_NAME=
DATABASE_USER=your-mysql-user
DATABASE_PASSWORD=your-mysql-password
DATABASE_HOST=
DATABASE_PORT=
DATABASE_URL=
```

Do not commit `.env` or production secrets to version control.

### 5. Create the database

Create the MySQL database named in `DATABASE_NAME`, then apply Django migrations:

```bash
python manage.py migrate
```

Create an administrator account if needed:

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

Open <http://127.0.0.1:8000/> in a browser. The admin interface is available at <http://127.0.0.1:8000/admin/>.

## Common Commands

Run Django checks:

```bash
python manage.py check
```

Collect production static files:

```bash
python manage.py collectstatic
```

Create migrations after model changes:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Main Routes

| Route             | Purpose                      |
| ----------------- | ---------------------------- |
| `/`               | Home page and course listing |
| `/login/`         | User login                   |
| `/register/`      | User registration            |
| `/dashboard/`     | Student search dashboard     |
| `/add_student/`   | Add a student                |
| `/view_students/` | View student records         |
| `/drives/`        | View job drives              |
| `/admin/`         | Django administration        |

## Production Notes

- Set `DEBUG=False` in production.
- Use a strong, unique `SECRET_KEY`.
- Configure `ALLOWED_HOSTS` for the deployed domain.
- Use a managed MySQL database and keep its credentials in environment variables.
- Configure persistent storage for uploaded files under `MEDIA_ROOT`.
- Run `python manage.py collectstatic` during deployment.
- Use HTTPS and review Django's deployment checklist before going live.

## License

This project is licensed under the [MIT License](LICENSE).
