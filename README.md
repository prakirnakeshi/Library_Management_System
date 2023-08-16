# Library Management System

The Library Management System is a web application designed to facilitate library operations and management. It is specifically tailored for librarians, offering features that enable efficient handling of books, members, book issuing, and more.

## Features

The Library Management System includes the following features:

1. **CRUD Operations:**
   - Create, Read, Update, and Delete operations for managing books and members.

2. **Book Issuing:**
   - Ability to issue books to library members, tracking which books are currently borrowed.

3. **Book Search:**
   - Search for books by name and author to quickly locate desired titles.

4. **Rent Fee Calculation:**
   - Automatically calculate and charge rent fees when books are returned.

5. **Debt Limit:**
   - Ensures that a member's outstanding debt does not exceed Rs. 500.

## Getting Started

Follow these steps to set up and run the Library Management System locally:

1. **Clone the Repository:**

2. **Create and Activate a Virtual Environment (Optional):**
python -m venv venv
venv\Scripts\activate (on Windows)

3. **Install Dependencies:**
pip install -r requirements.txt

4. **Configure the Database:**
- Open `settings.py` in the `LMS` directory and update the database settings.

5. **Apply Migrations:**
python manage.py makemigrations
python manage.py migrate

6. **Create Superuser (Admin):**
python manage.py createsuperuser

7. **Run the Development Server:**
python manage.py runserver

8. **Access the Application:**
- Open a web browser and navigate to `http://127.0.0.1:8000/admin/` to access the admin interface.
- Use the superuser credentials created earlier to log in.

## Usage

- Use the admin interface to manage books, members, and book issuing.
- Perform CRUD operations on books and members.
- Issue books to members and track borrowed books.
- Search for books by name and author.
- Charging rent fees on book returns is automated.
- The system ensures that a member's debt does not exceed Rs. 500.

## Contributing

Contributions to the Library Management System are welcome! If you find a bug or want to suggest an enhancement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---
*This README template is provided by ChatGPT, an AI language model by OpenAI.*
