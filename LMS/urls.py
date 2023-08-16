"""
URL configuration for meal_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from library_app.views import *
from django.contrib import admin
from django.urls import include, path
from library_app.frontviews import *
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include ('library_app.urls'))
    path('', index, name="home_page"),
    # path('booklist/', book_list, name="book_list"),

    path('home-page/', index, name='index'),
    path('login/',login_page, name='login_page'),
    path('register/',register_page, name='register_page'),
    
    path('logout/',logout_page, name='logout_page'),

    path('add_new_student/', add_new_student, name='new_student'),
    path('view_students/', view_students, name='view_students'),
    path('delete-student/<id>/', delete_student, name='delete_student'),
    path('delete-book/<id>/', delete_books, name='delete_student'),
    path('update-student/<id>/', update_student, name='update_student'),
    path('update-issuedbook/<id>/', update_issued_book, name='update_issued_book'),
    path('view-book/', view_books, name='view_books'),
    path('issued-book/', get_transaction_details, name='get_transaction_details'),
    path('issue-book/', issue_book, name='issue_book'),
    
    
    # path('add_new_book', views.add_new_book, name='new_book'),
    # path('add_book_issue', views.add_book_issue, name='book_issue'),
    # path('add_new_book_instance', views.add_new_book_instance, name='add_new_book_instance'),
    
    # path('view_books', views.view_books, name='show_book_record'),
    # path('view_books_issued', views.view_bissue, name='show_issue_record'),
    # path('edit/student/<str:roll>',views.edit_student_data,name="Edit Student data"),
    # path('edit/book/<uuid:id>',views.edit_book_data,name="Edit Student data"),
    # path('delete/student/<str:roll>',views.delete_student,name="Delete Student data"),
    # path('delete/book/<str:id>',views.delete_book,name="Delete book data"),
    # path('return_book/<int:id>',views.return_issued_book,name="return_issued_book"),
    # path('edit_issued/<int:id>',views.edit_issued,name="edit_issued"),
]

admin.site.index_title="Library"
