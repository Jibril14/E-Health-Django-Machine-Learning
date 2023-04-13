

from django import forms
from .models import User


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'role',
            'address',
            'password']
