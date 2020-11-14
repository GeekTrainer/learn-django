[1]: https://docs.djangoproject.com/en/3.1/topics/install/ "Django Installation Guide"
[2]: https://www.python.org/  "Install Python"
[3]: https://www.djangoproject.com/ "Django Website"
[4]: https://www.djangoproject.com/start/ "Get Started with Django"
[5]: https://docs.djangoproject.com/en/3.1/intro/install/ "Django Quick Install Guide"
[6]: https://docs.djangoproject.com/en/3.1/ref/django-admin/ "Command-line Utility"

#
# Module 1: Getting started with Django

Introduction
* Introduction Summary

    The Python language has quickly become one of the most popular programming languages and finding the right platform for your application is crucial for on time deployments. This module will discuss a popular framework named Django that is based on the Python language. In order to begin to understand the Django framework, we will take you through the types of applications that are best suited for deployment, installation, and creating your first program.

* Learning Objectives
    - In this module you will learn:
        - Why Django is great for quick deployment of web applications
        - The difference between Django and Flask
        - What types of applicatons are best for Django
        - How to install Django
        - How to create a simple program in Django

Prerequisites
* None
#
- Unit: What is Django?

    * Background

        Django (pronounced "jango") is a free and open source framework that was first released in 2005 and was named after a famous jazz guitarist Django Reinhardt. Over the years many Python frameworks have been developed, but Django has become one of the most popular because of its flexibility and security. It is suitable for both frontend and backend web development and the integrated Python libraries make it easy for rapid development. Django has become widely accepted across industries and because of its growing popularity, providers are more readily available to support Django applications on their platforms.

    * Application types

        Django offers a complete framework solution, which means it provides everything you need to quickly deploy your projects. Because Django offers great out of the box security, a vast community of users, and can scale on demand, this has become a framework of choice by most developers.  By using Django you have the ability to develop complex and database driven web applications that can include:
        * Machine learning
        * E-commerce platforms
        * Data analysis
        * Content Management

    * Django vs Flask

        While both of these frameworks could suit your needs for your next Python application, there are specific functionalities and levels of support that each provide. Let's quickly go through the differences so you can make the choice on which one is best suited for your needs.
        - Django
            1. Full-stack framework
            2. Ideal for complex data driven applications
            3. More of a learning curve
            4. Vast amount of users for support
            5. Out of the box security
            6. Numerous apps to help with your projects
            7. Suitable for development and production
        - Flask
            1. Lightweight web framework
            2. Great for smaller projects
            3. Bare bones framework so less of a learning curve 
            4. Uses Jinja2 as a templating language
            5. More control over elements within your application
            6. Suitable for development
        
        As you can see Django and Flask each offer great benefits for your projects. When choosing the right framework, spending a little time to think about not only the type and complexity of the application but also the end product will save you time and frustration in the end.


#        
- Unit: Installation

    While the Django framework may have a little bit of a learning curve, installing it is pretty simple with the steps below: 
    - The first step is to visit the Django website at this [link][3].
    - When viewing the Django website, you will have the choice to go through the tutorials and documentation, or just downloading the framework.
        * If you choose to read through some of documentation and tutorials then click [here][4]. This page gives you all the information you need to learn Django and also great ways to be a part of their community.
        * If you choose to just download the program then click the 'Download' button
            * You will then be given two options for the framework depending on which version you would like to use. For this lesson we are using the latest official version.
                * If you want to browse through the Django installation guide before downloading it can be found [here][1]. They also have a quick install guide that can be found [here][5].
                * Before downloading, also check that your Python version is the one that Django recommends. 
                    * If you do not have the recommended version of Python, then follow this [link][2] to the Python website to download the correct version.
            * Please note it is best practice to create virtual environments per project so as not to affect your other applications. Therefore, creating a virtual enviroment to hold your Django framework should also be considered before installing.

