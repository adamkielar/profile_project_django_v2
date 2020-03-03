import re
from PIL import Image

from django.core import validators
from django.core.exceptions import ValidationError
from django.core.files import File
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import PasswordChangeForm
from django import forms

from flatpickr import DatePickerInput
from zxcvbn_password.fields import PasswordField, PasswordConfirmationField
from tinymce.widgets import TinyMCE
from . import models


class AvatarForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = [
            "avatar",
        ]

    class Media:
        css = {"all": ("/assets/css/global.css",)}


class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = [
            "first_name",
            "last_name",
        ]


class ProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=DatePickerInput())
    bio = forms.CharField(
        widget=TinyMCE(attrs={"cols": 70, "rows": 20}),
        validators=[validators.MinLengthValidator(10)],
    )

    class Meta:
        model = models.Profile
        fields = [
            "email",
            "confirm_email",
            "city",
            "date_of_birth",
            "hobby",
            "bio",
        ]

    class Media:
        css = {"all": ("/assets/css/global.css",)}

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        confirm_email = cleaned_data.get("confirm_email")

        if email and confirm_email:
            if email != confirm_email:
                raise forms.ValidationError("Emails must match. Please check again")


class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(ChangePasswordForm, self).__init__(user, *args, **kwargs)

    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password1 = PasswordField()
    new_password2 = PasswordConfirmationField(confirm_with=new_password1)

    class Meta:
        form = PasswordChangeForm
        fields = [
            "old_password",
            "new_password1",
            "new_password2",
        ]

    class Media:
        css = {"all": ("/assets/css/global.css",)}

