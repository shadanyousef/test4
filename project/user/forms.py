from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no', 'password1', 'password2']

    def clean_phone_no(self):
        phone_no = self.cleaned_data.get('phone_no')
        if phone_no and len(phone_no) != 10:
            raise forms.ValidationError("Phone number must have exactly 10 digits.")
        return phone_no

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name and not first_name.isalpha():
            raise forms.ValidationError("First name should only contain letters.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if last_name and not last_name.isalpha():
            raise forms.ValidationError("Last name should only contain letters.")
        return last_name