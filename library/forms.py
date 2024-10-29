from django import forms
from django.contrib.auth.models import User
from . import models

class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

class StudentUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']

class StudentExtraForm(forms.ModelForm):
    email_address = forms.EmailField(label="Email Address")  # Changed to Email Address
    house_address = forms.CharField(max_length=255, label="House Address")  # Changed to House Address

    class Meta:
        model = models.StudentExtra
        fields = ['email_address', 'house_address']  # Updated fields list

class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = ['name', 'isbn', 'author', 'category']

class IssuedBookForm(forms.Form):
    isbn2 = forms.ModelChoiceField(queryset=models.Book.objects.all(), empty_label="Name and Label", to_field_name="isbn", label='Name and Isbn')
    enrollment2 = forms.ModelChoiceField(queryset=models.StudentExtra.objects.all(), empty_label="Name and Email Address", to_field_name='email_address', label='Email Address')  # Updated label
