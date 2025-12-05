# Django Blog Website

This repository contains the source code for a full‑featured blog website built with Django.  
It was developed while following the “Django Blogging System” premium course by Tech With Rathan, and then customized and extended as part of a personal learning project.

![Blog UI](UI.png)

## What this project includes

- Real‑world Django project structure with separate apps for blogs, dashboards, and assignments.  
- Models for Blog posts, Categories, Comments, and user relationships, including slugs and media (image) handling.  
- Forms for creating and editing posts, user registration, and adding comments.  
- Authentication and authorization using Django’s built‑in auth system: login, logout, groups, permissions, and decorators.  
- Custom admin configurations and list displays for better content management.  
- Dashboards for Editors and Managers with role‑based access and statistics.  
- Search, pagination, featured posts, and recent posts sections on the blog.  
- Static and media files configuration for images, CSS, and other assets.  
- A deployment‑ready setup with a `requirements.txt` file for easy environment recreation.

## What I learned

Working on this project helped in:

- Understanding how to structure a Django project into multiple apps with clear responsibilities.  
- Designing relational models (Blog, Category, Comment) and using slugs for SEO‑friendly URLs.  
- Using Django’s forms and generic views to implement full CRUD for posts and categories.  
- Implementing role‑based access control with Django Groups, permissions, and custom checks.  
- Building custom dashboards and using template inheritance, context processors, and custom error pages.  
- Handling user registration, login/logout, and restricting features to authenticated users.  

## Tech stack

- Python 3.10+  
- Django 4.x  
- SQLite for development (can be switched to PostgreSQL/MySQL in production)  

---

## How to run this project locally

Follow these steps to clone the repository, create a virtual environment, install dependencies, and start the server.

1. **Clone the repo**
git clone https://github.com/prathamdmehta/django-blog.git

2. **Create and activate a virtual environment**

Windows
python -m venv env
env\Scripts\activate

macOS / Linux
python3 -m venv env
source env/bin/activate

3. **Install dependencies**

pip install -r requirements.txt

4. **Apply migrations**

python manage.py migrate

5. **Create a superuser**

python manage.py createsuperuser

6. **Run the development server**

python manage.py runserver
