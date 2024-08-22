# Blog Project

A simple Django-based blog application where users can create, read, update, and delete blog posts.

## Installation

1. Clone the repository:

git clone https://github.com/jbloch100/blog_project.git
cd blog_project

2. Create a virtual environment and install dependencies:

python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

3. Apply migrations:

python manage.py migrate

4. Create a superuser (for admin access):

python manage.py createsuperuser

5. Run the development server:

python manage.py runserver

6. Visit `http://127.0.0.1:8000/` to see the blog in action.

## Features

- User authentication (login, logout)
- Create, read, update, and delete blog posts
- Admin panel for managing posts

## License

This project is licensed under the MIT License - see the [License](License) file for details.