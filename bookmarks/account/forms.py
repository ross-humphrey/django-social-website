from django import forms
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "first_name", "email")

    def clean_password2(
        self,
    ):  # You can define a clean_<fieldname>() method to any form fields to clean the value or raise validation errors
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Passwords don't match.")
        return cd["password2"]


class UserEditForm(forms.ModelForm):
    """
    Allows users to edit their first name, last name and email - attributes of the built in Django user model
    """

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class ProfileEditForm(forms.ModelForm):
    """
    Allows users to edit the profile data you save in the custom profile model
    """

    class Meta:
        model = Profile
        fields = ("date_of_birth", "photo")
