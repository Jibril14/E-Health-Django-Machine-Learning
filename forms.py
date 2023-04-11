import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class BorrowBookForm(forms.Form):
    return_date = forms.DateField(help_text="Enter a date between now and 4 weeks.")
    status = forms.CharField(max_length=1, required=False, widget=forms.HiddenInput )


    def clean(self):
        all_data = super().clean()
        return_date = self.cleaned_data['return_date']
        status = 'o'

        # Check if a date is not in the past.
        if return_date < datetime.date.today():
            raise ValidationError(_('Invalid date - return date in past'))

        # Check if a date is in the allowed range (+4 weeks from today).
        if return_date > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date -Return Date must be within 4weeks'))

        # Remember to always return the cleaned data.
        return all_data


class UserRegistrationForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username', 'email', 'password')


