# Micro-blogging-Platform

## Overview
The Micro-blogging-Platform is a web application that allows users to create, view, and manage blogs. It features user authentication, allowing users to register, log in, and log out. The application is built using Django, a high-level Python web framework.

## Features
- User registration and authentication
- Create, view, edit, and delete blogs
- User profile management
- Responsive design with Bootstrap for a modern user interface

## Technologies Used
- Django (Python web framework)
- SQLite (Database)
- HTML/CSS (Frontend)
- Bootstrap (Styling)
- JavaScript (for interactivity)

## Installation

### Prerequisites
- Python 3.x
- pip (Python package installer)
- Virtual environment (recommended)

### Steps to Set Up
1. **Clone the repository:**
   ```bash
   git clone https://github.com/VyshnavSanthosh/Micro-blogging-Platform-Using-Django.git
   cd blogs_django_project1
   ```

2. **Set up a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage
- Users can register for a new account.
- After logging in, users can create blogs, view their own blogs, and manage their profiles.
- Users can log out to end their session.

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

## Acknowledgements
- Django documentation for guidance on best practices.
- Bootstrap for responsive design components.
