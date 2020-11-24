[6]: https://docs.djangoproject.com/en/3.1/ref/django-admin/ "Command-line Utility"

## Hello, Django

### Exercise: Create a project with Django-admin

Now that Django is installed we are ready to begin the process of creating a project, but before we actually start coding there are a couple of things we have to do to create a Django project. While there are a couple of options for completing the following tasks for our purposes we will be using Visual Studio Code.
        
First, go to the command line and navigate to the directory that you would like to store your Django project. Once you are in the correct directory then run the following command to create your new project.

[!Note] If you decided to create a virtual environment for your Django framework, then make sure you are running this command from your activated virtual environment. 

    $ django-admin startproject myfirstproject

After running the above command the new project should now be in your chosen directory. In this instance you would see a new folder called 'myfirstproject'.

### Navigating the Project structure

Now that the Django project has been created let's look at the structure to see what was included.

    myfirstproject/
            manage.py
            myfirstproject/
                    **init**.py
                    settings.py
                    urls.py
                    asgi.py
                    wsgi.py

1. The first or outer **myfirstproject** in the structure is your root directory which contains the entire project.
2. Next you have **manage.py**. This is a command-line utility that is created in every Django project and actually has the same function as 'django-admin'. Below is an example of how this could be used if you were inside the project folder and wanted to see the available subcommands. 
        
        django-admin help

        OR

        python manage.py help
        
    For more information about the Django CLI, you can consult the [django-admin documentation][6].

3. The inner **myfirstproject** is considered the Python package for your project.
4. Next we have **init.py** and if you look at the contents of this file you will notice that it is empty. Don't worry as this should be empty and it functions to tell Python that this directory should be considered a package.
5. Next in line we have **settings.py**. This file contains all of your settings or configurations.
6. Next is **urls.py**. This file contains the urls within the project.
7. Lastly we have **asgi.py** and **wsgi.py**. These last two files serve as the entry point for your web servers depending on what type of server is deployed.

### Running Your First Project

Now that Django is installed, a project has been created, and we have examined the project structure it is time to make sure everything works.

Navigate to the **myfirstproject** root directory and enter the below in the command line.
        
    python manage.py runserver
        
If the project runs correctly it will start to perform system checks, and start your development server. Copy and paste the url of your development server in your preferred browser, and you should see a Django 'Congratulations' page with a rocket taking off.

### Projects vs Apps

Now that the first Django project has been created, we will continue on to create our first app but let's first define the difference between a project and an app. 
- App - provides the instructions of how a web application should function such as our "Hello, world!" app.

- Project - contains all of the necessary settings or apps for a specific website.
        
Now that we know the difference between a project and an app let's move to our next task of creating an app!