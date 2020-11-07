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
* Learning Objectives
    - In this module you will learn:
        - Why Django is used for quick deployment of web applications
        - What types of applicatons are best for Django
        - How to install Django
        - How to create a simple program in Django
#
- Unit: What is Django?

    * Background

        Django is a free and open source web framework that was developed to ease the creation of complex, database driven websites. With its collection of installed Python libraries it emphasizes less code and rapid development while focusing on sustainability and security. The great element about this framework is that it takes the hassle out of web development and leaves you to focus on your web application.

    * Application types

        Because Django offers a complete framework solution and provides both the frontend and backend, you have the ability to develop complex and fast scaling web applications. Some of these application types can include:
        * Machine learning
        * E-commerce platforms
        * Data analysis

    * Django vs Flask

        While both of these frameworks could suit your needs for your next Python application there are specific functionalities and levels of support that each provide. Let's quickly go through the differences, and find the one best suited for your needs.
        - Django is a high-level Python full stacked web framework that contains about everything you need to write your application which allows you to focus on your final product. The great thing about Django is that it can be used for both the frontend and backend. While the vanilla version might not do everything that you want because of the huge community of users there are numerous apps that could suit your needs.
        - Flask is a lightweight web framework based on Werkzeug and Jinja 2. Flask is used for your backend development, and gives you ability to create templates with a templating language called Jinja2. These templates can be created in different formats such as HTML, or XML and returned in an HTTP request.
        While Flask provides greater flexibility in your development by allowing you to have more control over your components, unfortunately it is not suitable for production. Because Flask is not suitable for production, you would then need to take an extra step of deploying the program to a web server that was able to communicate with Flask.
#        
- Unit: Installation

    While the Django framework may be a little bit of a learning curve installing it is pretty simple with the steps below. 
    - The first step is to visit the Django website at this [link][3].
    - When viewing the Django website, you will have the choice to go through the tutorials and documentation, or just downloading the framework.
        - If you choose to read through some of documentation and tutorials then click [here][4]. This page gives you all the information you need to learn Django and also great ways to be a part of their community.
        - If you choose to just download the program then click the 'Download' button
            - You will then be given two options for the framework depending on which version you would like to use. For this lesson we are using the latest official version.
                * If you want to browse through the Django installation guide before downloading it can be found [here][1]. They also have a quick install guide that can be found [here][5].
                * Before downloading also check that your Python version is the one that Django recommends. 
                    * If you do not have the recommended version of Python, then follow this [link][2] to the Python website to download the correct version.
                * Please note it is best practice to create virtual environments per project so as not to affect your other applications. Therefore, creating a virtual enviroment should also be considered to install the Django framework.

#
- Unit: Hello, Django
    * Create a project and application with Django-admin

        Now that Django is installed we are ready to begin the process of creating an application. But before we actually get to coding our first program there are a couple of things we have to do to create a Django project.
        * First, set up your Django project by using your command line to go to the directory that you would like to store your code. Once you are in the correct directory then run the following command to create your new project.
            * If you decided to create a virtual environment for your Django framework, then make sure you are running this command from your activated virtual environment. 
        ~~~
        $ django-admin startproject myfirstproject
        ~~~ 
        - After running the above the command you should now see your new project in your chosen folder. In this instance I would see a new folder called 'myfirstproject'.

    * Navigating the structure

        Now that you have created your Django project let's look at the structure.
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
        1. The first or outer 'myfirstproject' in the project structure is your root directory which contains the entire project.
        2. Next you have 'manage.py'. This is a command-line utility that is created in every Django project and actually has the same function as 'django-admin'. Below is an example of how you could use this command-line utility if you were inside of your project and wanted to see the available subcommands. For more information about these two command-line utilities click [here][6].
        ~~~
            django-admin help
            OR
            python manage.py help
        ~~~
        3. The inner 'myfirstproject' is the Python package for your project.
        4. Next we __init__.py and if you look at this file you will see that it is empty. Don't worry this is supposed to be empty, and it functions to tell Python that this directory should be considered a package.
        5. Next in line we have 'settings.py'. This file contains all of your settings or configurations for this project.
        6. Next is 'urls.py'. This file acts as a table of contents for all of the urls within the project.
        7. Lastly we have 'asgi.py' and 'wsgi.py'. These last two files serve as the entry point for your web servers depending on what type of server is deployed.

    * Checking The Installation

        Now that you have installed Django, and we have gone over what actually creates the project structure it is time to make sure everything works.

        Go to the outer folder of 'myfirstproject' and type:
        ~~~
        python manage.py runserver
        ~~~
        If everything works it will start to perform system checks, and start your development server. Copy and paste the url of your development server in your preferred browser, and if everything is running correctly you will see a 'Congratulations' page with a rocket taking off.
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