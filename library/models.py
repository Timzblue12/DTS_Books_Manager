from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

class StudentExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_address = models.EmailField(default='timzblue12@gmail.com')  # Updated field name
    house_address = models.CharField(max_length=255, default='Street Address')  # Updated field name

    def __str__(self):
        return self.user.first_name + '[' + str(self.email_address) + ']'  # Updated to reflect new field

    @property
    def get_name(self):
        return self.user.first_name

    @property
    def getuserid(self):
        return self.user.id

class Book(models.Model):
    catchoice = [
        ('fiction', 'Fiction'),
        ('history', 'History'),
        ('science', 'Science'),
        ('arts', 'Arts'),
        ('commerce', 'Commerce'),
    ]
    name = models.CharField(max_length=30)
    isbn = models.PositiveIntegerField()
    author = models.CharField(max_length=40)
    category = models.CharField(max_length=30, choices=catchoice, default='education')

    def __str__(self):
        return str(self.name) + "[" + str(self.isbn) + ']'

def get_expiry():
    return datetime.today() + timedelta(days=15)

class IssuedBook(models.Model):
    enrollment = models.CharField(max_length=30)  # This can remain as enrollment or could be updated to reflect new structure
    isbn = models.CharField(max_length=30)
    issuedate = models.DateField(auto_now=True)
    expirydate = models.DateField(default=get_expiry)
    statuschoice = [
        ('Issued', 'Issued'),
        ('Returned', 'Returned'),
    ]
    status = models.CharField(max_length=20, choices=statuschoice, default="Issued")

    def __str__(self):
        return self.enrollment
