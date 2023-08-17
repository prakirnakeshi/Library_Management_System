from datetime import timedelta
from django.shortcuts import render
from faker import Faker
fake = Faker()
name = fake.name()
import random

from library_app.models import *
def seed_db(n=20) -> None:
    try:    
        for _ in range(n):
            departments_objs = Department.objects.all()
            random_index = random.randint(0, len(departments_objs)-1) # generating random number between 0 and the length of the department(CSE, EEE, ECE i.e 3 for this case)
            department = departments_objs[random_index] # assiging the randomly generated number to each department, each department will have its own number.
            student_id = f'STU-0{random.randint(100,999)}'
            student_name = fake.name()
            student_email = fake.email()
            print("Chalo aa gaye")
            student_id_obj = StudentID.objects.create(student_id=student_id)

            student_obj = Student_information.objects.create(
                student_id=student_id_obj,
                student_name=student_name,
                student_email=student_email,
                department=department, # here we are assigning assigned foreign key to each candidate
            )
            # book_objs = Book.objects.all()
            # random_book = random.choice(book_objs)
            
            # issue_date = fake.date_this_decade()
            # return_date = fake.date_between(start_date=issue_date)
            # rent_fee = fake.pydecimal(left_digits=3, right_digits=2, positive=True)

            # # Calculate the difference between issue_date and return_date
            # date_difference = (return_date - issue_date).days

            # if date_difference > 7:
            #     additional_days = date_difference - 7
            #     additional_rent_fee = additional_days * 10
            #     rent_fee += additional_rent_fee
            
            # Transaction.objects.create(
            #     book=random_book,
            #     student=student_obj,
            #     issue_date=issue_date,
            #     return_date=return_date,
            #     rent_fee=rent_fee,
            # )
            
            
            # print("Recieved")
    except Exception as e:
        print(e)
    
def generate_issuedbook_(n=20) -> None:
    try:
        student_objs = list(Student_information.objects.all())  # Convert the queryset to a list
        
        for _ in range(n):
            book_objs = Book.objects.all()
            random_book = random.choice(book_objs)
            
            student = random.choice(student_objs)  # Select a random student from the list
            
            issue_date = fake.date_this_decade()
            # return_date = fake.date_between(start_date=issue_date)
            # rent_fee = fake.pydecimal(left_digits=2, right_digits=0, positive=True)
            # Generate a random return date between issue_date and 15 days later
            max_return_date = issue_date + timedelta(days=70)
            return_date = fake.date_between_dates(date_start=issue_date, date_end=max_return_date)
            
            rent_fee = fake.pydecimal(left_digits=2, right_digits=0, positive=True)

            # Calculate the difference between issue_date and return_date
            date_difference = (return_date - issue_date).days

            if date_difference > 7:
                additional_days = date_difference - 7
                additional_rent_fee = additional_days * 10
                rent_fee += additional_rent_fee
            
            Transaction.objects.create(
                book=random_book,
                student=student,  # Use the selected student instance
                issue_date=issue_date,
                return_date=return_date,
                rent_fee=rent_fee,
            )
            
            print("Data Imported")
    except Exception as e:
        print(e)


