# Author Project

## Description
The Author Project is a simple CRUD web application for managing a list of Authors. It allows users to add, update, delete, and view them. The project is built using Python with Django, HTML, and CSS.

### Prerequisites
- Python 3.x
- pip (Python package installer)
- Django 5.1
- some other stuff that you gotta figure out :D

### Steps
1. Clone the repository:
    ```sh
    git clone https://github.com/amdla/authors_project.git
    ```
2. Navigate to the project directory:
    ```sh
    cd authors_project
    ```
3. Apply migrations:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```
4. Run the application:
    ```sh
    python manage.py runserver
    ```
5. Alternatively you can run just
   ```sh
   python manage.py test authors_app
    ```
   to run the test file.

## Usage
Access the application by opening `http://127.0.0.1:8000` in your web browser.

---
Made with ❤️ by [amdla](https://github.com/amdla).
