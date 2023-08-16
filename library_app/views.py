# library/views.py


from django.shortcuts import render, redirect
# from .forms import DataImportForm
# from .models import Book

from library_app.frontviews import *
import requests
def get_books(num_books):
    print("See")
    url = "https://frappe.io/api/method/frappe-library"
    response = requests.get(url)
    data= response.json()["message"] 
    for title in data[:num_books]:
        print("API Response:", title)  
        if not Book.objects.filter(title=title["title"],authors=title["authors"],isbn=title["isbn"],publisher=title["publisher"]):
            Book.objects.create(title=title["title"],authors=title["authors"],isbn=title["isbn"],publisher=title["publisher"],)
            print("Saved")
        else:
            print("Data Exists")

            

from django.shortcuts import render, redirect

from django.shortcuts import render
from .models import Book
# from .utils import import_books  # Replace with the path to your import_books function








# library/views.py                  

from django.shortcuts import render
from library_app.models import *
def home_page(request):
    # books = Book.objects.all()
    return render(request, 'all/index.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'all/booklist.html',{'books': books})

def member_list(request):
    members = Student_information.objects.all()
    return render(request, 'all/memberlist.html', {'members': members})

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'all/transactionlist.html', {'transactions': transactions})

