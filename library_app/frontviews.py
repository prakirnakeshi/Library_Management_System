import datetime
from django.shortcuts import render, redirect,HttpResponse
from faker import Faker
import faker
# from .forms import StudentsForm, BookForm, Book_IssueForm,Book_instanceForm
# from .models import Students, Book, Book_Issue,BookInstance
# from 
from library_app.models import *
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout #
from django.contrib.auth.decorators import login_required
from django.db.models import Q
@login_required(login_url="/login/")  # meaning only after login, this page will load. Else one can use /view_book/
def index(request):
    return(render(request, 'frontend/base.html'))

@login_required(login_url="/login/")
def add_new_student(request):
    if request.method=="POST":
        data=request.POST
        department_name=data.get('department')
        student_id=data.get('student_id')
        student_name=data.get('student_name')
        student_email=data.get('student_email')
        
        print(student_name)
        # Retrieve the Department instance based on the department name
        try:
            department = Department.objects.get(department=department_name)
        except Department.DoesNotExist:
            # Handle the case when the department doesn't exist
            return HttpResponse("Department not found")
        # Check if student_id already exists
        if StudentID.objects.filter(student_id=student_id).exists():
            return HttpResponse("Student ID already exists")

        # Create StudentID instance
        student_id_obj, created = StudentID.objects.get_or_create(student_id=student_id)
        
        Student_information.objects.create(
            department=department,
            student_id=student_id_obj,
            student_name=student_name,
            student_email=student_email
        )
        return redirect('/add_new_student/')
    queryset = Student_information.objects.all()
# FOR SEARCHING
    if request.GET.get('search'):
        queryset = queryset.filter(student_name__icontains = request.GET.get('search'))
    
    context={'student_data':queryset}
    return (render(request, 'frontend/add_new_student.html',context))
@login_required(login_url="/login/")
def view_students(request):
    student_data=Student_information.objects.all()
    if request.GET.get('search'):
        search=request.GET.get('search')   
        student_data=student_data.filter(
            Q(student_name__icontains=search)|
            Q(student_id__student_id__icontains=search) 
            )
    context={'student_data':student_data}
    return render(request,'frontend/view_students.html',context)

@login_required(login_url="/login/")
def update_student(request, id):
    queryset = Student_information.objects.get(id=id)
    if request.method =="POST":
        data=request.POST
        department=data.get('department')
        student_id=data.get('student_id')
        student_name=data.get('student_name')
        student_email=data.get('student_email')

        queryset.department=department
        queryset.student_id=student_id
        queryset.student_name=student_name
        queryset.student_email=student_email
        

        queryset.save()
        return redirect('/view_students/')
    context={'student_data':queryset}
    return render(request,'frontend/edit_student_data.html',context)

def delete_student(request, id):
    queryset = Student_information.objects.get(id=id)
    queryset.delete()
    return redirect('/view_students/')

def delete_books(request, id):
    queryset = Book.objects.get(id=id)
    queryset.delete()
    return redirect('/view_book/')

@login_required(login_url="/login/")
def view_books(request):
    queryset = Book.objects.all()
    if request.GET.get('search'):
        search=request.GET.get('search')   
        queryset=queryset.filter(
            Q(title__icontains=search)|
            Q(authors__icontains=search)|
            Q(publisher__icontains=search)|
            Q(isbn__icontains=search)
            )
    context={'book_data':queryset}
    return render(request,'frontend/view_books.html', context)

def login_page(request):
    if request.method == "POST":  # getting data, whatever input was provided in the feild during login
    
        username=request.POST.get('username')
        password=request.POST.get('password')

        #To check if that username is registered or not.
        if not User.objects.filter(username=username).exists():
            messages.info(request, "User doesn't exists.")
            return redirect('/login/')
        
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Inavlid password ")
            return redirect('/login/')
        else:
            login(request,user)    # to maintain the logged in sessio
            return redirect('/home-page/')
    return render(request,'frontend/login.html')

def logout_page(request):
    logout(request) 
    return redirect('/login/')

