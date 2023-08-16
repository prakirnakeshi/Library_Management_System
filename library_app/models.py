from django.db import models
from requests import request
from django.contrib.auth.models import User

class Department(models.Model):
    department = models.CharField(max_length=100)
    def __str__(self)->str:
        return f"{self.department}"

    class Meta:
        # app_label = 'library_app'
        ordering=['department']
        

class Book(models.Model): 
    title = models.CharField(max_length=200,default=True)
    authors = models.CharField(max_length=100)
    isbn = models.CharField(max_length=50)
    publisher = models.CharField(max_length=100)

    def __str__(self)->str:
        return f"{self.title}=>{self.authors}=>{self.isbn}=>{self.publisher}"


class StudentID(models.Model):
    student_id=models.CharField(max_length=100)

    def __str__(self)->str:
        return self.student_id

class Student_information(models.Model):
    department=models.ForeignKey(Department, related_name="depart", on_delete=models.CASCADE)
    student_id=models.OneToOneField(StudentID, related_name="studentid", on_delete=models.CASCADE, default=True)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(default=True)
    # outstanding_debt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self)->str:
        return self.student_name
    class Meta:
        ordering=['student_name']
        verbose_name="student" 

class Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student=models.ForeignKey(Student_information, on_delete=models.CASCADE)
    issue_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    rent_fee = models.DecimalField(max_digits=6, decimal_places=2, default=0)

class UserModel(models.Model):
    User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True) # meaning if the user is deleted, all the data created by the user will be deleted. Also use, on_delete.CASCADE