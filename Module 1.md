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
    The Python language has quickly become one of the most popular programming languages, and finding the right platform for your application is crucial for on time deployments. This module will discuss a popular framework named Django that is based on the Python language. In order to begin to understand the Django framework we will take you through the types of applications that are best suited for deployment, installation, and creating your first program.

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

        Django (pronounced "jango") is a free and open source framework that was first released in 2005, and was named after a famous jazz guitarist Django Reinhardt. Over the years many Python frameworks have been developed, but Django has become one of the most popular because of its flexibility and security. It is suitable for both frontend and backend web development, and the integrated Python libraries make it easy for rapid development. Django has become widely accepted across industries, and because of its growing popularity providers are more readily available to support Django applications on their platforms.

    * Application types

        Django offers a complete framework solution which means it provides everything you need to quickly deploy your projects. Because Django offers great out of the box security, a vast community of users, and can scale on demand this has become a framework of choice by most developers.  By using Django you have the ability to develop complex and database driven web applications that can include:
        * Machine learning
        * E-commerce platforms
        * Data analysis
        * Content Management

    * Django vs Flask

        While both of these frameworks could suit your needs for your next Python application there are specific functionalities and levels of support that each provide. Let's quickly go through the differences so you can make the choice on which one is best suited for your needs.
        - Django
            1. Full-stack framework
            2. Ideal for complex data driven applications
            3. More of a learning curve because of everything included
            4. Vast amount of users for support
            5. Out of the box security
            6. Numerous apps to help with your application
            7. Suitable for development, and production
        - Flask
            1. Lightweight web framework
            2. Great for smaller projects
            3. Bare bones framework so less of a learning curve 
            4. Uses Jinja2 as a templating language
            5. More control over elements within your application
            6. Suitable for development
        
        As you can see Django and Flask each offer great benefits for your projects. When choosing the right framework spending a little time to think about not only the type and complexity of the application, but also the end product will save you time and frustration in the end.


#        
- Unit: Installation

    While the Django framework may be a little bit of a learning curve installing it is pretty simple with the steps below. 
    - The first step is to visit the Django website at this [link][3].
    - When viewing the Django website, you will have the choice to go through the tutorials and documentation, or just downloading the framework.
        * If you choose to read through some of documentation and tutorials then click [here][4]. This page gives you all the information you need to learn Django and also great ways to be a part of their community.
        * If you choose to just download the program then click the 'Download' button
            * You will then be given two options for the framework depending on which version you would like to use. For this lesson we are using the latest official version.
                * If you want to browse through the Django installation guide before downloading it can be found [here][1]. They also have a quick install guide that can be found [here][5].
                * Before downloading also check that your Python version is the one that Django recommends. 
                    * If you do not have the recommended version of Python, then follow this [link][2] to the Python website to download the correct version.
            * Please note it is best practice to create virtual environments per project so as not to affect your other applications. Therefore, creating a virtual enviroment to hold your Django framework should also be considered before installing.

#
- Unit: Hello, Django
    * Create a project and application with Django-admin

        Now that Django is installed we are ready to begin the process of creating an application, but before we actually start coding our first program there are a couple of things we have to do to create a Django project. While there are a couple of options for completing the following tasks for our purposes we will be using Visual Studio Code.
        * First, go to the command line and navigate to the directory that you would like to store your Django application. Once you are in the correct directory then run the following command to create your new project.
            * If you decided to create a virtual environment for your Django framework, then make sure you are running this command from your activated virtual environment. 
            ~~~
            $ django-admin startproject myfirstproject
            ~~~ 
        - After running the above command you should now see your new project in your chosen directory. In this instance I would see a new folder called 'myfirstproject'.

    * Navigating the structure

        Now that the new Django project has been created let's look at the structure.
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
        2. Next you have __manage__.__py__ This is a command-line utility that is created in every Django project and actually has the same function as 'django-admin'. Below is an example of how you could use this command-line utility if you were inside of your project and wanted to see the available subcommands. For more information about these two command-line utilities click [here][6].
        ~~~
            django-admin help

            OR

            python manage.py help
        ~~~
        3. The inner __myfirstproject__ is the Python package for your project.
        4. Next we __init__.__py__ and if you look at the contents of this file you will see that it is empty. Don't worry this is supposed to be empty, and it functions to tell Python that this directory should be considered a package.
        5. Next in line we have __settings__.__py__. This file contains all of your settings or configurations.
        6. Next is __urls__.__py__. This file acts as a table of contents for all of the urls within the project.
        7. Lastly we have __asgi__.__py__ and __wsgi__.__py__. These last two files serve as the entry point for your web servers depending on what type of server is deployed.

    * Running Your First Project

        Now that you have installed Django, created a project, and have learned about the project structure it is time to make sure everything works.

        Go to the outer folder of __myfirstproject__ and type:
        ~~~
        python manage.py runserver
        ~~~
        If everything works it will start to perform system checks, and start your development server. Copy and paste the url of your development server in your preferred browser, and if everything is running correctly you will see a 'Congratulations' page with a rocket taking off.

    * Projects vs Apps

        Now that you have created your first Django project, we will move on to create your first application but first lets define the difference between a project and an application. After you created the __myfirstproject__ project folder you saw it contained all of the necessary componects to run the Django 'Congratulations' page, but what it lacked was actually being able to perform a function. As you will see in the next task an application will be created, within the __myfirstproject__ project folder called Hello, World!, that will perform a simple function and print 'Hello, World' on the screen. As you start to develop more complex projects you will notice multiple apps within your project structure, and that your apps may even span across multiple projects.

    * Hello, world!

        In this lesson the real fun begins as we begin to create our first program. 

5. Routing and views
    * Routing concepts
    * Registering routes
    * Introducing views
    * Creating a view
6. Knowledge Check
    * Check your knowledge
      - Questions
7. Summary
    * In this module you learned:
      - How to install Django
      - How to navigate the Django platform
      - How to create a simple program
    * In the next module in this Learning Path,