def register_page(request):
    if request.method == "POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=User.objects.filter(username=username)

        if user.exists():
            messages.info(request, "Username already taken")
            return redirect('/login/')
        user= User.objects.create(
           first_name=first_name, 
           last_name=last_name,
           username=username
        )
        user.set_password(password) # to encrpt the password
        user.save()
        messages.info(request, "Congrats!! You've been Resgitered.")
        return redirect('/register/')
    
    return render(request,'frontend/register.html')

def return_book(request):
    query=get_transaction_details.objects

@login_required(login_url="/login/")
def get_transaction_details(request):
    queryset=Transaction.objects.all()
    book_data=Book.objects.all()    
    if request.GET.get('search'):
        search=request.GET.get('search')  
        print("Search query:", search) 
        queryset=queryset.filter(
            Q(book__title__icontains=search)| # only one header it will search, if not get then move to other.
            Q(student__student_name__icontains=search) # "student" variable in Transaction act as FOREIGN KEY, so"__"" is use to access the objects of the FOREGIN KEY, 
            # as it import class which contains the required field we want from it, "student_name" in our case
            )
    return render(request,'frontend/issued_books.html', {'transaction':queryset, 'book_data': book_data})


@login_required(login_url="/login/")
def issue_book(request):
    if request.method=="POST":
        student_id=request.POST.get('student_id')
        student_name=request.POST.get('student_name')
        book_name=request.POST.get('book_name')
        issuebookdate=request.POST.get('issuebookdate')

        # if not StudentID.objects.filter(student_id=student_id).exists():
        #     messages.info(request, "Student_id not found.")
        # if not Student_information.objects.filter(student_name=student_name).exists():
        #     messages.info(request, "Student Name not found.")
        # if not Book.objects.filter(book_name=book_name).exists():
        #     messages.info(request, "Book not found.")

        try:
            student = Student_information.objects.get(student_id__student_id=student_id, student_name=student_name)
            book = Book.objects.get(title=book_name)
        except (Student_information.DoesNotExist, Book.DoesNotExist):
            messages.error(request, "Student or Book not found.")
            return render(request, 'frontend/toissuebook.html')
        
        
        # transactiondetails_obj=Transaction.objects.all()

        # if transactiondetails_obj.rent_fee 
        if Transaction.objects.filter(student=student, return_date__isnull=True, rent_fee__gt=500).exists():
            messages.error(request, "Student has outstanding rent fees and cannot issue a book.")
            return render(request, 'frontend/toissuebook.html')
        else:
            Transaction.objects.create(
                student=student,
                book=book,
                issue_date=issuebookdate
            )
    return render(request, 'frontend/toissuebook.html')

# from library_app.utils import get_books
# def import_books_view(request):
#     if request.method == 'POST':
#         num_books = request.POST.get('num_books')
#         if num_books > 0:
#             get_books(num_books)
#             return render(request, 'frontend/view_books.html', {'num_books': num_books})
    
#     return render(request, 'frontend/view_books.html')
@login_required(login_url="/login/")
def update_issued_book(request, id):
    queryset = Transaction.objects.get(id=id)
    if request.method =="POST":
        issue_date = request.POST.get('issue_date')
        return_date = request.POST.get('return_date')
        rent_fee= request.POST.get('rent_fee')

         # Calculate date difference and additional rent fee
        date_difference = 0  # Initialize with a default value
        if issue_date and return_date:  # Make sure both issue_date and return_date are not None
            issue_date_obj = datetime.strptime(issue_date, '%Y-%m-%d')
            return_date_obj = datetime.strptime(return_date, '%Y-%m-%d')
            date_difference = (return_date_obj - issue_date_obj).days
            
            rent_fee = faker.pydecimal(left_digits=3, right_digits=2, positive=True)

            if date_difference > 7:
                additional_days = date_difference - 7
                additional_rent_fee = additional_days * 10
                rent_fee += additional_rent_fee
        else:
            rent_fee = 0
        queryset.return_date = return_date
        queryset.rent_fee = rent_fee
        queryset.save()
        return redirect('/issued-book/')
    context={'student_data':queryset}
    return render(request,'frontend/updateissuedbooks.html',context)