# Blogs-Jinja-Py

Flask Blog is a web application built with Flask that allows users to create, edit, and delete blog posts. It features a user-friendly interface for managing blog content and includes additional pages for information about the site and a contact form for user inquiries.

## Features

- **Create New Post**: Users can create new blog posts by filling out a form with a title, subtitle, author name, image URL, and content.

- **Edit Post**: Users can edit existing blog posts by accessing the edit form and making changes to the post details.

- **Delete Post**: Users can delete existing blog posts, removing them from the database.

- **View All Posts**: Users can view all existing blog posts on the homepage, with links to individual post pages.

- **View Individual Post**: Users can view individual blog posts in detail, including the title, author, date, and content.

- **About Page**: Users can access an about page providing information about the website or the author.

- **Contact Page**: Users can submit inquiries through a contact form, which sends an email notification to the specified email address.

## Setup

1. Install Dependencies: Run `pip install -r requirements.txt` to install all required packages.

2. Set up Environment Variables: Set the following environment variables:

   - `EMAIL`: Your email address for receiving contact form submissions.
   - `EMAIL_PASSWORD`: Your email password for SMTP authentication.

3. Database Setup: Run `python` in your terminal to enter the Python interactive shell, then run the following commands:

   ```python
   from app import db
   db.create_all()
   exit()
