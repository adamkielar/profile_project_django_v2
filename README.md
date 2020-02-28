# User Profile with Django

Step to get the project running.

1. Use the `requirements.txt` file to install the project dependencies.

2. Run your migrations to create the tables in the database.
   `python manage.py migrate`

3. Run the server.
   `python manage.py runserver`


Once you add a Model with some fields or each time you make changes to the Model, make sure you run:

`python manage.py makemigrations` to create an initial/new migration file inside the `migrations` folder for that `<app>`. So when you run the `migrate` command it knows how to setup or alter the database tables before data starts getting put in those tables.

This project has following functionality:

1. You can create user profile with: First Name, Last Name, Email, Date of Birth, Bio and Avatar

2. You can edit user profile: First Name, Last Name, Email, Date of Birth, Confirm Email, Bio and Avatar

- Edit profile form has email validation

- Date of Birth uses date dropdown widget (django-flatpickr==1.0.1)

- Bio field uses tinymce ( django-tinymce==2.8.0)

3. User can change password

- password form has following validations:

must not be the same as the current password minimum password length of 14 characters. must use of both uppercase and lowercase letters must include one or more numerical digits must include one or more of special characters, such as @, #, $ cannot contain the user name or parts of the user’s full name, such as their first name

- password strength meter is included (django-zxcvbn-password==2.1.0)

4. User can edit and download his avatar (Cropper v4.1.0)

TODO: save cropped image to database