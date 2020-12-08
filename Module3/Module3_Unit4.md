Although the admin interface was automatically created, no users were configured. In order to login the Django admin site we now need to create our first user. Before starting make sure to activate your virtual environment and then follow the below steps to add an admin to your application.

1. By default Django requires that an admin be a superuser to login. So to create our first superuser, navigate to the inside of the first **myfirstproject** folder and enter the below line into the command line. 

    python manage.py createsuperuser

2. After running this command it will ask you for a username, an email, and then a password. For this example we have chosen **admin** for the username. Once the information is entered an admin superuser will be created.