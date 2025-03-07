# Job Portal

## Overview
Job Portal is a web application built with Django that connects job seekers and recruiters. Applicants can create resumes, apply for jobs, and track their applications. Recruiters can register their companies, post job ads, and manage applications. The admin panel provides control over users, job postings, and platform settings.

## Features
### Applicant Features:
- User registration and login.
- Create and manage resumes.
- Browse job listings.
- Apply for jobs with a single click.
- Track job applications.

### Recruiter Features:
- Recruiter registration and login.
- Create and manage company profiles.
- Post job advertisements.
- View and manage applications received.

### Admin Features:
- Manage users (Applicants & Recruiters).
- Oversee job postings and company registrations.
- Ensure smooth platform operations.

## Installation & Setup

### Prerequisites
- Python 3.x
- Django
- PostgreSQL or SQLite (as per project configuration)

### Steps to Run the Project
1. **Clone the Repository**
   ```sh
   git clone <repository_url>
   cd job-portal
   ```
2. **Create a Virtual Environment & Activate It**
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Apply Migrations**
   ```sh
   python manage.py migrate
   ```
5. **Create a Superuser (Admin Account)**
   ```sh
   python manage.py createsuperuser
   ```
   Default Admin Credentials:
   ```
   Username: JobPortal
   Email: shaikhbinash702@gmail.com
   Password: Job_Portal01
   ```
6. **Run the Development Server**
   ```sh
   python manage.py runserver
   ```
7. **Access the Application**
   Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

## Tech Stack
- **Backend:** Django, Django REST Framework
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Database:** PostgreSQL / SQLite
- **Authentication:** Django's built-in authentication system

## Contributing
Feel free to contribute by submitting pull requests or reporting issues.

## License
This project is open-source and available under the MIT License.

## Contact
For any queries or suggestions, reach out via email: **shaikhbinash702@gmail.com**.

