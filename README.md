# User Profile | Python and Django

## Description

This project has following functionality:

1. You can create user profile with: First Name, Last Name, Email, Date of Birth, Bio and Avatar

2. You can edit user profile: First Name, Last Name, Email, Date of Birth, Confirm Email, Bio and Avatar

3. User can change password

* password form has following validations:

must not be the same as the current password minimum password length of 14 characters. must use of both uppercase and lowercase letters must include one or more numerical digits must include one or more of special characters, such as @, #, $ cannot contain the user name or parts of the user’s full name, such as their first name

* password strength meter is included

4. User can edit and download his avatar

## Technologies and Packages Used in App

* Django
* [Django Flatpickr](https://pypi.org/project/django-flatpickr/)
* [Django Tinymce](https://pypi.org/project/django-tinymce/)
* [Django ZXCVBN Password](https://pypi.org/project/django-zxcvbn-password/)
* [Django Cropperjs](https://pypi.org/project/django-cropperjs/)

## How to use

Step to get the project running.

1. Use the `requirements.txt` file to install the project dependencies.

2. Run your migrations to create the tables in the database.
   `python manage.py migrate`

3. Run the server.
   `python manage.py runserver`
