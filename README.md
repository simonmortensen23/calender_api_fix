# Task Planner API

## Links

## Table of Contents
- [Introduction](#introduction)
- [Technologies](#technologies)
- [Bugs](#bugs)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

## Introduction

Task Planner is the perfect app for planning day to day chores or smaller tasks. With Task Planner the users has the ability to share their tasks with family, friends or co-workers and leave small task notes, due date and progress status for the others to see.

This repository is the backend of the application using the Django REST Framework(DRF) holding the API database for the front end part of the application.

## Testing

### Validator Testing
- I ran all the apps of the API through pycodestyle and fixed the missing white lines, whitespaces and too long lines.

### Manual Testing
- Manual Tests were carried out for the url paths and CRUD functionalities and shown in a table

### CRUD Testing
- Table was made to check a user could Create, Read, Update, Delete
- I used a key in the table 
    - LI meaning the user was logged in, and so could Create, and read.
    - LO meaning the user was not logged in and so could only read.
    - LI/O meaning the user was logged in and the owner so had full CRUD functionality.
![image](https://user-images.githubusercontent.com/43667190/206542859-f6c3fa79-31e2-4498-a5ee-d047e3cb33b1.png)


## Bugs

### Unfixed
- None known

## Technologies
### Languages
 - Python - Django REST framework
### Frameworks, libraries, and Programs
 - Cloudinary Storage
  - storage of images
 - Pillow
  - Image processing
 - Git
  - Version control, committing and pushing to github
 - Github
  - Storing the respository, files and images
 - ElephantSQL
  - Database storage
 - Render
  - Deploy of application
 - Django REST Auth
 - Postgres SQL
 - CORS headers

## Project Setup
1. Use the Code Institutes full template to create a new repository, and open it in Gitpod.
2. Install Django by using the terminal command: pip install 'django<4'
3. Start the project using the terminal command: django-admin startproject calender_api_fix .
4. Install the Cloudinary library using the terminal command: pip install django-cloudinary-storage
5. Install the Pillow library for image processing capabilities using the terminal command: pip install Pillow
6. Go to settings.py file to add the newly installed apps, the order is important
7. Create an env.py file in the top directory
8. In the env.py file and add the following for the cloudinary url: import os
os.environ["CLOUDINARY_URL"] = "cloudinary://API KEY HERE"
9. In the settings.py file set up cloudinary credentials, define the media url and default file storage with the following code:
import os

if os.path.exists('env.py'):
    import env

CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
}
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
10. Workspace is now ready to use.

## Deployment
### Setting up JSON web tokens
1. Install JSON Web Token authentication by using the terminal command: pip install dj-rest-auth
2. In settings.py add these 2 items to the installed apps list: 'rest_framework.authtoken' 'dj_rest_auth'
3.In the main urls.py file add the rest auth url to the pattern list: path('dj-rest-auth/', include('dj_rest_auth.urls')),
4. Migrate the database using the terminal command: python manage.py migrate
5. To allow users to register install Django Allauth: pip install 'dj-rest-auth[with_social]'
6. In settings.py add the following to the installed app list
- 'django.contrib.sites',
- 'allauth',
- 'allauth.account',
- 'allauth.socialaccount',
- 'dj_rest_auth.registration',
7. also add the line in settings.py: SITE_ID = 1
8. In the main urls.py file add the registration url to patterns: dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')
9. Install the JSON tokens with the simple jwt library: pip install djangorestframework-simplejwt
10. In env.py set DEV to 1 to check wether in development or production: os.environ['DEV'] = '1'
11. In settings.py add an if/else statement to check development or production:
- REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )],
12. Add the following code in settings.py
- REST_USE_JWT = True # enables token authentication
- JWT_AUTH_SECURE = True # tokens sent over HTTPS only
- JWT_AUTH_COOKIE = 'my-app-auth' #access token
- JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token' #refresh token
13. Create a serializers.py file in the calender_api:fix file(my project file name)
14. Add the code from the Django documentation UserDetailsSerializer as follows:
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    profile_id = serializers.ReadOnlyField(source='profile.id')
    
    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + \
            ('profile_id',)
15. In settings.py overwrite the default User Detail serializer
16. Run the migrations for database again: python manage.py migrate
17. Update the requirements file with the following terminal command: pip freeze > requirements.txt
18. Make sure to save all files, add and commit followed by pushing to Github.

### Deployment to ElephantSQL and Render
1. This project was initially deployed to Heroku but due to changes it was moved to ElephantSQL and Render
2. Create new instance on ElephantSQL
3. Set name to event_api
4. Confirmed by pressing "Create Instance"
5. Skipped migrating databases as it had no important data stored
6. Created build.sh file in API project
7. Pasted install code into file:
 - set -o errexit
 - pip install -r requirements.txt
 - python manage.py makemigrations && python manage.py migrate
8. Deleted Procfile as Render doesn't need it
9. Added, comitted and pushed
10. Clicked on New + button and chose webservice 
11. Connected with calender_api_fix respository
12. In settings I set the environment to Python3 and chose main branch
13. Set build command to: ./build.sh
14. Set start command to:  gunicorn calender_api.wsgi:application
15. Under the Environment tab I chose the advanced option
16. Added Environment Variable and the key: WEB_CURRENCY, value 4
17. Copy and pasted env.py content into a Secret File and removed DEV lines
18. Set project to autodeployment. 

## Credits
 - The code institute moments project was used as a guideline for the API and CSS. 
## Acknowledgements
 - My friend Nikolaj who helped me throughout this project.
