# Prolibrary - A Book Record Management System

Prolibrary is a web-based application designed for managing a library's book records. This system allows librarians and users to add, edit, view, search, delete, and sort book records efficiently. 

Built with Django, it leverages the framework's robust back-end capabilities to provide a smooth and intuitive user experience.



## Features

- **View Books:** Users can view a list of all books in the library with details such as title, price, category, and description.
- **Add Books:** A simple form to add new books to the system.
- **Edit Books:** Update the details of existing books.
- **Delete Books:** Remove books from the system.
- **Search Functionality:** Quickly find books by their title.
- **Sort by Price:** Users can sort the book list based on the price, either in ascending or descending order.
- **Responsive Design:** The application is usable on both desktop and mobile browsers.


## Getting Started

### Prerequisites
```
Python 3.x
Django (latest version)
```


1. Clone the repository:

   ```bash
   git clone https://github.com/hellomohitsangwan/prolibrary.git

2. Run database migrations:
   ```bash
    cd prolibrary
    python manage.py makemigrations
    python manage.py migrate


3. art the development server:
   ```bash
    python manage.py runserver



4. Visit http://localhost:8000 to access the Prolibrary application.