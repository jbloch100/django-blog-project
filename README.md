# Blog Project

A simple Django-based blog application where users can create, read, update, and delete blog posts.

## Table of Contents

- [Installation](#installation)
- [Features](#features)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [License](#license)
- [Contributing](#contributing)

## Installation

### Prerequisites

- Python 3.x
- Git
- Virtualenv (optional but recommended)

### Steps

1. Clone the repository:

	```bash
	git clone https://github.com/jbloch100/blog_project.git
	cd blog_project
	```

2. Create a virtual environment and install dependencies:

	```bash
	python3 -m venv env
	source env/bin/activate	# On Windows use `env\Scripts\activate`
	pip install -r requirements.txt
	```

3. Apply migrations:

	```bash
	python manage.py migrate
	```

4. Create a superuser (for admin access):

	```bash
	python manage.py createsuperuser
	```

5. Run the development server:
	
	```bash
	python manage.py runserver
	```

6. Visit `http://127.0.0.1:8000/` to see the blog in action.

## Features

- User authentication (login, logout)
- Create, read, update, and delete blog posts
- Admin panel for managing posts

## Usage

1. Register for a new account or log in with existing credentials.
2. Once logged in, you can create new blog posts, edit or delete existing ones.
3. Access the admin panel at `http://127.0.0.1:8000/admin/` for more administrative controls.

## Screenshots

### Homepage
![Homepage Screenshot](path/to/homepage_screenshot.png)

### Create Post
![Create Post Screenshot](path/to/create_post_screenshot.png)

## License

This project is licensed under the MIT License - see the [License file](License) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your changes.