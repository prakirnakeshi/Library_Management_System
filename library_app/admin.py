
from django.contrib import admin
# Register your models here.

from library_app.models import *
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors', 'isbn', 'publisher')

# Register the Book model with the custom admin class
admin.site.register(Book, BookAdmin)
admin.site.register(Student_information)
admin.site.register(Department)
admin.site.register(StudentID)


class TranscationAdmin(admin.ModelAdmin):
    list_display = ('book', 'student', 'issue_date', 'return_date','rent_fee')

admin.site.register(Transaction, TranscationAdmin)
