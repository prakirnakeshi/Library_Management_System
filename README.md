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

- Use the admin interface to manage books, members, and book issues.
- Perform CRUD operations on books and members.
- Issue books to members and track borrowed books.
- Search for books by name and author.
- Charging rent fees on book returns is automated.
- The system ensures that a member's debt does not exceed Rs. 500.

## Screenshot
# Login Page
![Screenshot (510)](https://github.com/prakirnakeshi/Library_Management_System/assets/84929360/d51cb541-d9bf-4515-bda9-50e7e5d45e97)

# Add Student Details
![Screenshot (511)](https://github.com/prakirnakeshi/Library_Management_System/assets/84929360/36efab82-ecca-4108-a458-bfe32349d3fa)

# Search Student 
![Screenshot (512)](https://github.com/prakirnakeshi/Library_Management_System/assets/84929360/810e5f1d-32a6-4281-aa26-e2271186e41b)

# Search Book Name
![Screenshot (513)](https://github.com/prakirnakeshi/Library_Management_System/assets/84929360/cf74a100-c290-4bc7-9937-73d5880163cf)

# Issue Book to a Student
![Screenshot (514)](https://github.com/prakirnakeshi/Library_Management_System/assets/84929360/7da365ff-164b-4491-9b77-6b26c75f2efc)

# Transaction Details of Issued Book
![Screenshot (515)](https://github.com/prakirnakeshi/Library_Management_System/assets/84929360/e414fe89-a4ef-4992-b32d-6789416a42e8)

# Add Return Date
![Screenshot (516)](https://github.com/prakirnakeshi/Library_Management_System/assets/84929360/39a8524e-922c-4b36-a1ce-d7e6f1cdbe20)

## Contributing

Contributions to the Library Management System are welcome! If you find a bug or want to suggest an enhancement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---