#
- Unit: Hello, Django
    * Create a project with Django-admin

        Now that Django is installed we are ready to begin the process of creating a project, but before we actually start coding there are a couple of things we have to do to create a Django project. While there are a couple of options for completing the following tasks for our purposes we will be using Visual Studio Code.
        
        First, go to the command line and navigate to the directory that you would like to store your Django project. Once you are in the correct directory then run the following command to create your new project.

        * If you decided to create a virtual environment for your Django framework, then make sure you are running this command from your activated virtual environment. 
            ~~~
            $ django-admin startproject myfirstproject
            ~~~ 
        After running the above command the new project should now be in your chosen directory. In this instance you would see a new folder called 'myfirstproject'.

    * Navigating the Project structure

        Now that the Django project has been created let's look at the structure to see what was included.
        ~~~
        myfirstproject/
                manage.py
                myfirstproject/
                        __init__.py
                        settings.py
                        urls.py
                        asgi.py
                        wsgi.py
        ~~~
        1. The first or outer __myfirstproject__ in the structure is your root directory which contains the entire project.
        2. Next you have __manage__.__py__. This is a command-line utility that is created in every Django project and actually has the same function as 'django-admin'. Below is an example of how this could be used if you were inside the project folder and wanted to see the available subcommands. 
        
            For more information about these two command-line utilities click [here][6].
        ~~~
            django-admin help

            OR

            python manage.py help
        ~~~
        3. The inner __myfirstproject__ is considered the Python package for your project.
        4. Next we have __init__.__py__ and if you look at the contents of this file you will notice that it is empty. Don't worry as this should be empty and it functions to tell Python that this directory should be considered a package.
        5. Next in line we have __settings__.__py__. This file contains all of your settings or configurations.
        6. Next is __urls__.__py__. This file acts as a table of contents for all of the urls within the project.
        7. Lastly we have __asgi__.__py__ and __wsgi__.__py__. These last two files serve as the entry point for your web servers depending on what type of server is deployed.

    * Running Your First Project

        Now that Django is installed, a project has been created, and we have investigated the project structure it is time to make sure everything works.

        Navigate to the __myfirstproject__ root directory and enter the below in the command line.
        ~~~
        python manage.py runserver
        ~~~
        If everything works it will start to perform system checks, and start your development server. Copy and paste the url of your development server in your preferred browser, and if everything is running correctly you will see a Django 'Congratulations' page with a rocket taking off.

    * Projects vs Apps

        Now that the first Django project has been created, we will continue on to create our first app but let's first define the difference between a project and an app. 
        * App - provides the instructions of how a web application should function such as our "Hello, world!" app.

        * Project - contains all of the necessary settings or apps for a specific website.
        
        Now that we know the difference between a project and an app let's move to our next task of creating an app!

#
* Unit: Creating Your First App

    * Creating Hello, world!

        In order to create the app, we first start by navigating to the project root folder __myfirstproject__ and input the following on the command line.
        
            python manage.py startapp hello_world
           
        With this command, Django will automatically create the required folders and files and the following structure should now be visible.

        ~~~  
        hello_world/
            __init__.py
            admin.py
            apps.py
            migrations/
                __init__.py
            models.py
            tests.py
            views.py
        ~~~
           
    * Creating a View

        Now that the app has been created, we can begin to take the necessary steps so it will perform a simple function. The first step in the process is to create a view.  

        Go into the __views__.__py__ file contained within the __hello_world__ directory and enter the below information:

            from django.http import HttpResponse

            def index(request):
                return HttpResponse("Hello, world!")

        
        Creating a view is an essential action, as it handles what views to return when a specific URL is sent as a request. In the next section, we will now map the URL so this view can be called. 

    * URL Mapping

        Now that a view has been created, the next step is to map it to the appropriate URL. In Django this is called a URLconf and it serves as a table of contents for your app.
        
        To begin this process create another file in the __hello_world__ directory named __urls__.__py__ and enter the below code.

            from django.urls import path
            from . import views

            urlpatterns = [
                path('', views.index, name='index'),
            ]

        The most important part of this code is the __urlpatterns__ tuple, as this is where the views and URLs are connected or mapped. As you can see, we have imported our __views__.__py__ file so we are able to use it within the __urlpatterns__ code. 

        Now that we have created our URLconf for our app, we must now create one in our project root directory.

        Go to the second __myfirstproject__ directory and in the __urls__.__py__ file enter the below code.

            from django.contrib import admin
            from django.urls import include, path
            
            urlpatterns = [
                path('hello_world/', include('hello_world.urls')),
                path('admin/', admin.site.urls),
            ]

        When opening the file you will notice Django has already populated some of the code, and our task will be to add our new app path to the existing code. In addition to adding the new path, you will also need to import another function named __include__ from __django.urls__. 

    * Understanding the __Include__ Function

        As you continue to learn and have more complex file structures, you will add more views and URLs for your app. This function plays a key role in your app, as it allows you to call other URLconfs.

        For example, we currently have the path __/hello_world/__ that directs us to our index view and displays "Hello, world!". Let's say we wanted to add another view to our app so we could display a simple greeting to the user. In order to add another view we would add the following to our __hello_world.views.py__ file.

            def user(request, user_id)
                response = "Hello user # %s."
                return HttpResponse(response % user_id)

        Next in the __hello_world/url.py__ file add the following:

            path('<user_id>', views.user, name='user'),

        If we now called this view by entering http://localhost:8000/hello_world/5 in our browser, Django would first look in __myfirstproject.urls__ and search for the urlpatterns. After finding the first match for __hello_world/__, it would then strip that part from the URL and continue with the remaining string to the __hello_world.urls__ where it would continue looking for a match. After finding the match, it would then diplay the appropriate view. This function allows a simple way to manage and organize URLs within the application and provides greater freedom to change path roots without breaking the app.

    
    * Running Your First App

        Now that the structure is complete, views have been added, and the URLs mapped, it is time to run your app by entering the below link into your browser.

            http://localhost:8000/hello_world/

        If everything worked then you should see "Hello, world" at the top left hand of the screen.
   
6. Knowledge Check
    * Check your knowledge
      - Questions (See Module1_KQ.yaml for questions)

7. Summary
    * In this module you learned:
      - How to install Django
      - The difference between a project and an app
      - How to create and configure a simple app
    * In the next module of this learning path, you will learn about Django's Object-Relational Mapper (ORM), how to install and manage a SQLite database, and then create and query data.